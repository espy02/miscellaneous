// I created this script to bypass pixiv's referrer pages. Later, I found out that someone had created a much better script that would also bypass those pages.
// In other words, this script is useless, however I'm leaving it here for archival purposes, also because this was my first ever script.

// ==UserScript==
// @name         pixiv Referrer Bypass
// @namespace    https://github.com/espy02
// @version      1.0
// @description  Bypass pixiv's referrer pages
// @author       espy
// @match        https://www.pixiv.net/jump.php*
// @icon         https://www.pixiv.net/favicon.ico/
// @grant        none
// ==/UserScript==

(function() {
    let new_url = "";
    let dont_append = 3;
    for (let i = 31; i < location.href.length; i++) {
        if (dont_append == 3) {
            if (location.href.substring(i, i + 3) == "%3A") { // substitute substring with a colon, and prevent next two character from being appended
                new_url += ":";
                dont_append = 1;
            } else if (location.href.substring(i, i + 3) == "%2F") { // substitute substring with a slash, and prevent next two character from being appended
                new_url += "/";
                dont_append = 1;
            } else {
                new_url += location.href.substring(i, i + 1); // append next character
            }
        } else { // prevents from appending to the href string the next two characters, if dont_append < 3
            dont_append++;
        }
    }
    location.href = new_url; // opens the correct link
})();
