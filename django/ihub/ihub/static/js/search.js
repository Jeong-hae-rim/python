
var showSearchDetail = document.querySelector('#userSearch');
console.log(showSearchDetail);

showSearchDetail.addEventListener('click', function(event){
    document.querySelector('.modal-title').innerHTML = 'API 명을 정확히 입력해주세요'
    document.querySelector('.modal-body-div').innerHTML = ''

    let searchString = document.querySelector('#myInput');
    console.log(searchString);
    axios.get(`/apis/search/${searchString.value}/`)
    .then(res => {
        console.log(res.data.api_pk);
        let targetId = res.data.api_pk;
        axios.get(`/apis/${targetId}/detail/`)
        .then(res => {
            console.log(res.data)
            document.querySelector('.modal-body-div').innerHTML =''
            document.querySelector('#chartdiv').innerHTML =''
            document.querySelector('.modal-title').innerHTML = res.data.api_name
            document.querySelector('.modal-body-div').innerHTML = 
            '<div>최종수정일 : ' + res.data.latest_modified_date + '</div>' +
            '<div>저작권자명 : ' + res.data.copyright + '</div>' +
            '<div>라이센스 : ' + res.data.copyright_range + '</div>' +
            '<div>다운로드수 : ' + res.data.download_count + '</div>'
        })
    })


})
