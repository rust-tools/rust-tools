const fs = require('fs');

function findID(filePath = 'data/items.json', search_term = null, search_by_id = false) {
    if (search_term === null) {
        search_term = prompt("Enter item name or id: ").toLowerCase();
    }

    let data = JSON.parse(fs.readFileSync(filePath, 'utf8'));

    for (let id in data) {
        let info = data[id];
        if (search_by_id) {
            if (id.toLowerCase() === search_term) {
                return info['name'];
            }
        } else if (info['name'].toLowerCase() === search_term || info['shortname'] === search_term) {
            return id;
        }
    }

    return "Not a valid item name or id.";
}

function findDurability(itemType, itemName, raidType = 'explo', durabFile = 'data/rustlabsDurabilityData.json') {
    let raidTypeList = ['eco', 'explo'];
    let itemTypeList = ['deployable', 'vehicle', 'building'];
    let itemsFile = 'data/items.json';
    let cheapest = Infinity;
    let dict_ = {};
    let list_ = [];
    let dellist = [];

    let data = JSON.parse(fs.readFileSync(durabFile, 'utf8'));

    if (!raidTypeList.includes(raidType)) {
        return "Invalid Raid Type";
    }
    if (!itemTypeList.includes(itemType)) {
        return "Invalid Item Type";
    }

    let search_term = (itemType === 'deployable') ? findID(itemsFile, itemName) : itemName;

    for (let info of Object.values(data)) {
        for (let item in info) {
            if (search_term === item) {
                for (let i of info[item]) {
                    for (let key in i) {
                        let value = i[key];
                        if (key === "group" || key === "quantity" || key === "time" || key === "timeString" || key === "fuel" || key === "sulfur") {
                            list_.push(value);
                        }
                        if (key === "toolId") {
                            let raidTool = findID(itemsFile, value, true);
                            dict_[raidTool] = list_;
                            list_ = [];
                        }
                    }
                }
            }
        }
    }

    if (raidType === 'eco') {
        for (let key in dict_) {
            if (dict_[key][0] !== 'melee') {
                dellist.push(key);
            }
        }
    } else if (raidType === 'explo') {
        for (let key in dict_) {
            if (dict_[key][0] !== 'explosive') {
                dellist.push(key);
            }
        }
    }

    for (let i of dellist) {
        delete dict_[i];
    }

    if (raidType === 'explo') {
        for (let value of Object.values(dict_)) {
            if (value[-1] !== null && value[-1] < cheapest) {
                cheapest = value[-1];
            }
        }

        for (let key in dict_) {
            if (dict_[key][-1] === cheapest) {
                return `Trying to ${raidType}raid: ${itemName}\nBest option to ${raidType}raid: ${key}\nCost: ${dict_[key][-1]} sulfur\nTime to raid: ${dict_[key][3]}\nQuantity needed: ${dict_[key][1]}`;
            }
        }
    } else if (raidType === 'eco') {
        for (let value of Object.values(dict_)) {
            if (value[2] !== null && value[2] < cheapest) {
                cheapest = value[2];
            }
        }

        for (let key in dict_) {
            if (dict_[key][2] === cheapest) {
                return `Trying to ${raidType}raid: ${itemName}\nBest option to ${raidType}raid: ${key}\nTime to ${raidType}raid: ${dict_[key][3]}\nQuantity needed: ${dict_[key][1]}`;
            }
        }
    }
}