let crData;
$.ajax({
  url: "/craw",
  type: "GET",
  success: function(data) {
    crData = JSON.parse(data);
  }
})
$("#crBtn").on("click", () => {
  $("tbody").html("");
  for (var i = 0; i < crData["destinations"].length; i++) {
    var raw = `
    <tr>
      <th scope="row">${i + 1}</th>
      <td>${crData["departures"][i]}</td>
      <td>${crData["destinations"][i]}</td>
      <td>$${crData["prices"][i]}</td>
    </tr>
    `;
    $("tbody").append(raw);
  }
})