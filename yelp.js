

function load(term) {
    fetch('http://127.0.0.1:5000/yelp-test?term=' + term).then(res => res.json()).then(response => {
        console.log(response);
        let businesses = response.businesses;

        for(let i = 0; i < businesses.length; i++){
            document.getElementById('display').innerHTML += `
                <div class="card" style="width: 40rem; font-family: "PT Serif Caption";">
                    <h5 class="card-title"><b>${businesses[i].name}</b></h5>
                    <img height="150px" width="150px" src=${businesses[i].image_url}>
                    <div>Rating: ${businesses[i].rating}/5</div>
                    <div>Reviews: ${businesses[i].review_count}</div>
                    <div>Address: ${businesses[i].location.display_address}</div>
                    <div>Phone: ${businesses[i].display_phone}</div>
                </div>
                
            `;
        }

    })
}
