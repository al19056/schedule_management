/**
 ***Designer:山川
 ***Date:2021.6.4
 ***Purpose:予定の空行追加と削除，決定ボタンの実装
 ***/
//追加ボタン押下
$('#add').click(function () {
  /*空行の追加
      引数なし
      戻り値なし
  */
  $(
    '<div class="plan-info" id="plan-info">' +
    '<div class="col-sm-3 text-center">' +
    '<label for="start">開始時刻</label>' +
    '<input type=datetime-local id="start" name="start" class="start form-control">' +
    '</div>' +
    '<div class="col-sm-3 text-center">' +
    '<label for="end">終了時刻</label>' +
    '<input type="datetime-local" id="end" name="end" class="end form-control">' +
    '</div>' +
    '<div class="col-sm-4 text-center">' +
    '<label for="plan-name">予定名</label>' +
    '<input type="text" id="plan-name" name="plan-name" class="plan-name form-control">' +
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
    .appendTo("#plans")
});

//削除ボタン押下(予定の削除に対応)
$(document).on("click", ".del", function () {
  /*削除処理
      引数なし
      戻り値なし
  */
  var target = $(this).parent().parent(); //target is plan-info class
  var id = target.find('#id').val();
  //idがあるとき(登録済みの予定を削除)
  if (id != "") {
    //削除するidをpost
    $.post('/plan/edit', '{"start":"","end":"","title":"","id":"' + id + '"}')
      .done(function (data) {
        if (data == "success del") {
          alert("予定の削除に成功しました")
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
//決定ボタン押下(予定の追加と更新に対応)
$(document).on("click", "#decide", function () {
  if (nowDoing == false) {
    nowDoing = true;
    var start = $(this).parent().parent().find("#start").val();
    var end = $(this).parent().parent().find("#end").val();
    var planName = $(this).parent().parent().find("#plan-name").val();
    var id = $(this).parent().parent().find("#id").val();
    var idFind = $(this).parent().parent().find("#id")

    if (start == "" || end == "" || planName == "" || start >= end) {
      nowDoing = false;
      alert("正しい値を入力してください")
      return;
    }
    var resStr = "{'start':'" + start + "','end':'" + end + "','title':'" + planName + "','id':'" + id + "'}"
    $.post('/plan/edit', resStr)
      .done(function (data) {
        if (data == 'success update') {
          alert("予定の編集に成功しました")
        }
        else if (data == 'failed') {
          alert("失敗しました。再度入力をお試しください")
        }
        else {
          alert("予定の追加に成功しました")
          idFind.val(data)
        }
        nowDoing = false;
      })
  }
});
