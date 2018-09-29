// <script>
    function shareLink() {
      var copyLink = document.getElementById("link");
      copyLink.select();
      document.execCommand("Copy");
      alert("Link Copied: " + copyLink.value);
    }
  // </script>
