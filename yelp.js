

function load() {
    fetch('http://127.0.0.1:5000/yelp-test').then(res => res.json()).then(response => {
        console.log(response);
        let businesses = response.businesses;

        for(let i = 0; i < businesses.length; i++){
            document.getElementById('display').innerHTML += `
                <div class="card" style="width: 16rem;">


                    <h5 class="card-title">${businesses[i].name}</h5>
                    <img src=${businesses[i].image_url}>
                    <div>Rating: ${businesses[i].rating}/5</div>
                    <div>Reviews: ${businesses[i].review_count}</div>
                    <div>Address: ${businesses[i].location.display_address}</div>
                    <div>Phone: ${businesses[i].display_phone}</div>

                </div>
                
            `;
        }

    })
}
