/*******************************************************
 ***Designer:山川
 ***Date:2021.6.4
 ***Purpose:W5,6における追加・削除，決定ボタンの機能実装
 ******************************************************/

function taskAddForm() {
  /* 
    追加ボタン押下時に入力欄を追加する

    引数：なし
    戻り値：なし    
  */
  $(
    '<div class="task-info" id="task-info">' +
    '<div class="col-sm-3 text-center">' +
    '<label for="due">締切日</label>' +
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
    '<input type="hidden" name="taskID" id="taskID">' +
    '</div>' +
    '</div>')
    .appendTo("#tasks")
}
function taskDeleteForm(thisObj) {
  /*
    登録済みの課題の時は削除要求をpost
    その後
      2行以上欄がある:その行を削除
      1行しかない    :その行をクリア

    引数：
      thisObj:削除ボタンを押されたform
    
    戻り値：
      なし
  */
  var target = $(thisObj).parent().parent(); //target is task-info class
  var id = target.find('#taskID').val();
  //idがあるとき(登録済みの課題を削除)
  if (id != "") {
    //削除するidをpost(他は空文字)
    $.post('/task/edit', '{"due":"","need":"","title":"","taskID":"' + id + '"}')
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

function postTaskEdit(thisObj) {
  /*
    thisObjのフォームに入力されている情報をpost(JSON形式)

    引数：
      thisObj:決定ボタンを押されたform

    戻り値：
      なし
  */
  //postようきゅの返信待ちでないとき
  if (nowDoing == false) {
    nowDoing = true;
    var due = $(thisObj).parent().parent().find("#due").val();
    var need = $(thisObj).parent().parent().find("#need").val();
    var taskName = $(thisObj).parent().parent().find("#task-name").val();
    var id = $(thisObj).parent().parent().find("#taskID").val();
    var idFind = $(thisObj).parent().parent().find("#taskID")

    //必要情報の欠如、必要時間が0以下の時エラーアラート
    if (due == "" || need == "" || taskName == "" || need <= "0") {
      nowDoing = false;
      alert("正しい値を入力してください")
      return;
    }
    var resStr = "{'due':'" + due + "','need':'" + need + "','title':'" + taskName + "','taskID':'" + id + "'}"//post用json文字列
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
}


//追加ボタン押下
$('#add').click(function () {
  taskAddForm();
});

//削除ボタン押下(課題の削除に対応)
$(document).on("click", ".del", function () {
  taskDeleteForm(this);
});

nowDoing = false; //postの応答待ち状態
//決定ボタン押下(課題の追加と更新に対応)
$(document).on("click", "#decide", function () {
  postTaskEdit(this)
});
