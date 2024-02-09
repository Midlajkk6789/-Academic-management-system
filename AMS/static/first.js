function editdepartment(id) {
  //   alert(id);
  document.getElementById('spin'+id).className='fas fa-spinner'

  $.ajax({
    type: "POST",
    url: "http://127.0.0.1:8000/editDepartment/",
    data: {
      eid: id,
    },
    dataType: "json",
    success: function (data) {
      document.getElementById("eidtid").value= data.dataid;
      document.getElementById("deptname").value = data.DepartmentName;
      document.getElementById("deptcode").value = data.DepartmentCode;
      document.getElementById("deptstatus").value = data.status;
      $("#modal-default").modal("show");
      document.getElementById('spin'+id).className='fas fa-edit'
    },
    error: function (error) {},
  });

}



  function updateDepartment() {
    document.getElementById('updatebutton').innerHTML='Loading ...'
    var id = document.getElementById("eidtid").value;
    var name = document.getElementById("deptname").value;
    var code = document.getElementById("deptcode").value;
    var status = document.getElementById("deptstatus").value;
  
    $.ajax({
      type: "POST",
      url: "http://127.0.0.1:8000/updateDepartment/",
      data: {
        eid: id,
        DepartmentName: name,
        DepartmentCode: code,
        status: status,
      },
      dataType: "json",
      success: function (data) {
        
        console.log("Update successful:", data);
       
        $("#modal-default").modal("hide");
        document.getElementById('updatebutton').innerHTML='Update'
        location.reload();
      },
      error: function (error) {
        console.error("Error updating department:", error);
        
      },
    });
  }

function del(id){
  console.log(id);
  document.getElementById('delid').value=id
  $('#myModal').modal("show");

}
function deletedipartment(){
  var id = document.getElementById('delid').value;
  document.getElementById('delet').innerHTML='Deleting...' 
  // alert(id)
  $.ajax({
    type: 'POST' ,
    url: "http://127.0.0.1:8000/deleteDipartment/",
    data:{
      dId : id
    },
    dataType:'json',
    success: function (data) {

      console.log("Delete successful:", data);
    
      $("#myModal").modal("hide");
      document.getElementById('delet').innerHTML='Delete'
      location.reload();
      

    },
    error: function (error) {
      console.log(error);
    },

  })

}
function DeleteAdminClass(){
  
  
  var id = document.getElementById('delid').value;
  document.getElementById('delet').innerHTML='Deleting...' 
  alert(id)
  $.ajax({
    type: 'POST' ,
    url: "http://127.0.0.1:8000/deleteClass/",
    data:{
      dId : id
    },
    dataType:'json',
    success: function (data) {

      console.log("Delete successful:", data);
    
      $("#myModal").modal("hide");
      document.getElementById('delet').innerHTML='Delete'
      location.reload(true);
      

    },
    error: function (error) {
      console.log(error);
    },

  })

}

function editClass(id){
  document.getElementById('editbutton'+id).className='fas fa-spinner'
  $.ajax({
    url:'http://127.0.0.1:8000/editClass/',
    type:'POST',
    data:{
      'eid':id
    },
    datatype:'json',
    success:function(data){
      document.getElementById("ClassName").value=data.className
      document.getElementById('status').value=data.status
      document.getElementById('editid').value=data.id
      $('#modal-default').modal('show')
      document.getElementById('editbutton'+id).className='fas fa-edit'
    },
    error:function(error){
      console.log('error')
    }

  })
}
function updateClass(id){
  var classname=document.getElementById("ClassName").value
  var status=document.getElementById('status').value
  var id=document.getElementById('editid').value
  document.getElementById('updateButton').innerHTML='Updating...'
  $.ajax({
    url:'http://127.0.0.1:8000/updateClass/',
    type:'POST',
    data:{
      'classname':classname,
      'status':status,
      'id':id

    },
    datatype:'json',
    success:function(data){
      $('#modal-default').modal('hide')
      location.reload();
      alert(data.msg)
   
      document.getElementById('updateButton').innerHTML='Update'

    },
    error:function(error){
      console.log(error)
    }
  })

}

function SubjectM(id){
  document.getElementById('spin'+id).className='fas fa-spinner'
  document.getElementById('Subjectid').value=id
  alert(id)
  $.ajax({
    type: "POST",
    url: "http://127.0.0.1:8000/editSubject/",
    data: {
      'eid': id
    },
    dataType: "json",
    success: function (data) {
      document.getElementById('SubjectMName').value=data.subject.subjectName
      document.getElementById('SubjectMStatus').value=data.subject.status
      
      for (var element of data.classes) {
        console.log(element);
    }
      $("#modal-default").modal("show");
      document.getElementById('spin'+id).className='fas fa-edit'
    }
  })
}

// employee catagory
function showDiv() {
  alert('hii')
  var selectdep = document.getElementById("selectOption");
  var divToShow = document.getElementById("divToShow");

  // Reset display for all divs
  divToShow.style.display = "none";
  var a=selectdep.value.split('+')[1]

  // Check the selected option and show the corresponding div
  if (a === "2") {
    document.getElementById("divToShow").style.display = "block";
  } else {
    divToShow.style.display = "none";
    // Show another div based on the selected option
    // Add more conditions as needed
  }
  // Add more conditions as needed for other options
}

function selectSubject() {
  var id = document.getElementById('selectCla').value;

  $.ajax({
    url: 'http://127.0.0.1:8000/selectSubject/',
    type: 'POST',
    data: {
      'sid': id
    },
    dataType: 'json',
    success: function (data) {
      // alert("Request successful");

      var selectsub = document.getElementById("dynamicSelect");

      // Clear existing options
      selectsub.innerHTML = '';

      // Check if 'subjects' exists in the response
      if (data.subjects && Array.isArray(data.subjects)) {
        var subjects = data.subjects;

        var option = document.createElement("option");
        option.value = '';
        option.text = '--Select Subject--';
        selectsub.appendChild(option);

        // Loop through the subjects array and create option elements
        for (var i = 0; i < subjects.length; i++) {
          var option = document.createElement("option");
          option.value = subjects[i].subid;
          option.text = subjects[i].subname;
          selectsub.appendChild(option);
        }
      } else {
        console.error('Invalid data structure:', data);
      }
    },
    error: function (error) {
      console.error('Request failed:', error);
    }
  });
}
var count = 1;  // Assuming count is declared somewhere in your script

function addRow() {
  // Get input values
  var class_std = document.getElementById("selectCla");
  var division = document.getElementById("division");
  var subject = document.getElementById("dynamicSelect");

  // Get table reference
  var table = document.getElementById("dataTable").getElementsByTagName('tbody')[0];

  // Check if the entry already exists
  var isDuplicate = false;
  for (var i = 0, row; row = table.rows[i]; i++) {
    var existingClass = row.cells[1].innerText;
    var existingDivision = row.cells[2].innerText;
    var existingSubject = row.cells[3].innerText;

    if (class_std.options[class_std.selectedIndex].text === existingClass && division.options[division.selectedIndex].text === existingDivision && subject.options[subject.selectedIndex].text === existingSubject) {
      isDuplicate = true;
      break;
    }
  }

  // If duplicate, display a message and return
  if (isDuplicate) {
    alert("Entry already exists in the table!");
    return;
  }

  // Create a new row
  var newRow = table.insertRow(table.rows.length);

  // Insert cells with input values
  var cell0 = newRow.insertCell(0);
  var cell1 = newRow.insertCell(1);
  var cell2 = newRow.insertCell(2);
  var cell3 = newRow.insertCell(3);
  var cell4 = newRow.insertCell(4);

  cell0.innerHTML = count++;
  cell1.innerHTML = class_std.options[class_std.selectedIndex].text;

  // Create an input element and set its value
  var inputElement1 = document.createElement("input");
  inputElement1.type = "hidden";
  inputElement1.name = "Eclass";
  inputElement1.value = class_std.value;
  cell1.appendChild(inputElement1);

  cell2.innerHTML = division.options[division.selectedIndex].text;
  var inputElement2 = document.createElement("input");
  inputElement2.type = "hidden";
  inputElement2.name = "Edivision";
  inputElement2.value = division.value;
  cell2.appendChild(inputElement2);

  cell3.innerHTML = subject.options[subject.selectedIndex].text;
  var inputElement3 = document.createElement("input");
  inputElement3.type = "hidden";
  inputElement3.name = "Esubject";
  inputElement3.value = subject.value;
  cell3.appendChild(inputElement3);

  cell4.innerHTML = '<a onclick="deleteRow(this)" class="btn btn-sm btn-danger"><i class="fas fa-trash"></i></a>';

  // Clear input values
  class_std.value = "";
  division.value = "";
  subject.value = "";

  
}
function deleteRow(row) {
  var rowIndex = row.parentNode.parentNode.rowIndex;
  document.getElementById("dataTable").deleteRow(rowIndex);
}