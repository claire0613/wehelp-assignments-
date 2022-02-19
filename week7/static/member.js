async function searchData() {
    const username = document.querySelector("#inputSearch").value; //==document.getElementsByName('searchUsername')[0//index_num].value
    const searchResult = document.querySelector(".searchResult")
    const url = `http://127.0.0.1:3000/api/members?username=${username}`;
    await fetch(url, {
            method: "GET"
        })
        .then(res => {
             return res.json()
        }).then(result => {
            if (result.data === null || result.data === undefined){
                searchResult.innerText = '查無此會員'
            }else{
                const name = result.data.name;
                const username = result.data.username
                searchResult.innerText = `姓名:${name}(帳號:${username})`
            }
                

        })
        .catch(err => {
            console.log('fetch failed', err)
        });
}


async function updateData() {
    const updatename = document.querySelector("#updatename").value;
    const url = `http://127.0.0.1:3000/api/member`;
    const updateResult = document.querySelector(".updateResult");
    await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                "name": `${updatename}`
            })
        })
        .then(res => {
            return res.json();

        })
        .then(result => {
            const success = result.ok;
            const fail = result.error;
            if (success === true) {
                const title = document.querySelector('.login')
                title.innerText = `${updatename}，歡迎登入系統`
                updateResult.innerText = '更新成功';
            }
            if (fail === true) {

                updateResult.innerText = '會員未登入，更新失敗';
            }
        })
        .catch(err => {
            console.log('fetch failed', err)
        });
}