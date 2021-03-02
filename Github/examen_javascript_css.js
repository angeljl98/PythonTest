var obj = new Object();
obj.name = "Raj";
obj.age = 32;
obj.married = false;

//convert object to json string
var string = JSON.stringify(obj);

//convert string to Json Object
console.log(JSON.parse(string)); // this is your requirement.


<script type="text/javascript">
function myFunction () {
    console.log('Executed!');
}

var interval = setInterval(function () { myFunction(); }, 60000);
</script>

var errorObj = new Error(["message"]);
