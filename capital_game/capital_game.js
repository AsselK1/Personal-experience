// This allows the Javascript code inside this block to only run when the page
// has finished loading in the browser.
let database;
let map;
$( document ).ready(function() {
  let firebaseConfig = {
    apiKey: "AIzaSyCDI13xDAXI5GhtVzYoSllqgyp81n3EAa4",
    authDomain: "pr-3-17dcf.firebaseapp.com",
    projectId: "pr-3-17dcf",
    storageBucket: "pr-3-17dcf.appspot.com",
    messagingSenderId: "72032162022",
    appId: "1:72032162022:web:ab443cf65d5547ed01ab27",
    measurementId: "G-02MPH1Q03J"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
  database = firebase.database();
    $.ajax({
        url: "country_capital_geo.csv",
        dataType: "text",
        async: false,
        success: function(data) {
            window.pairs=processData(data);
        }
    });

    $.ajax({
        url: "country_capital_geo.csv",
        dataType: "text",
        async: false,
        success: function(data) {
            window.coordinates=processDataCoor(data);
        }
    });
    mapboxgl.accessToken = 'pk.eyJ1IjoiYXNzZWxrMSIsImEiOiJja29rMmU4NnYwMThrMnJxcG9vbmk3bWJsIn0.llYnSylRpufBVIKPv5z0lA';
    $( function() {
        const arr=[];
        for (let i=0;i<pairs.length;i++){
            arr.push(pairs[i].capital);
        }
        $("#pr2__capital").autocomplete({
            source: function (request, response) {
                var inp=request.term;
                var count=0;
                var ret=[]
                for (let i=0; i<arr.length; i++){
                    for(let j=0; j<inp.length; j++){
                        if(j>=arr[i].length){
                            count=0;
                            break;
                        }
                        if (inp[j].toUpperCase()===(arr[i][j].toUpperCase())){
                            count++
                        }
                    }
                    if (count===inp.length){
                        ret.push(arr[i]);
                    }
                    count=0;
                }
                response(ret);
            },
            minLength: 2,
            select: function (event, ui){
                event.preventDefault();
                document.getElementById('pr2__capital').value=ui.item.value;
                add();
            }
        });
    });
    $("#modes").change(function(){
        if (document.getElementById("modes").value==="Right"){
            correct();
        }
        if (document.getElementById("modes").value==="Wrong"){
            wrong();
        }
        if (document.getElementById("modes").value==="All"){
            all();
        }
    });
    show();




});
function processData(allText) {
    let allTextLines = allText.split(/\r\n|\n/);
    let headers = allTextLines[0].split(',');
    let lines = [];

    for (let i=1; i<allTextLines.length; i++) {
        let data = allTextLines[i].split(',');
        if (data.length === headers.length) {

            let tarr = {};
            for (let j=0; j<headers.length-2; j++) {
                tarr[headers[j]]=data[j];
                //tarr.push(headers[j]+":"+data[j]);
            }
            lines.push(tarr);
        }
    }
    return lines
}
function processDataCoor(allTextt) {
    let allTexttLines = allTextt.split(/\r\n|\n/);
    let headers = allTexttLines[0].split(',');
    let lines = [];

    for (let i=1; i<allTexttLines.length; i++) {
        let data = allTexttLines[i].split(',');
        if (data.length === headers.length) {

            let tarr = {};
            let j=0;
            tarr[headers[j]]=data[j];
            tarr["coordinates"]=[data[j+2], data[j+3]];
            //for (let j=0; j<headers.length-2; j++) {
              //  tarr[headers[j]]=data[j];
                //tarr.push(headers[j]+":"+data[j]);
            //}
            lines.push(tarr);
        }
    }
    return lines
}
$("modes").change(function(){
  alert("The text has been changed.");
});

function correct(){
    let a = document.getElementById("mytable");
    let rights = a.childNodes;
    let count1=0;
    for(let i=0; i<rights.length;i++) {
        if (rights[i]) {
            if (rights[i].className === "wrong") {
                rights[i].style.display = "none";
            }
            if (rights[i].className === "right") {
                rights[i].style.display = "table-row";
                count1++;
            }
        }
    }
    let x = document.createElement("tr");
    x.id="empty_list";
    x.innerHTML="\n" +
        "          <td></td>\n" +
        "          <td>\n" +
        "            <p style=\"text-align: center\">The list is empty</p>\n" +
        "          </td>\n" +
        "          <td></td>\n" +
        "        ";
    if(count1 === 0 && !document.getElementById('empty_list')){
        let elem = document.getElementById("mytable");
        elem.appendChild(x);
    }
    else if (!!document.getElementById('empty_list')){
        document.getElementById("empty_list").visibility="hidden";
    }
}
function empty(){
    let actions = database.ref("actions");
    let entries = database.ref("entries");

    let newAction = actions.push().key;
    const query = database.ref('entries').orderByChild('id');

    database.ref('actions/'+newAction+'/action').set('clear');
    query.once('value').then(function(snapshot) {
        snapshot.forEach(function(childNodes){
            database.ref('actions/'+newAction+'/data').push(childNodes.val());
        })
    })
    entries.once('value').then(function(snapshot) {
        snapshot.forEach(function(childNodes){
            database.ref('entries/'+childNodes.key).remove();
        })
    })
    entries.once('value', function(snapshot){
        if(snapshot.numChildren() === 0){
            alert('no items to clear');
            database.ref('actions/'+newAction).remove();
            return false;
        }
    })
    setTimeout(show, 1000);
}

function show() {
    let question = 0;
    let country_capital_pairs = window.pairs;
    if(document.getElementById("correct").question === undefined){
       question = Math.floor(Math.random() * (country_capital_pairs.length));
    }
    else question=document.getElementById("correct").question;
    document.getElementById("mytable").innerHTML= `<tr style="border-bottom: 2px solid black;">
    <th>COUNTRY</th>
    <th>CAPITAL CITY</th>
    <th>ANSWER</th>
</tr>
<tr>
    <td>
        <div id='pr2__country'></div>
    </td>
    <td className="container">
        <input type="text" id="pr2__capital" name="capital" value="" autoFocus list="options">
            <datalist id="options"></datalist>
            <input type="hidden" id="correct" value1="" value2="" coord_x="" coord_y="">
            <label className="suggestions" id="suggestions" style="z-index: 100; font-weight: normal"></label>
    </td>
    <td>
        <button type="button" id="pr2__button" onClick="add()">Check answer</button>
    </td>
</tr>`;
    if (!!document.getElementById("empty_list")){
        entries.on('value', function(snapshot){
        if(snapshot.numChildren() === 0){
            document.getElementById("empty_list").visibility="visible";
        }
        else{
            document.getElementById("empty_list").visibility="hidden";
        }
    })
    }
    document.getElementById("correct").question=question;
    document.getElementById('pr2__country').innerHTML = country_capital_pairs[question].country;
    document.getElementById("correct").value1=country_capital_pairs[question].capital;
    document.getElementById("correct").value2=country_capital_pairs[question].country;
    document.getElementById("correct").coord_x=window.coordinates[question].coordinates[0];
    document.getElementById("correct").coord_y=window.coordinates[question].coordinates[1];
    document.getElementById('pr2__country').coord_x=window.coordinates[question].coordinates[0];
    document.getElementById('pr2__country').coord_y=window.coordinates[question].coordinates[1];
    document.getElementById("pr2__capital").focus();
    document.getElementById('pr2__country').addEventListener("mouseover", country1);
    document.getElementById('pr2__country').addEventListener("mouseout", nohover1);
    map = new mapboxgl.Map({
        container: 'map', // container ID
        style: 'mapbox://styles/mapbox/satellite-streets-v11', // style URL
        center: [document.getElementById("correct").coord_x, document.getElementById("correct").coord_y], // starting position [lng, lat]
        zoom: 4 // starting zoom
        });
    const suggestionsPanel = document.querySelector('#suggestions');
    suggestionsPanel.innerHTML = '';
    mapboxgl.accessToken = 'pk.eyJ1IjoiYXNzZWxrMSIsImEiOiJja29rMmU4NnYwMThrMnJxcG9vbmk3bWJsIn0.llYnSylRpufBVIKPv5z0lA';
    map.setCenter([document.getElementById("correct").coord_x, document.getElementById("correct").coord_y]);
    map.setZoom(4);
    map.setStyle("mapbox://styles/mapbox/satellite-streets-v11");
    document.getElementById('pr2__capital').addEventListener('keypress', function(e){
        if(e.code === 'Enter'){
            e.preventDefault();
            add();
            return true;
        }
  }, false);

    let entries=database.ref("entries");


    entries.once('value').then(function(snapshot) {
        snapshot.forEach(function(childSnapshot) {
            let childData = childSnapshot.val();
            if (childData.correctness===true){
                let x = document.createElement("tr");
                let a = document.createElement("td");
                let b = document.createElement("td");
                let c = document.createElement("td");
                x.appendChild(a);
                x.appendChild(b);
                x.appendChild(c);
                let corr_country = childData.country;
                let corr_capit = childData.corr_answer;
                let corr_capit1 = childData.corr_answer;
                let uniqid = childData.id;

                let remove = document.createElement("BUTTON");
                remove.innerHTML = "Remove";
                remove.setAttribute("type", "button");
                let data= {
                    country: childData.country,
                    given_answer: childData.given_answer,
                    corr_answer: childData.corr_answer,
                    correctness: true,
                    coord_x: childData.coord_x,
                    coord_y: childData.coord_y,
                    id: childData.id,
                };
                remove.addEventListener("click", function () {
                    let actions = database.ref("actions");
                    actions.push({
                        action: "remove",
                        data: data,
                    });
                    let entries = database.ref("entries");
                    entries.once('value', function (snapshot) {
                        snapshot.forEach(function (childNodes) {

                            if (childNodes.val().id === uniqid) {
                                database.ref("entries" + "/" + childNodes.key).remove();
                            }
                        })
                    })
                    //x.remove();
                    setTimeout(show, 1000);
                });
                a.innerHTML=corr_country;
                b.innerHTML=corr_capit;
                c.innerHTML = corr_capit1;
                c.appendChild(remove);
                x.style.color="green";
                x.className = "right";
                a.className = "countryname";
                c.className = "capitalname";
                a.addEventListener("mouseover", country);
                a.addEventListener("mouseout", nohover);
                c.addEventListener("mouseover", capital);
                c.addEventListener("mouseout", nohover_cap);

                a.x = childData.coord_x;
                a.y = childData.coord_y;
                a.row = x
                c.row = x
                c.x = childData.coord_x;
                c.y = childData.coord_y;
                document.getElementById("mytable").appendChild(x);
                //ref.child(keys[0]).remove();
                //ref.child(keys[0]).remove();
            }
            else if (childData.correctness===false){
                let x = document.createElement("tr");
                let a = document.createElement("td");
                let b = document.createElement("td");
                let c = document.createElement("td");
                x.appendChild(a);
                x.appendChild(b);
                x.appendChild(c);
                let corr_country = childData.country;
                let corr_capit = childData.given_answer;
                let corr_capit1 = childData.corr_answer;
                let uniqid = childData.id;

                let remove = document.createElement("BUTTON");
                remove.innerHTML = "Remove";
                remove.setAttribute("type", "button");
                let data= {
                    country: childData.country,
                    given_answer: childData.given_answer,
                    corr_answer: childData.corr_answer,
                    correctness: false,
                    coord_x: childData.coord_x,
                    coord_y: childData.coord_y,
                    id: childData.id,
                };
                remove.addEventListener("click", function () {
                    let actions = database.ref("actions");
                    actions.push({
                        action: "remove",
                        data: data,
                    });
                    let entries = database.ref("entries");
                    entries.once('value', function (snapshot) {
                        snapshot.forEach(function (childNodes) {

                            if (childNodes.val().id === uniqid) {
                                database.ref("entries" + "/" + childNodes.key).remove();
                            }
                        })
                    })
                    //x.remove();
                    setTimeout(show, 1000);
                });
                a.innerHTML=corr_country;
                b.innerHTML=corr_capit;
                b.style.textDecoration="line-through";
                c.innerHTML = corr_capit1;
                c.appendChild(remove);
                x.style.color = "red";
                x.className = "wrong";
                a.className = "countryname";
                c.className = "capitalname";
                a.addEventListener("mouseover", country);
                a.addEventListener("mouseout", nohover);
                c.addEventListener("mouseover", capital);
                c.addEventListener("mouseout", nohover_cap);

                a.x = childData.coord_x;
                a.y = childData.coord_y;
                a.row = x
                c.row = x
                c.x = childData.coord_x;
                c.y = childData.coord_y;
                document.getElementById("mytable").appendChild(x);
                //ref.child(keys[0]).remove();
            }

        });
    });
    let x = document.createElement("tr");
    x.id="empty_list";
    x.innerHTML="\n" +
        "          <td></td>\n" +
        "          <td>\n" +
        "            <p style=\"text-align: center\">The list is empty</p>\n" +
        "          </td>\n" +
        "          <td></td>\n" +
        "        ";
    entries.on('value', function(snapshot){
        if(snapshot.numChildren() === 0 && !document.getElementById('empty_list')){
            let elem = document.getElementById("mytable");
            elem.appendChild(x);
        }
        else if (!!document.getElementById('empty_list')){
            document.getElementById("empty_list").visibility="hidden";
        }
    })
}
function preset(){
    let actions = database.ref("actions");
    let entries = database.ref("entries");
    entries.once('value', function(snapshot){
        snapshot.forEach(function(childNodes){
            database.ref('entries/'+childNodes.key).remove();
        })
    })
    actions.once('value', function(snapshot){
        snapshot.forEach(function(childNodes){
            database.ref('actions/'+childNodes.key).remove();
        })
    })
    document.getElementById('correct').question = undefined;
    setTimeout(show, 1000);
}
function undo(){
    let actions = database.ref("actions");
    actions.once('value', function(snapshot){
        if(snapshot.numChildren() === 0){
            alert('no actions to undo');
            return true;
        }
    })
    let entries = database.ref("entries");
    database.ref("actions").limitToLast(1).once('value').then(function(snapshot){
        snapshot.forEach(function(childNodes){
            if(childNodes.val().action === "add"){
                entries.on('value', function(snap){
                    snap.forEach(function(child){

                        if(child.val().id === childNodes.val().data.id){
                            database.ref("entries/"+child.key).remove();
                        }
                    })
                })
            }
            else if(childNodes.val().action === "remove"){
                entries.push(childNodes.val().data);
                const query = database.ref('entries').orderByChild('id');
                entries.once('value').then(function(snapshot) {
                    snapshot.forEach(function(childNodes){
                        database.ref('entries/'+childNodes.key).remove();
                    })
                })

                query.once('value').then(function(snapshot) {
                    snapshot.forEach(function(childNodes){
                        database.ref('entries').push(childNodes.val());
                    })
                })

            }
            else if(childNodes.val().action == "clear"){
                database.ref("actions/"+childNodes.key+"/data").once('value',function(snap){
                    snap.forEach(function(child){
                        entries.push(child.val());
                    })
                })
            }
            setTimeout(()=>{database.ref("actions/"+childNodes.key).remove();}, 500);
        })
    })
    setTimeout(show, 1000);
}
function wrong(){
    let a = document.getElementById("mytable");
    let rights = a.childNodes;
    let count1=0;
    for(let i=0; i<rights.length;i++) {
        if (rights[i]) {
            if (rights[i].className === "right") {
                rights[i].style.display = "none";
            }
            if (rights[i].className === "wrong") {
                rights[i].style.display = "table-row";
                count1++;
            }
        }
    }
    let x = document.createElement("tr");
    x.id="empty_list";
    x.innerHTML="\n" +
        "          <td></td>\n" +
        "          <td>\n" +
        "            <p style=\"text-align: center\">The list is empty</p>\n" +
        "          </td>\n" +
        "          <td></td>\n" +
        "        ";
    if(count1 === 0 && !document.getElementById('empty_list')){
        let elem = document.getElementById("mytable");
        elem.appendChild(x);
    }
    else if (!!document.getElementById('empty_list')){
        document.getElementById("empty_list").visibility="hidden";
    }
}
function all(){
    var a = document.getElementById("mytable");
    var rights = a.childNodes;
    var count1=0;
    for(let i=0; i<rights.length;i++) {
        if (rights[i]) {
            if (rights[i].className === "right") {
                rights[i].style.display = "table-row";
                count1++;
            }
            if (rights[i].className === "wrong") {
                rights[i].style.display = "table-row";
                count1++
            }
        }
    }
    let x = document.createElement("tr");
    x.id="empty_list";
    x.innerHTML="\n" +
        "          <td></td>\n" +
        "          <td>\n" +
        "            <p style=\"text-align: center\">The list is empty</p>\n" +
        "          </td>\n" +
        "          <td></td>\n" +
        "        ";
    if(count1 === 0 && !document.getElementById('empty_list')){
        let elem = document.getElementById("mytable");
        elem.appendChild(x);
    }
    else if (!!document.getElementById('empty_list')){
        document.getElementById("empty_list").visibility="hidden";
    }

}

function country() {
    this.row.style.backgroundColor="lightgrey";
    let x=this.x;
    let y=this.y;
    let timer;
    timer = setTimeout(function() {
        map.setCenter([x,y]);
        map.setZoom(4);
        map.setStyle('mapbox://styles/mapbox/satellite-streets-v11');
        /*let map = new mapboxgl.Map({
            container: 'map', // container ID
            style: 'mapbox://styles/mapbox/satellite-streets-v11', // style URL
            center: [x, y], // starting position [lng, lat]
            zoom: 4 // starting zoom
        });*/
        document.getElementById("map").style.border="3px orange solid";
        }, 500)
}
function capital() {
    this.row.style.backgroundColor="lightgrey";
    let x=this.x;
    let y=this.y;
    let timer;
    timer = setTimeout(function() {
        map.setZoom(6);
        map.setCenter([x,y]);
        map.setStyle('mapbox://styles/mapbox/dark-v10');
        /*map = new mapboxgl.Map({
            container: 'map', // container ID
            style: 'mapbox://styles/mapbox/dark-v10', // style URL
            center: [x, y], // starting position [lng, lat]
            zoom: 6 // starting zoom
        });*/
        document.getElementById("map").style.border="3px orange solid";
        }, 500)
}
function nohover() {
    document.getElementById("map").style.border="none";
    this.row.style.backgroundColor="#eee";
}
function nohover_cap() {
    this.row.style.backgroundColor="#eee";
    let x=this.x;
    let y=this.y;
    document.getElementById("map").style.border="none";
    map.setZoom(6);
    map.setCenter([x,y]);
    map.setStyle('mapbox://styles/mapbox/satellite-streets-v11');
    /*map = new mapboxgl.Map({
        container: 'map', // container ID
        style: 'mapbox://styles/mapbox/satellite-streets-v11', // style URL
        center: [x, y], // starting position [lng, lat]
        zoom: 6 // starting zoom
    });*/
}

function country1() {
    let x = this.coord_x;
    let y = this.coord_y;
    let timer;
    timer = setTimeout(function() {
        map.setZoom(4);
        map.setCenter([x,y]);
        map.setStyle('mapbox://styles/mapbox/satellite-streets-v11');
        /*map = new mapboxgl.Map({
            container: 'map', // container ID
            style: 'mapbox://styles/mapbox/satellite-streets-v11', // style URL
            center: [x, y], // starting position [lng, lat]
            zoom: 4 // starting zoom
        });*/
        document.getElementById("map").style.border="3px orange solid";
        }, 500)
}

function nohover1() {
    document.getElementById("map").style.border="none";
}

function checkAnswer(){
    if (document.getElementById("modes").value!=="All"){
        document.getElementById("modes").value="All";
        all();
    }
    if (document.getElementById('pr2__capital').value !=='') {
        if (document.contains(document.getElementById("empty_list"))){
            var elem = document.getElementById("empty_list");
            elem.style.display="none";
        }
        if (document.getElementById('pr2__capital').value.toUpperCase() === document.getElementById("correct").value1.toUpperCase()) {
            let x = document.createElement("tr");
            let a = document.createElement("td");
            let b = document.createElement("td");
            let c = document.createElement("td");
            x.appendChild(a);
            x.appendChild(b);
            x.appendChild(c);
            let corr_country = document.createTextNode(document.getElementById('correct').value2);
            let corr_capit = document.createTextNode(document.getElementById('correct').value1);
            let corr_capit1 = document.createTextNode(document.getElementById('correct').value1);
            let uniqid=Date.now();
            let remove=document.createElement("BUTTON");
            let data={
                country: document.getElementById('correct').value2,
                given_answer:document.getElementById("correct").value1,
                corr_answer:document.getElementById("correct").value1,
                correctness: true,
                id: uniqid,
            }
            let actions = database.ref('actions');
            actions.push({
                action: "add",
                data: data,
            })
            remove.innerHTML="Remove";
            remove.setAttribute("type", "button");
            remove.addEventListener("click", function (){
                let actions = database.ref("actions");
                actions.push({
                    action: "remove",
                    data: data,
                });
                let entries = database.ref("entries");
                entries.once('value', function(snapshot){
                    snapshot.forEach(function(childNodes){

                        if(childNodes.val().id === uniqid){
                            database.ref("entries"+"/"+childNodes.key).remove();
                        }
                    })
                })
                x.remove();
                return false;
            });
            a.appendChild(corr_country);
            b.appendChild(corr_capit);
            c.appendChild(corr_capit1);
            c.appendChild(remove);
            x.style.color="green";
            x.className="right";
            a.className="countryname";
            c.className="capitalname";
            a.addEventListener("mouseover", country);
            a.addEventListener("mouseout", nohover);
            c.addEventListener("mouseover", capital);
            c.addEventListener("mouseout", nohover_cap);

            a.x=document.getElementById("correct").coord_x;
            a.y=document.getElementById("correct").coord_y;
            a.row=x
            c.row=x
            c.x=document.getElementById("correct").coord_x;
            c.y=document.getElementById("correct").coord_y;
            document.getElementById("mytable").appendChild(x);

            let ref = database.ref('entries');
            ref.push(data);
            //ref.child(keys[0]).remove();
        }
        else {
            let x = document.createElement("tr");
            let a = document.createElement("td");
            let b = document.createElement("td");
            let c = document.createElement("td");
            x.appendChild(a);
            x.appendChild(b);
            x.appendChild(c);
            let corr_country = document.createTextNode(document.getElementById('correct').value2);
            let corr_capit = document.createTextNode(document.getElementById('pr2__capital').value);
            let real_capit = document.createTextNode(document.getElementById('correct').value1)
            let remove=document.createElement("BUTTON");
            let uniqid = Date.now();
            document.getElementById('correct').key = uniqid;
            let data= {
                country: document.getElementById('correct').value2,
                given_answer: document.getElementById('pr2__capital').value,
                corr_answer: document.getElementById('correct').value1,
                correctness: false,
                id: uniqid,
            };
            let actions = database.ref('actions');
            actions.push({
                action: "add",
                data: data,
            })
            remove.innerHTML="Remove";
            remove.setAttribute("type", "button");

            remove.addEventListener("click", function (){
                let actions = database.ref("actions");
                actions.push({
                    action: "remove",
                    data: data,
                });
                let entries = database.ref("entries");
                entries.once('value', function(snapshot){
                    snapshot.forEach(function(childNodes){

                        if(childNodes.val().id === uniqid){
                            database.ref("entries"+"/"+childNodes.key).remove();
                        }
                    })
                })
                x.remove();
                return false;
            });
            a.appendChild(corr_country);
            b.appendChild(corr_capit);
            c.appendChild(real_capit);
            c.appendChild(remove)
            b.style.textDecoration="line-through";
            c.style.fontStyle="italic";
            a.className="countryname";
            c.className="capitalname";
            a.addEventListener("mouseover", country);
            a.addEventListener("mouseout", nohover);
            c.addEventListener("mouseover", capital);
            c.addEventListener("mouseout", nohover_cap);
            a.x=document.getElementById("correct").coord_x;
            a.y=document.getElementById("correct").coord_y;
            a.row=x
            c.row=x
            c.x=document.getElementById("correct").coord_x;
            c.y=document.getElementById("correct").coord_y;
            document.getElementById("mytable").appendChild(x);
            x.style.color="red";
            x.className="wrong";
            let ref = database.ref('entries');
            ref.push(data);

        }
        document.getElementById('pr2__capital').value='';
        const suggestionsPanel = document.querySelector('.suggestions');
        suggestionsPanel.innerHTML = '';
        let country_capital_pairs = pairs;
        let question = Math.floor(Math.random() * (country_capital_pairs.length));
        document.getElementById('pr2__country').innerHTML = country_capital_pairs[question].country;
        document.getElementById('pr2__capital').value = '';
        document.getElementById("correct").question=question;
        document.getElementById("correct").value1 = country_capital_pairs[question].capital;
        document.getElementById("correct").value2 = country_capital_pairs[question].country;
        document.getElementById("correct").coord_x=window.coordinates[question].coordinates[0];
        document.getElementById("correct").coord_y=window.coordinates[question].coordinates[1];
        document.getElementById('pr2__country').coord_x=window.coordinates[question].coordinates[0];
        document.getElementById('pr2__country').coord_y=window.coordinates[question].coordinates[1];
        mapboxgl.accessToken = 'pk.eyJ1IjoiYXNzZWxrMSIsImEiOiJja29rMmU4NnYwMThrMnJxcG9vbmk3bWJsIn0.llYnSylRpufBVIKPv5z0lA';
        map.setCenter([document.getElementById("correct").coord_x, document.getElementById("correct").coord_y]);
        map.setZoom(4);
        map.setStyle("mapbox://styles/mapbox/satellite-streets-v11");
        /*map = new mapboxgl.Map({
            container: 'map', // container ID
            style: 'mapbox://styles/mapbox/satellite-streets-v11', // style URL
            center: [document.getElementById("correct").coord_x, document.getElementById("correct").coord_y], // starting position [lng, lat]
            zoom: 4 // starting zoom
        });*/
        document.getElementById('pr2__capital').addEventListener('keypress', function (e) {
            if (e.code == 'Enter') {
                e.preventDefault();
                add();
                return true;
            }
        }, false);
    }
    document.getElementById("pr2__capital").focus();
}

function add(){
    if(document.getElementById("pr2__capital").value !== ''){
        let correctness = false;
        if (document.getElementById('pr2__capital').value.toUpperCase() === document.getElementById("correct").value1.toUpperCase()){
            correctness = true;
        }
        let uniqid = Date.now();
        document.getElementById('correct').key = uniqid;
        let data= {
            country: document.getElementById('correct').value2,
            given_answer: document.getElementById('pr2__capital').value,
            corr_answer: document.getElementById('correct').value1,
            coord_x: document.getElementById('correct').coord_x,
            coord_y: document.getElementById('correct').coord_y,
            correctness: correctness,
            id: uniqid,
        };
        let entries = database.ref('entries');
        entries.push(data);
        let actions = database.ref("actions");
        actions.push({
            action: "add",
            data: data,
        });
        document.getElementById('correct').question = undefined;
    }
    setTimeout(show, 1000);
}
