function OpenPopup(studentid) {
  const pop = document.getElementById('deleteModal');
  const confirmBtn = document.getElementById('confirmDeleteBtn');

  confirmBtn.href = '/students/delete/' + studentid;
  pop.style.display = 'flex';

}

function ClosePopup() {
  const pop = document.getElementById('deleteModal');
  pop.style.display = 'none';
}
