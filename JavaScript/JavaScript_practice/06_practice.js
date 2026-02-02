function writeNote() {
  let name = document.getElementById('writer').value; // name input 값 가져오기
  let content = document.getElementById('content').value; // conent input 값 가져오기

  let table = document.getElementById('table'); // table 요소 선택
  let tr = document.createElement('tr'); // tr 생성 (td, td, td, td 넣기 위함)

  // 작성자 cell 만들기
  let tdWriter = document.createElement('td');
  tdWriter.innerText = name;

  // 내용 cell 만들기
  let tdContent = document.createElement('td');
  tdContent.innerText = content;

  // 작성일 cell 만들기
  let tdDate = document.createElement('td');
  let now = new Date();
  tdDate.innerText = `${now.getFullYear()}-${
    now.getMonth() + 1
  }-${now.getDate()} ${now.getHours()}:${now.getMinutes()}`;

  // tr에 위에서 만든 3개의 td 추가
  tr.append(tdWriter, tdContent, tdDate);

  // table에 tr 추가
  table.append(tr);

  // input 창 초기화
  document.getElementById('writer').value = '';
  document.getElementById('content').value = '';
}