var IsCustom = false;
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
    document.getElementById("CustomStep").style.display = "block";
    IsCustom = true;
    document.getElementById("PB_4").className = "inactive";
    document.getElementById("PB_3").className = "active";

}

function RemoveCustom() {
    document.getElementById("CustomStep").style.display = "none";
    IsCustom = false;
    document.getElementById("PB_3").className = "active";

    document.getElementById("PB_4").className = "hidden";
}



function ContinueStep1() {//Check the first name, last name and email's input fields' validity
    if (document.getElementsByName("Email")[0].checkValidity() && document.getElementsByName("FirstName")[0].checkValidity() && document.getElementsByName("LastName")[0].checkValidity()) {
        document.getElementById('Step2').scrollIntoView();
        document.getElementById("PB_1").className = "active";
    }

}

function ContinueStep2() {
    if (document.getElementsByName("TumorFile")[0].checkValidity() && document.getElementsByName("NormalFile")[0].checkValidity() && document.getElementsByName("PanelOfNormals")[0].checkValidity()) {
        document.getElementById('Step3').scrollIntoView();
        document.getElementById("PB_2").className = "active";
    }
}