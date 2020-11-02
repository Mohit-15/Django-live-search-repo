
const spinnerBox = document.getElementById("spinner-box")
const mainDiv = document.getElementById("maindiv")

$.ajax ({
	    type: 'GET',
	    url: "/json_data/",
	    success: function(response){
	    	setTimeout(function(){
	    		spinnerBox.classList.add("not-visible")
		    	mainDiv.classList.remove("not-visible")
	    	}, 500)
	},
	    error: function(error){
	    console.log(error)
	}
})