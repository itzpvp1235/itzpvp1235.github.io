const searchbar = document.getElementById("search")
const items = document.getElementsByClassName("list-item")
const search_form = document.getElementById("search-form")
const modal = document.getElementById("myModal");
const span = document.getElementsByClassName("close")[0];
const search_table = document.getElementById("search-result-table")
const search_header = document.getElementById("search-header")

search_form.addEventListener("submit", e => {
    e.preventDefault()

    search_header.innerHTML = "Searching..."

    search_table.style.display = "block"

    const search_query = searchbar.value
    search_table.innerHTML = "<tr>\n" +
        "                        <th>Project</th>\n" +
        "                        <th>Type</th>\n" +
        "                        <th>Date created</th>\n" +
        "                        <th>Version, Last updated</th>\n" +
        "                        <th>Discontinued?</th>\n" +
        "                        <th class='items-desc'>Description</th>\n" +
        "                    </tr>"

    let matches = 0
    let already_on_list = []

    // the search
    Array.prototype.forEach.call(items, item => {
        console.log(item.parentElement.parentElement.children[5].innerHTML.toUpperCase())
        if (item.innerHTML.toUpperCase().includes(search_query.toUpperCase())) {
            already_on_list.push(item)
            const clone = item.parentElement.parentElement.cloneNode(true)
            clone.children[0].children[0].classList.remove("list-item")
            search_table.appendChild(clone)

            matches++
        }
    });

    Array.prototype.forEach.call(items, item => {
        console.log(item.parentElement.parentElement.children[5].innerHTML.toUpperCase())
        if (item.parentElement.parentElement.children[5].innerHTML.toUpperCase().includes(search_query.toUpperCase())) {
            if (!(already_on_list.includes(item))) {
                const clone = item.parentElement.parentElement.cloneNode(true)
                clone.children[0].children[0].classList.remove("list-item")
                search_table.appendChild(clone)

                matches++
            }
        }
    });


    search_header.innerHTML = "Search Results (" +  matches + " Results)"

    if (matches === 0) {
        search_table.style.display = "none"
        search_header.innerHTML = "No results were found"
    }
})

var item_names = []
Array.prototype.forEach.call(items, item => {
    item_names.push(item.innerHTML)
});
console.log(item_names)

function autocomplete(inp, arr) {
    /*the autocomplete function takes two arguments,
    the text field element and an array of possible autocompleted values:*/
    var currentFocus;
    /*execute a function when someone writes in the text field:*/
    inp.addEventListener("input", function(e) {
        var a, b, i, val = this.value;
        /*close any already open lists of autocompleted values*/
        closeAllLists();
        if (!val) { return false;}
        currentFocus = -1;
        /*create a DIV element that will contain the items (values):*/
        a = document.createElement("DIV");
        a.setAttribute("id", this.id + "autocomplete-list");
        a.setAttribute("class", "autocomplete-items");
        /*append the DIV element as a child of the autocomplete container:*/
        this.parentNode.appendChild(a);
        /*for each item in the array...*/
        for (i = 0; i < arr.length; i++) {
            /*check if the item starts with the same letters as the text field value:*/
            if (arr[i].substr(0, val.length).toUpperCase() === val.toUpperCase()) {
                /*create a DIV element for each matching element:*/
                b = document.createElement("DIV");
                /*make the matching letters bold:*/
                b.innerHTML = "<strong>" + arr[i].substr(0, val.length) + "</strong>";
                b.innerHTML += arr[i].substr(val.length);
                /*insert a input field that will hold the current array item's value:*/
                b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
                /*execute a function when someone clicks on the item value (DIV element):*/
                b.addEventListener("click", function(e) {
                    /*insert the value for the autocomplete text field:*/
                    inp.value = this.getElementsByTagName("input")[0].value;
                    /*close the list of autocompleted values,
                    (or any other open lists of autocompleted values:*/
                    closeAllLists();
                });
                a.appendChild(b);
            }
        }
    });
    /*execute a function presses a key on the keyboard:*/
    inp.addEventListener("keydown", function(e) {
        var x = document.getElementById(this.id + "autocomplete-list");
        if (x) x = x.getElementsByTagName("div");
        if (e.keyCode == 40) {
            /*If the arrow DOWN key is pressed,
            increase the currentFocus variable:*/
            currentFocus++;
            /*and and make the current item more visible:*/
            addActive(x);
        } else if (e.keyCode == 38) { //up
            /*If the arrow UP key is pressed,
            decrease the currentFocus variable:*/
            currentFocus--;
            /*and and make the current item more visible:*/
            addActive(x);
        } else if (e.keyCode == 13) {
            /*If the ENTER key is pressed, prevent the form from being submitted,*/
            e.preventDefault();
            if (currentFocus > -1) {
                /*and simulate a click on the "active" item:*/
                if (x) x[currentFocus].click();
            }
        }
    });
    function addActive(x) {
        /*a function to classify an item as "active":*/
        if (!x) return false;
        /*start by removing the "active" class on all items:*/
        removeActive(x);
        if (currentFocus >= x.length) currentFocus = 0;
        if (currentFocus < 0) currentFocus = (x.length - 1);
        /*add class "autocomplete-active":*/
        x[currentFocus].classList.add("autocomplete-active");
    }
    function removeActive(x) {
        /*a function to remove the "active" class from all autocomplete items:*/
        for (var i = 0; i < x.length; i++) {
            x[i].classList.remove("autocomplete-active");
        }
    }
    function closeAllLists(elmnt) {
        /*close all autocomplete lists in the document,
        except the one passed as an argument:*/
        var x = document.getElementsByClassName("autocomplete-items");
        for (var i = 0; i < x.length; i++) {
            if (elmnt != x[i] && elmnt != inp) {
                x[i].parentNode.removeChild(x[i]);
            }
        }
    }
    /*execute a function when someone clicks in the document:*/
    document.addEventListener("click", function (e) {
        closeAllLists(e.target);
    });
}

/*An array containing all the country names in the world:*/
/*initiate the autocomplete function on the "myInput" element, and pass along the countries array as possible autocomplete values:*/
autocomplete(document.getElementById("search"), item_names);

// When the user clicks on the button, open the modal
document.getElementById("submit-button-search").onclick = function() {
    modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}