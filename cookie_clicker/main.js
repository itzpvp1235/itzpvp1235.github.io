var cookies = 0
var cookies_per_second = 0

let prestige_level = 0
let prestige_cost =  1000000
let cookies_until_prestige = 1000000
let prestige_button = false
let cookies_per_click = 1
let itteration_count = 0
let cookies_per_click_upgrade_cost = 1000
let cookies_upgrade_add_value = 10
let cookie_upgrade_level = 0
let cookies_required_to_win = 1000000000000000000000000
let decrease_amount = 0.95
let decrease_cost = 5000
let upgrade_reduce_cost = 10000
let upgrade_reduce_amount = 0.85

let cursors = 0
let grandmas = 0
let factories = 0
let networks = 0
let cookie_stashes = 0
let cookie_duplicators = 0
let time_machines = 0
let cookie_guys = 0
let time_machine_factories = 0

let cursor_cost = 10
let grandma_cost = 100
let factory_cost = 500
let network_cost = 2000
let cookie_stash_cost = 10000
let cookie_duplicator_cost = 30000
let time_machine_cost = 300000
let cookie_guy_cost = 1000000
let time_machine_factory_cost = 5000000

let CURSOR_AMOUNT = 0.1
let GRANDMA_AMOUNT = 1
let FACTORY_AMOUNT = 5;
let NETWORK_AMOUNT = 20;
let COOKIE_STASH_AMOUNT = 100;
let COOKIE_DUPLICATOR_AMOUNT = 300;
let TIME_MACHINE_AMOUNT = 3000;
let COOKIE_GUY_AMOUNT = 10000;
let TIME_MACHINE_FACTORY_AMOUNT = 50000;

let use_anti_cheat = true

function update_all_feilds() {
    document.getElementById("cursor-count").innerHTML = "Amount: " + cursors.toString();
    document.getElementById("cursor-cost").innerHTML = "Cost: " + cursor_cost.toString();
    document.getElementById("grandma-count").innerHTML = "Amount: " + grandmas.toString();
    document.getElementById("grandma-cost").innerHTML = "Cost: " + grandma_cost.toString();
    document.getElementById("factory-count").innerHTML = "Amount: " + factories.toString();
    document.getElementById("factory-cost").innerHTML = "Cost: " + factory_cost.toString();
    document.getElementById("network-count").innerHTML = "Amount: " + networks.toString();
    document.getElementById("network-cost").innerHTML = "Cost: " + network_cost.toString();
    document.getElementById("cookiestash-count").innerHTML = "Amount: " + cookie_stashes.toString();
    document.getElementById("cookiestash-cost").innerHTML = "Cost: " + cookie_stash_cost.toString();
    document.getElementById("cookiedupe-count").innerHTML = "Amount: " + cookie_duplicators.toString();
    document.getElementById("cookiedupe-cost").innerHTML = "Cost: " + cookie_duplicator_cost.toString();
    document.getElementById("timemachine-count").innerHTML = "Amount: " + time_machines.toString();
    document.getElementById("timemachine-cost").innerHTML = "Cost: " + time_machine_cost.toString();
    document.getElementById("cookieguy-count").innerHTML = "Amount: " + cookie_guys.toString();
    document.getElementById("cookieguy-cost").innerHTML = "Cost: " + cookie_guy_cost.toString();
    document.getElementById("timemachinefactory-count").innerHTML = "Amount: " + time_machine_factories.toString();
    document.getElementById("timemachinefactory-cost").innerHTML = "Cost: " + time_machine_factory_cost.toString();
    document.getElementById("cookies-per-second").innerHTML = "Per second: " + cookies_per_second.toString();
    document.getElementById("upgrade-reduce").innerHTML = "Purchase for $" + upgrade_reduce_cost.toString();
    document.getElementById("upgrade-cost-reduce").innerHTML = "Purchase for $" + decrease_cost.toString();
    document.getElementById("upgrade-cookie").innerHTML = "Upgrade for $" + cookies_per_click_upgrade_cost.toString();
}

function save() {
    document.getElementById("save-sec").style.display = "block"

    document.getElementById("text").innerHTML = cookies.toString() + " " +
        cookies_per_second.toString() + " " +
        prestige_level.toString() + " " +
        prestige_cost.toString() + " " +
        cookies_until_prestige.toString() + " " +
        prestige_button.toString() + " " +
        cookies_per_click.toString() + " " +
        itteration_count.toString() + " " +
        cookies_per_click_upgrade_cost.toString() + " " +
        cookies_upgrade_add_value.toString() + " " +
        cookie_upgrade_level.toString() + " " +
        cookies_required_to_win.toString() + " " +
        decrease_amount.toString() + " " +
        decrease_cost.toString() + " " +
        upgrade_reduce_cost.toString() + " " +
        upgrade_reduce_amount.toString() + " " +
        cursors.toString() + " " +
        grandmas.toString() + " " +
        factories.toString() + " " +
        networks.toString() + " " +
        cookie_stashes.toString() + " " +
        cookie_duplicators.toString() + " " +
        time_machines.toString() + " " +
        cookie_guys.toString() + " " +
        time_machine_factories.toString() + " " +
        cursor_cost.toString() + " " +
        grandma_cost.toString() + " " +
        factory_cost.toString() + " " +
        network_cost.toString() + " " +
        cookie_stash_cost.toString() + " " +
        cookie_duplicator_cost.toString() + " " +
        time_machine_cost.toString() + " " +
        cookie_guy_cost.toString() + " " +
        time_machine_factory_cost.toString() + " " +
        CURSOR_AMOUNT.toString() + " " +
        GRANDMA_AMOUNT.toString() + " " +
        FACTORY_AMOUNT.toString() + " " +
        NETWORK_AMOUNT.toString() + " " +
        COOKIE_STASH_AMOUNT.toString() + " " +
        COOKIE_DUPLICATOR_AMOUNT.toString() + " " +
        TIME_MACHINE_AMOUNT.toString() + " " +
        COOKIE_GUY_AMOUNT.toString() + " " +
        TIME_MACHINE_FACTORY_AMOUNT.toString()
}

function close_save_menu() {
    document.getElementById("save-sec").style.display = "none"
}

function load() {
    document.getElementById("load-sec").style.display = "block";
    document.getElementById("load-error").style.display = "none";

    let box_value = document.getElementById("load-input").value = ""
}

function validate_load_string(str) {
    // Length of split list should equal 43

    let load_string = str.split(" ")
    let correct_length = load_string.length === 43

    let valid = load_string[6] === "true" || "false"
    return valid && correct_length
}

function confirm_load() {
    use_anti_cheat = false
    let box_value = document.getElementById("load-input").value

    if (validate_load_string(box_value)) {
        document.getElementById("load-error").style.display = "none";
        document.getElementById("load-sec").style.display = "none";

        let box_value_list = box_value.split(" ")

        for (let i=0; i<43; i++) {
            box_value_list[i] = Number(box_value_list[i])
        }

        cookies = box_value_list[0]
        cookies_per_second = box_value_list[1]

        prestige_level = box_value_list[2]
        prestige_cost = box_value_list[3]
        cookies_until_prestige = box_value_list[4]
        prestige_button = box_value_list[5] === "true"
        cookies_per_click = box_value_list[6]
        itteration_count = box_value_list[7]
        cookies_per_click_upgrade_cost = box_value_list[8]
        cookies_upgrade_add_value = box_value_list[9]
        cookie_upgrade_level = box_value_list[10]
        cookies_required_to_win = box_value_list[11]
        decrease_amount = box_value_list[12]
        decrease_cost = box_value_list[13]
        upgrade_reduce_cost = box_value_list[14]
        upgrade_reduce_amount = box_value_list[15]

        cursors = box_value_list[16]
        grandmas = box_value_list[17]
        factories = box_value_list[18]
        networks = box_value_list[19]
        cookie_stashes = box_value_list[20]
        cookie_duplicators = box_value_list[21]
        time_machines = box_value_list[22]
        cookie_guys = box_value_list[23]
        time_machine_factories = box_value_list[24]

        cursor_cost = box_value_list[25]
        grandma_cost = box_value_list[26]
        factory_cost = box_value_list[27]
        network_cost = box_value_list[28]
        cookie_stash_cost = box_value_list[29]
        cookie_duplicator_cost = box_value_list[30]
        time_machine_cost = box_value_list[31]
        cookie_guy_cost = box_value_list[32]
        time_machine_factory_cost = box_value_list[33]

        CURSOR_AMOUNT = box_value_list[34]
        GRANDMA_AMOUNT = box_value_list[35]
        FACTORY_AMOUNT = box_value_list[36]
        NETWORK_AMOUNT = box_value_list[37]
        COOKIE_STASH_AMOUNT = box_value_list[38]
        COOKIE_DUPLICATOR_AMOUNT = box_value_list[39]
        TIME_MACHINE_AMOUNT = box_value_list[40]
        COOKIE_GUY_AMOUNT = box_value_list[41]
        TIME_MACHINE_FACTORY_AMOUNT = box_value_list[42]

        document.getElementById("prestige-paragraph").innerHTML = "You have reached " + prestige_cost +
            " cookies<br>you can prestige for " + prestige_cost + " to get double cookies"

        display_cookie_with_prefix()
        update_all_feilds()
        validate_items()
    } else {
        document.getElementById("load-error").style.display = "block";
    }

    use_anti_cheat = true
}

function cancel_load() {
    document.getElementById("load-sec").style.display = "none";
    document.getElementById("load-error").style.display = "block";
}

function display_cookie_with_prefix() {
    cookies = Math.round(cookies * 10) / 10;
    if (cookies >= 999000000000000000000000) {
        document.getElementById("cookies").innerHTML = "Cookies: " + (Math.round((cookies * 100) / 1000000000000000000000000) / 100).toString() + "SEPT";
    } else if (cookies >= 999000000000000000000) {
        document.getElementById("cookies").innerHTML = "Cookies: " + (Math.round((cookies * 100) / 1000000000000000000000) / 100).toString() + "SEXT";
    } else if (cookies >= 999000000000000000) {
        document.getElementById("cookies").innerHTML = "Cookies: " + (Math.round((cookies * 100) / 1000000000000000000) / 100).toString() + "QUINT";
    } else if (cookies >= 999000000000000) {
        document.getElementById("cookies").innerHTML = "Cookies: " + (Math.round((cookies * 100) / 1000000000000000) / 100).toString() + "QUAD";
    } else if (cookies >= 999000000000) {
        document.getElementById("cookies").innerHTML = "Cookies: " + (Math.round((cookies * 100) / 1000000000000) / 100).toString() + "T";
    } else if (cookies >= 999000000) {
        document.getElementById("cookies").innerHTML = "Cookies: " + (Math.round((cookies * 100) / 1000000000) / 100).toString() + "B";
    } else if (cookies >= 999000) {
        document.getElementById("cookies").innerHTML = "Cookies: " + (Math.round((cookies * 100) / 1000000) / 100).toString() + "M";
    } else if (cookies >= 1000) {
        document.getElementById("cookies").innerHTML = "Cookies: " + (Math.round((cookies * 100) / 1000) / 100).toString() + "K";
    } else {
        document.getElementById("cookies").innerHTML = "Cookies: " + (Math.round(cookies * 10) / 10).toString();
    }
}

function add_cookie() { 
    cookies+= cookies_per_click
    display_cookie_with_prefix()
}

function round_prices() {
    cookies_per_second = Math.round(cookies_per_second * 10) / 10
    cookies = Math.round(cookies * 10) / 10
    cursor_cost = Math.round(cursor_cost * 10) / 10
    grandma_cost = Math.round(grandma_cost * 10) / 10
    factory_cost = Math.round(factory_cost * 10) / 10
    network_cost = Math.round(network_cost * 10) / 10
    cookie_stash_cost = Math.round(cookie_stash_cost * 10) / 10
    cookie_duplicator_cost = Math.round(cookie_duplicator_cost * 10) / 10
    time_machine_cost = Math.round(time_machine_cost * 10) / 10
    cookie_guy_cost = Math.round(cookie_guy_cost * 10) / 10
    time_machine_factory_cost = Math.round(time_machine_factory_cost * 10) / 10
}

function add_generator() {
    let gen_type = event.target.id;

    if (gen_type === "cursor") {
        if (cookies >= cursor_cost) {
            cookies_per_second += CURSOR_AMOUNT;
            cookies -= cursor_cost;
            cursors++;
            cursor_cost = cursor_cost * 1.01
            round_prices()
            document.getElementById("cursor-count").innerHTML = "Amount: " + cursors.toString();
            document.getElementById("cursor-cost").innerHTML = "Cost: " + cursor_cost.toString();
        }
    } else if (gen_type === "grandma") {
        if (cookies >= grandma_cost) {
            cookies_per_second += GRANDMA_AMOUNT;
            cookies -= grandma_cost;
            grandmas++;
            grandma_cost = grandma_cost * 1.01
            round_prices()
            document.getElementById("grandma-count").innerHTML = "Amount: " + grandmas.toString();
            document.getElementById("grandma-cost").innerHTML = "Cost: " + grandma_cost.toString();
        }
    } else if (gen_type === "factory") {
        if (cookies >= factory_cost) {
            cookies_per_second += FACTORY_AMOUNT;
            cookies -= factory_cost;
            factories++;
            factory_cost = factory_cost * 1.001
            round_prices()
            document.getElementById("factory-count").innerHTML = "Amount: " + factories.toString();
            document.getElementById("factory-cost").innerHTML = "Cost: " + factory_cost.toString();
        }
    } else if (gen_type === "network") {
        if (cookies >= network_cost) {
            cookies_per_second += NETWORK_AMOUNT;
            cookies -= network_cost;
            networks++;
            network_cost = network_cost * 1.0008
            round_prices()
            document.getElementById("network-count").innerHTML = "Amount: " + networks.toString();
            document.getElementById("network-cost").innerHTML = "Cost: " + network_cost.toString();
        }
    } else if (gen_type === "cookiestash") {
        if (cookies >= cookie_stash_cost) {
            cookies_per_second += COOKIE_STASH_AMOUNT;
            cookies -= cookie_stash_cost;
            cookie_stashes++;
            cookie_stash_cost = cookie_stash_cost * 1.0006
            round_prices()
            document.getElementById("cookiestash-count").innerHTML = "Amount: " + cookie_stashes.toString();
            document.getElementById("cookiestash-cost").innerHTML = "Cost: " + cookie_stash_cost.toString();
        }
    } else if (gen_type === "cookiedupe") {
        if (cookies >= cookie_duplicator_cost) {
            cookies_per_second += COOKIE_DUPLICATOR_AMOUNT;
            cookies -= cookie_duplicator_cost;
            cookie_duplicators++;
            cookie_duplicator_cost = cookie_duplicator_cost * 1.0003
            round_prices()
            document.getElementById("cookiedupe-count").innerHTML = "Amount: " + cookie_duplicators.toString();
            document.getElementById("cookiedupe-cost").innerHTML = "Cost: " + cookie_duplicator_cost.toString();
        }
    } else if (gen_type === "timemachine") {
        if (cookies >= time_machine_cost) {
            cookies_per_second += TIME_MACHINE_AMOUNT;
            cookies -= time_machine_cost;
            time_machines++;
            time_machine_cost = time_machine_cost * 1.0001
            round_prices()
            document.getElementById("timemachine-count").innerHTML = "Amount: " + time_machines.toString();
            document.getElementById("timemachine-cost").innerHTML = "Cost: " + time_machine_cost.toString();
        }
    } else if (gen_type === "cookieguy") {
        if (cookies >= cookie_guy_cost) {
            cookies_per_second += COOKIE_GUY_AMOUNT;
            cookies -= cookie_guy_cost;
            cookie_guys++;
            cookie_guy_cost = cookie_guy_cost * 1.00005
            round_prices()
            document.getElementById("cookieguy-count").innerHTML = "Amount: " + cookie_guys.toString();
            document.getElementById("cookieguy-cost").innerHTML = "Cost: " + cookie_guy_cost.toString();
        }
    } else if (gen_type === "timemachinefactory") {
        if (cookies >= time_machine_factory_cost) {
            cookies_per_second += TIME_MACHINE_FACTORY_AMOUNT;
            cookies -= time_machine_factory_cost;
            time_machine_factories++;
            time_machine_factory_cost = time_machine_factory_cost * 1.0001
            round_prices()
            document.getElementById("timemachinefactory-count").innerHTML = "Amount: " + time_machine_factories.toString();
            document.getElementById("timemachinefactory-cost").innerHTML = "Cost: " + time_machine_factory_cost.toString();
        }
    } else {
        alert("Error while trying to process shop purchase: " + gen_type.toString());
    }

    display_cookie_with_prefix()
    cookies_per_second = Math.round(cookies_per_second * 10) / 10;
    document.getElementById("cookies-per-second").innerHTML = "Per second: " + cookies_per_second.toString();
}

document.addEventListener('DOMContentLoaded', function() {
    window.setInterval(function() {
        if (itteration_count === 19) {
            add_cookies();
            itteration_count = 0
        } else {
            itteration_count++
        }

        validate_items();
        test_for_upgrade();
        check_win();

        if (use_anti_cheat) {
            cheat_detection();
        }
        progress_bar();
    }, 50);
 }, false);

function progress_bar() {
    let bar = document.getElementById("cookies-win-progress");

    bar.value = cookies.toString();

    if (bar.value >= bar.max) {
        bar.max = bar.value * 10;
        document.getElementById("progress-label").innerHTML = (bar.max).toString();

    }
}

async function buy() {
    let gen_type = event.target.id;

    if (gen_type === "cursor-max") {
        while(cookies >= cursor_cost) {
            cookies_per_second += CURSOR_AMOUNT;
            cookies -= cursor_cost;
            cursors++;
            cursor_cost = cursor_cost * 1.01
            round_prices()
            document.getElementById("cursor-count").innerHTML = "Amount: " + cursors.toString();
            document.getElementById("cursor-cost").innerHTML = "Cost: " + cursor_cost.toString();
        }
    } else if (gen_type === "grandma-max") {
        while (cookies >= grandma_cost) {
            cookies_per_second += GRANDMA_AMOUNT;
            cookies -= grandma_cost;
            grandmas++;
            grandma_cost = grandma_cost * 1.01
            round_prices()
            document.getElementById("grandma-count").innerHTML = "Amount: " + grandmas.toString();
            document.getElementById("grandma-cost").innerHTML = "Cost: " + grandma_cost.toString();
        }
    } else if (gen_type === "factory-max") {
        while (cookies >= factory_cost) {
            cookies_per_second += FACTORY_AMOUNT;
            cookies -= factory_cost;
            factories++;
            factory_cost = factory_cost * 1.001
            round_prices()
            document.getElementById("factory-count").innerHTML = "Amount: " + factories.toString();
            document.getElementById("factory-cost").innerHTML = "Cost: " + factory_cost.toString();
        }
    } else if (gen_type === "network-max") {
        while (cookies >= network_cost) {
            cookies_per_second += NETWORK_AMOUNT;
            cookies -= network_cost;
            networks++;
            network_cost = network_cost * 1.0008
            round_prices()
            document.getElementById("network-count").innerHTML = "Amount: " + networks.toString();
            document.getElementById("network-cost").innerHTML = "Cost: " + network_cost.toString();
        }
    } else if (gen_type === "cookiestash-max") {
        while (cookies >= cookie_stash_cost) {
            cookies_per_second += COOKIE_STASH_AMOUNT;
            cookies -= cookie_stash_cost;
            cookie_stashes++;
            cookie_stash_cost = cookie_stash_cost * 1.0006
            round_prices()
            document.getElementById("cookiestash-count").innerHTML = "Amount: " + cookie_stashes.toString();
            document.getElementById("cookiestash-cost").innerHTML = "Cost: " + cookie_stash_cost.toString();
        }
    } else if (gen_type === "cookiedupe-max") {
        while (cookies >= cookie_duplicator_cost) {
            cookies_per_second += COOKIE_DUPLICATOR_AMOUNT;
            cookies -= cookie_duplicator_cost;
            cookie_duplicators++;
            cookie_duplicator_cost = cookie_duplicator_cost * 1.0003
            round_prices()
            document.getElementById("cookiedupe-count").innerHTML = "Amount: " + cookie_duplicators.toString();
            document.getElementById("cookiedupe-cost").innerHTML = "Cost: " + cookie_duplicator_cost.toString();
        }
    } else if (gen_type === "timemachine-max") {
        while (cookies >= time_machine_cost) {
            cookies_per_second += TIME_MACHINE_AMOUNT;
            cookies -= time_machine_cost;
            time_machines++;
            time_machine_cost = time_machine_cost * 1.0001
            round_prices()
            document.getElementById("timemachine-count").innerHTML = "Amount: " + time_machines.toString();
            document.getElementById("timemachine-cost").innerHTML = "Cost: " + time_machine_cost.toString();
        }
    } else if (gen_type === "cookieguy-max") {
        while (cookies >= cookie_guy_cost) {
            cookies_per_second += COOKIE_GUY_AMOUNT;
            cookies -= cookie_guy_cost;
            cookie_guys++;
            cookie_guy_cost = cookie_guy_cost * 1.00005
            round_prices()
            document.getElementById("cookieguy-count").innerHTML = "Amount: " + cookie_guys.toString();
            document.getElementById("cookieguy-cost").innerHTML = "Cost: " + cookie_guy_cost.toString();
        }
    } else if (gen_type === "timemachinefactory-max") {
        while (cookies >= time_machine_factory_cost) {
            cookies_per_second += TIME_MACHINE_FACTORY_AMOUNT;
            cookies -= time_machine_factory_cost;
            time_machine_factories++;
            time_machine_factory_cost = time_machine_factory_cost * 1.0001
            round_prices()
            document.getElementById("timemachinefactory-count").innerHTML = "Amount: " + time_machine_factories.toString();
            document.getElementById("timemachinefactory-cost").innerHTML = "Cost: " + time_machine_factory_cost.toString();
        }
    } else {
        alert("Error while trying to process shop purchase: " + gen_type.toString());
    }
}

function buy_max() {
    buy().then(r => document.getElementById("cookies-per-second").innerHTML = "Per second: " + cookies_per_second.toString());
    round_prices()
}

function cheat_detection() {
    let accurate_cookies_per_second =
        (CURSOR_AMOUNT * cursors) +
        (GRANDMA_AMOUNT * grandmas) +
        (FACTORY_AMOUNT * factories) +
        (NETWORK_AMOUNT * networks) +
        (COOKIE_STASH_AMOUNT * cookie_stashes) +
        (COOKIE_DUPLICATOR_AMOUNT * cookie_duplicators) +
        (TIME_MACHINE_AMOUNT * time_machines) +
        (COOKIE_GUY_AMOUNT * cookie_guys) +
        (TIME_MACHINE_FACTORY_AMOUNT * time_machine_factories)
    if (accurate_cookies_per_second < cookies_per_second) {
        window.location.replace("cheat.html");
    }
}

 function check_win() {
    if (cookies >= cookies_required_to_win) {
        window.location.replace("winscreen.html");
    }

    cookies_to_win = cookies_required_to_win - cookies
    if (cookies_to_win >= 999000000000000000000000) {
        string_formatted = (Math.round((cookies_to_win * 100) / 1000000000000000000000000) / 100).toString() + "SEPT";
    } else if (cookies_to_win >= 999000000000000000000) {
        string_formatted = (Math.round((cookies_to_win * 100) / 1000000000000000000000) / 100).toString() + "SEXT";
    } else if (cookies_to_win >= 999000000000000000) {
        string_formatted = (Math.round((cookies_to_win * 100) / 1000000000000000000) / 100).toString() + "QUINT";
    } else if (cookies_to_win >= 999000000000000) {
        string_formatted = (Math.round((cookies_to_win * 100) / 1000000000000000) / 100).toString() + "QUAD";
    } else if (cookies_to_win >= 999000000000) {
        string_formatted = (Math.round((cookies_to_win * 100) / 1000000000000) / 100).toString() + "T";
    } else if (cookies_to_win >= 999000000) {
        string_formatted = (Math.round((cookies_to_win * 100) / 1000000000) / 100).toString() + "B";
    } else if (cookies_to_win >= 999000) {
        string_formatted = (Math.round((cookies_to_win * 100) / 1000000) / 100).toString() + "M";
    } else if (cookies_to_win >= 1000) {
        string_formatted = (Math.round((cookies_to_win * 100) / 1000) / 100).toString() + "K";
    } else {
        string_formatted = Math.round(cookies_to_win.toString());
    }

    document.getElementById("cookies-until-win").innerHTML = "You win in " + string_formatted +
        " cookies (" + (Math.round(((cookies / cookies_to_win) * 1000) / 10)).toString() + "%)";
 }

function test_for_upgrade() {
    if (prestige_level >= 3) {
        document.getElementById("upgrades-wrapper").style.display = "none";
        document.getElementById("upgrade-unlocked-wrapper").style.display = "block";
    } else {
        document.getElementById("upgrades-wrapper").style.display = "block";
        document.getElementById("upgrade-unlocked-wrapper").style.display = "none";
    }
}

function upgrade() {
    if (event.target.id === "upgrade-cookie") {
        if (cookies >= cookies_per_click_upgrade_cost) {
            cookie_upgrade_level++
            cookies -= cookies_per_click_upgrade_cost
            cookies_per_click += cookies_upgrade_add_value
            cookies_upgrade_add_value = cookies_upgrade_add_value * 5
            cookies_per_click_upgrade_cost = cookies_per_click_upgrade_cost * 8
            document.getElementById("upgrade-cookie").innerHTML = "Upgrade for $" + cookies_per_click_upgrade_cost.toString();
            document.getElementById("purchase-failed").style.display = "none";
            document.getElementById("cookie-upgrade-level").innerHTML = "Cookie upgrade level: " + cookie_upgrade_level.toString() + " Per Click: " + cookies_per_click.toString();
        } else {
            document.getElementById("purchase-failed").style.display = "block";
        }
    } else if (event.target.id === "upgrade-cost-reduce") {
        if (cookies >= decrease_cost) {
            if (cursor_cost > 10 && grandma_cost > 50 && factory_cost > 250) {
                if (network_cost > 1000 && cookie_stash_cost > 5000 && cookie_duplicator_cost > 15000) {
                    if (time_machine_cost > 150000 && cookie_guy_cost > 500000 && time_machine_factory_cost > 2500000) {
                        cursor_cost = cursor_cost * decrease_amount
                        grandma_cost = grandma_cost * decrease_amount
                        factory_cost = factory_cost * decrease_amount
                        network_cost = network_cost * decrease_amount
                        cookie_stash_cost = cookie_stash_cost * decrease_amount
                        cookie_duplicator_cost = cookie_duplicator_cost * decrease_amount
                        time_machine_cost = time_machine_cost * decrease_amount
                        cookie_guy_cost = cookie_guy_cost * decrease_amount
                        time_machine_factory_cost = time_machine_factory_cost * decrease_amount

                        decrease_cost = decrease_cost * 5

                        round_prices()

                        document.getElementById("upgrade-cost-reduce").innerHTML = "Purchase for $" + decrease_cost.toString();
                        document.getElementById("purchase-failed").style.display = "none";
                    }
                }
            }

            document.getElementById("cursor-cost").innerHTML = "Cost: " + cursor_cost.toString();
            document.getElementById("grandma-cost").innerHTML = "Cost: " + grandma_cost.toString();
            document.getElementById("factory-cost").innerHTML = "Cost: " + factory_cost.toString();
            document.getElementById("network-cost").innerHTML = "Cost: " + network_cost.toString();
            document.getElementById("cookiestash-cost").innerHTML = "Cost: " + cookie_stash_cost.toString();
            document.getElementById("cookiedupe-cost").innerHTML = "Cost: " + cookie_duplicator_cost.toString();
            document.getElementById("timemachine-cost").innerHTML = "Cost: " + time_machine_cost.toString();
            document.getElementById("cookieguy-cost").innerHTML = "Cost: " + cookie_guy_cost.toString();
            document.getElementById("timemachinefactory-cost").innerHTML = "Cost: " + time_machine_factory_cost.toString();
        } else {
            document.getElementById("purchase-failed").style.display = "block";
        }
    } else if (event.target.id === "upgrade-reduce") {
        if (cookies >= upgrade_reduce_cost) {
            if (cookies_per_click_upgrade_cost >= 1000 && decrease_cost >= 5000) {
                cookies_per_click_upgrade_cost = cookies_per_click_upgrade_cost * upgrade_reduce_amount
                decrease_cost = decrease_cost * upgrade_reduce_amount

                cookies_per_click_upgrade_cost = Math.round(cookies_per_click_upgrade_cost)
                decrease_cost = Math.round(decrease_cost)

                upgrade_reduce_cost = upgrade_reduce_cost * 5

                document.getElementById("upgrade-reduce").innerHTML = "Purchase for $" + upgrade_reduce_cost.toString();
                document.getElementById("upgrade-cost-reduce").innerHTML = "Purchase for $" + decrease_cost.toString();
                document.getElementById("upgrade-cookie").innerHTML = "Upgrade for $" + cookies_per_click_upgrade_cost.toString();

                document.getElementById("purchase-failed").style.display = "none";
            }
        } else {
            document.getElementById("purchase-failed").style.display = "block";
        }
    } else {
        alert("failed to process upgrade purchase: " + event.target.id)
    }
}

function add_cookies() {
    cookies += cookies_per_second
    display_cookie_with_prefix()
}

function validate_items() {
    cursor_cost = Math.round(cursor_cost * 10) / 10
    grandma_cost = Math.round(grandma_cost * 10) / 10
    factory_cost = Math.round(factory_cost * 10) / 10
    network_cost = Math.round(network_cost * 10) / 10
    cookie_stash_cost = Math.round(cookie_stash_cost * 10) / 10
    cookie_duplicator_cost = Math.round(cookie_duplicator_cost * 10) / 10
    time_machine_cost = Math.round(time_machine_cost * 10) / 10
    cookie_guy_cost = Math.round(cookie_guy_cost * 10) / 10
    time_machine_factory_cost = Math.round(time_machine_factory_cost * 10) / 10

    cookies_until_prestige = prestige_cost - cookies;

    if (cookies >= cursor_cost) {
        document.getElementById("cursor-cost").style.color = "black";
    } else {
        document.getElementById("cursor-cost").style.color = "red";
    }

    if (cookies >= grandma_cost) {
        document.getElementById("grandma-cost").style.color = "black";
    } else {
        document.getElementById("grandma-cost").style.color = "red";
    }

    if (cookies >= factory_cost) {
        document.getElementById("factory-cost").style.color = "black";
    } else {
        document.getElementById("factory-cost").style.color = "red";
    }

    if (cookies >= network_cost) {
        document.getElementById("network-cost").style.color = "black";
    } else {
        document.getElementById("network-cost").style.color = "red";
    }

    if (cookies >= cookie_stash_cost) {
        document.getElementById("cookiestash-cost").style.color = "black";
    } else {
        document.getElementById("cookiestash-cost").style.color = "red";
    }

    if (cookies >= cookie_duplicator_cost) {
        document.getElementById("cookiedupe-cost").style.color = "black";
    } else {
        document.getElementById("cookiedupe-cost").style.color = "red";
    }

    if (cookies >= time_machine_cost) {
        document.getElementById("timemachine-cost").style.color = "black";
    } else {
        document.getElementById("timemachine-cost").style.color = "red";
    }

    if (cookies >= cookie_guy_cost) {
        document.getElementById("cookieguy-cost").style.color = "black";
    } else {
        document.getElementById("cookieguy-cost").style.color = "red";
    }

    if (cookies >= time_machine_factory_cost) {
        document.getElementById("timemachinefactory-cost").style.color = "black";
    } else {
        document.getElementById("timemachinefactory-cost").style.color = "red"
    }

    if (cookies_until_prestige <= 0 && !prestige_button) {
        prestige_button = true
    }

    if (cookies >= prestige_cost && prestige_button) {
        document.getElementById("prestige-wrapper").style.display = "inline";
        prestige_button = false
    } else {
        document.getElementById("prestige-wrapper").style.display = "none";
    }

    if (cookies < prestige_cost) {
        if (cookies_until_prestige >= 999000000000000000000000) {
            document.getElementById("cookies-until-prestige").innerHTML = "Next prestige in " + (Math.round((cookies_until_prestige * 100) / 1000000000000000000000000) / 100).toString() + "SEPT cookies";
        } else if (cookies_until_prestige >= 999000000000000000000) {
            document.getElementById("cookies-until-prestige").innerHTML = "Next prestige in " + (Math.round((cookies_until_prestige * 100) / 1000000000000000000000) / 100).toString() + "SEXT cookies";
        } else if (cookies_until_prestige >= 999000000000000000) {
            document.getElementById("cookies-until-prestige").innerHTML = "Next prestige in " + (Math.round((cookies_until_prestige * 100) / 1000000000000000000) / 100).toString() + "QUINT cookies";
        } else if (cookies_until_prestige >= 999000000000000) {
            document.getElementById("cookies-until-prestige").innerHTML = "Next prestige in " + (Math.round((cookies_until_prestige * 100) / 1000000000000000) / 100).toString() + "QUAD cookies";    
        } else if (cookies_until_prestige >= 999000000000) {
            document.getElementById("cookies-until-prestige").innerHTML = "Next prestige in "
                + (Math.round((cookies_until_prestige * 10) / 1000000000000) / 10).toString() + "T cookies";
        } else if (cookies_until_prestige >= 999000000) {
            document.getElementById("cookies-until-prestige").innerHTML = "Next prestige in "
                + (Math.round((cookies_until_prestige * 10) / 1000000000) / 10).toString() + "B cookies";
        } else if (cookies_until_prestige >= 999000) {
            document.getElementById("cookies-until-prestige").innerHTML = "Next prestige in "
                + (Math.round((cookies_until_prestige * 10) / 1000000) / 10).toString() + "M cookies";
        } else if (cookies_until_prestige >= 1000) {
            document.getElementById("cookies-until-prestige").innerHTML = "Next prestige in "
                + (Math.round((cookies_until_prestige * 10) / 1000) / 10).toString() + "K cookies";
        } else {
            document.getElementById("cookies-until-prestige").innerHTML = "Next prestige in "
                + Math.round(cookies_until_prestige).toString() + " cookies";
        }

        document.getElementById("cookies-until-prestige").style.color = "black";
    
    } else {
        document.getElementById("cookies-until-prestige").innerHTML = "You can prestige now!";
        document.getElementById("cookies-until-prestige").style.color = "green";
    }

    if (cookies_per_click >= 1000) {
        document.getElementById("cookie").src = "assets/cookie-chip.png";
    }
}

function prestige() {
    document.getElementById("prestige-paragraph").innerHTML = "You have reached " + prestige_cost +
        " cookies<br>you can prestige for " + prestige_cost + " to get double cookies"
    prestige_level++;

    alert("Congratulatons, you have prestiged! You are now prestige " + prestige_level.toString())

    cookies -= prestige_cost;
    prestige_cost = prestige_cost * 10;
    prestige_button = false;

    CURSOR_AMOUNT = CURSOR_AMOUNT * 2
    GRANDMA_AMOUNT = GRANDMA_AMOUNT * 2
    FACTORY_AMOUNT = FACTORY_AMOUNT * 2
    NETWORK_AMOUNT = NETWORK_AMOUNT * 2
    COOKIE_STASH_AMOUNT = COOKIE_STASH_AMOUNT * 2
    COOKIE_DUPLICATOR_AMOUNT = COOKIE_DUPLICATOR_AMOUNT * 2
    COOKIE_GUY_AMOUNT = COOKIE_GUY_AMOUNT * 2
    TIME_MACHINE_FACTORY_AMOUNT = TIME_MACHINE_FACTORY_AMOUNT * 2

    document.getElementById("prestige-paragraph").innerHTML = "You have reached " + prestige_cost +
" cookies<br>you can prestige for " + prestige_cost + " to get double cookies"
}
