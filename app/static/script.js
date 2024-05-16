  $(document).ready(function() {
    const replyButton = $("#reply-btn");
    const replyForm = $("#reply-form-req-page");

    replyButton.on("click", function() {
      replyForm.toggle();
    });

    // Prevent form submission on submit
    $("#reply-form-element").on("submit", function(e) {
      e.preventDefault();
      console.log("Form submitted");
    });
  });