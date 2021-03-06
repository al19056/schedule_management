/*****************************************************
 ***Designer:山川
 ***Date:2021.6.4
 ***Purpose:W4における 追加・削除，決定ボタンの機能実装
 ****************************************************/

function planAddForm() {
  /*
    追加ボタン押下時に入力欄を追加する

    引数：なし
    戻り値：なし
  */
  $(
    '<div class="plan-info" id="plan-info">' +
    '<div class="col-sm-3 text-center">' +
    '<label for="start">開始時刻</label>' +
    '<input type=datetime-local id="start" name="start" class="start form-control" min="2000-01-01" max="2099-12-31">' +
    '</div>' +
    '<div class="col-sm-3 text-center">' +
    '<label for="end">終了時刻</label>' +
    '<input type="datetime-local" id="end" name="end" class="end form-control" min="2000-01-01" max="2099-12-31">' +
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
    '<input type="hidden" name="planID" id="planID">' +
    '</div>' +
    '</div>')
    .appendTo("#plans");
}

function planDeleteForm(thisObj) {
  /*
    削除ボタン押下時、登録済みの予定の時は削除要求をpost
    その後
      2行以上欄がある:その行を削除
      1行しかない    :その行をクリア

    引数：
      thisObj:削除ボタンを押されたform

    戻り値：
      なし
  */
  var target = $(thisObj).parent().parent(); //target is plan-info class
  var id = target.find('#planID').val();

  //idがあるとき(登録済みの予定を削除)
  if (id != "") {
    //削除するidをpost(他は空文字)
    $.post('/plan/edit', '{"start":"","end":"","title":"","planID":"' + id + '"}')
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
}

function postPlanEdit(thisObj) {
  /*
    thisObjのフォームに入力されている情報をpost(JSON形式)

    引数：
      thisObj:決定ボタンを押されたform

    戻り値：
      なし
  */
  //post要求の返信待ちでないとき
  if (nowDoing == false) {
    nowDoing = true;
    var start = $(thisObj).parent().parent().find("#start").val();
    var end = $(thisObj).parent().parent().find("#end").val();
    var planName = $(thisObj).parent().parent().find("#plan-name").val();
    var id = $(thisObj).parent().parent().find("#planID").val();
    var idFind = $(thisObj).parent().parent().find("#planID")

    //必要情報の欠如、時間矛盾、同一日内に終わらない予定の時エラーアラート
    if (start == "" || end == "" || planName == "" || start >= end || start.substr(0, 10) != end.substr(0, 10) || start.length != 16 || end.length != 16 || !("1900-01-01T00:00" < start && start < "2100-01-01T00:00") || !("1900-01-01T00:00" < end && end < "2100-01-01T00:00")) {
      nowDoing = false;
      if (start.substr(0, 10) == end.substr(0, 10)) {
        alert("正しい値を入力してください")
      }
      else {
        alert("複数日にまたがる予定の追加はできません")
      }
      return;
    }
    var resStr = "{'start':'" + start + "','end':'" + end + "','title':'" + planName + "','planID':'" + id + "'}" //post用json文字列
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
}


//追加ボタン押下
$('#add').click(function () {
  planAddForm();
});

//削除ボタン押下(予定の削除に対応)
$(document).on("click", ".del", function () {
  planDeleteForm(this)
});

nowDoing = false; //postの応答待ち状態
//決定ボタン押下(予定の追加と更新に対応)
$(document).on("click", "#decide", function () {
  postPlanEdit(this);
});
