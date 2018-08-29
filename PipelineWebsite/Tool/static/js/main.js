var IsCustom = false;
var timeoutfunction;

$('.autoplay').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 2000,
    dots: true,
    centerMode: false,
    focusOnSelect: true,
});

function CreateCustom() {
    var i;
    var list = document.getElementsByClassName("Step");
    for (i = 0; i < list.length; i++) {
        list[i].style.width = "22%";
    }
    document.getElementById("Step2Content").style.marginLeft="5%";
    for (i = 1; i < 5; i++) {
        var name = "PB_" + i.toString();
        document.getElementById(name).style.width = "25%";
    }
    IsCustom = true;
    clearTimeout(timeoutfunction);
    timeoutfunction=setTimeout(displaycustom, 2100);
}


function displaycustom(){
    document.getElementById("CustomStep").style.display = "block";
    document.getElementById("PB_4").className = "inactive";
    document.getElementById("PB_3").className = "active";
}

function RemoveCustom() {
    var i;
    var list = document.getElementsByClassName("Step");
    for (i = 0; i < list.length; i++) {
        list[i].style.width = "30%";
    }
    for (i=1;i<5;i++){
        var name = "PB_"+i.toString();
        document.getElementById(name).style.width="33%";
    }
    document.getElementById("Step2Content").style.marginLeft = "20  %";

    document.getElementById("CustomStep").style.display = "none";
    IsCustom = false;
    document.getElementById("PB_3").className = "active";

    document.getElementById("PB_4").className = "hidden";
    clearTimeout(timeoutfunction);
}


function ContinueStep1() {//Check the first name, last name and email's input fields' validity
    if (document.getElementsByName("Email")[0].checkValidity() && document.getElementsByName("FirstName")[0].checkValidity() && document.getElementsByName("LastName")[0].checkValidity()) {
        document.getElementById("PB_1").className = "active";
    }

}

function ContinueStep2() {
    if (document.getElementsByName("TumorFile")[0].checkValidity() && document.getElementsByName("NormalFile")[0].checkValidity() && document.getElementsByName("PanelOfNormals")[0].checkValidity()) {
        document.getElementById("PB_2").className = "active";
    }
}