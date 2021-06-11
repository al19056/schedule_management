/**
 ***Designer:山川
 ***Date:2021.6.4
 ***Purpose:課題の空行追加と削除，決定ボタンの実装
 ***/
//追加ボタン押下
$('#add').click(function () {
  /*空行の追加
      引数なし
      戻り値なし
  */
  $(
    '<div class="task-info" id="task-info">' +
    '<div class="col-sm-3 text-center">' +
    '<label for="due">締め切り日</label>' +
    '<input type=datetime-local id="due" name="due" class="due form-control">' +
    '</div>' +
    '<div class="col-sm-3 text-center">' +
    '<label for="need">必要時間</label>' +
    '<input type="number" id="need" name="need" class="need form-control">' +
    '</div>' +
    '<div class="col-sm-4 text-center">' +
    '<label for="task-name">課題名</label>' +
    '<input type="text" id="task-name" name="task-name" class="task-name form-control">' +
    '</div>' +
    '<div class="col-sm-1">' +
    '<label>　</label>' +
    '<input type="button" name="decide" class="decide form-control btn-primary" value="決定" id="decide">' +
    '</div>' +
    '<div class="col-sm-1">' +
    '<label>　</label>' +
    '<input type="button" name="del" class="del form-control" value="削除">' +
    '</div>' +
    '<div>' +
    '<input type="hidden" name="id" id="id">' +
    '</div>' +
    '</div>')
    .appendTo("#tasks")
});

//削除ボタン押下(課題の削除に対応)
$(document).on("click", ".del", function () {
  /*削除処理
      引数なし
      戻り値なし
  */
  var target = $(this).parent().parent(); //target is task-info class
  var id = target.find('#id').val();
  //idがあるとき(登録済みの課題を削除)
  if (id != "") {
    //削除するidをpost
    $.post('/task/edit', '{"due":"","need":"","title":"","id":"' + id + '"}')
      .done(function (data) {
        if (data == "success del") {
          alert("課題の削除に成功しました")
        }
        else if (data == "failed") {
          alert("失敗しました。再度入力をお試しください")
        }
        else { alert(data) }
      })
  }
  //欄の削除
  //2行以上の時の削除
  if (target.parent().children().length > 1) {
    target.remove();
  }
  //1行のみの時に削除(入力クリア)
  else {
    target
      .find("input")
      .not(":button,:submit")
      .val("")
  }
});

let nowDoing = false; //postの返信が来る前に決定できないようにするため
//決定ボタン押下(課題の追加と更新に対応)
$(document).on("click", "#decide", function () {
  if (nowDoing == false) {
    nowDoing = true;
    var due = $(this).parent().parent().find("#due").val();
    var need = $(this).parent().parent().find("#need").val();
    var taskName = $(this).parent().parent().find("#task-name").val();
    var id = $(this).parent().parent().find("#id").val();
    var idFind = $(this).parent().parent().find("#id")

    if (due == "" || need == "" || taskName == "" || need <= "0") {
      nowDoing = false;
      alert("正しい値を入力してください")
      return;
    }
    var resStr = "{'due':'" + due + "','need':'" + need + "','title':'" + taskName + "','taskID':'" + id + "'}"
    $.post('/task/edit', resStr)
      .done(function (data) {
        if (data == 'success update') {
          alert("課題の編集に成功しました")
        }
        else if (data == 'failed') {
          alert("失敗しました。再度入力をお試しください")
        }
        else {
          alert("課題の追加に成功しました")
          idFind.val(data)
        }
        nowDoing = false;
      })
  }
});
