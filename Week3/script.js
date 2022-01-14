let list_site = [];
let list_img = [];

function getdata() {
    let src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json";
    fetch(src)
        .then(function (response) {
            return response.json();
        })
        .then(function (result) {
            let data = result.result.results;
            let site = "";
            for (let i in data) {
                let site = data[i].stitle;
                list_site.push(site);
            }
            for (let i in data) {
                let photo = "https" + data[i].file.split("https")[1];
                list_img.push(photo);
            }

            // 取得外層容器 myList
            let ul = document.getElementById('content');
            // 建立一個 DocumentFragment，可以把它看作一個「虛擬的容器」
            let fragment = document.createDocumentFragment();
            for (let i = 0; i < 8; i++) {
                // 生成新的，加入文字後置入 fragment 中。
                let newDiv = document.createElement('div');
                let text = document.createElement('div');
                let newImg = new Image()
                newDiv.className = 'site'
                text.className = 'word'
                text.textContent = list_site[i]
                newImg.src = list_img[i]
                newDiv.append(newImg, text)
                fragment.appendChild(newDiv)
            }
            ul.appendChild(fragment)
        });
}
let n = 8;

function load() {
    let ul = document.getElementById('content');
    let fragment = document.createDocumentFragment();
    if (n < list_site.length) {
        for (let i = n; i < n + 8; i++) {
            let newDiv = document.createElement('div');
            let text = document.createElement('div');
            let newImg = new Image()
            newDiv.className = 'site'
            text.className = 'word'
            text.textContent = list_site[i]
            newImg.src = list_img[i]
            newDiv.append(newImg, text)
            fragment.appendChild(newDiv)
            if (i > list_site.length) {
                return;
            }
        }
        ul.appendChild(fragment)
        n = n + 8;
    } else {
        console.log("no data")
        return;
    }
}
getdata();