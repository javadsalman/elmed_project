const shareController = (function () {
    const url = encodeURIComponent(window.location.href);
    const copyButton = $('#copy-url');
    function popShareButton(id, link, name) {
        $(`#${id}`).click(function () {
            window.open(link + url, `${name}-share-dialog`, 'width=800,height=600');
            return false;
        });
    }

    function init() {
        popShareButton('fb-share-button', 'https://www.facebook.com/sharer/sharer.php?u=', 'facebook');
        popShareButton('twitter-share-button', 'https://twitter.com/intent/tweet?url=', 'twitter');
        popShareButton('whatsapp-share-button', 'https://api.whatsapp.com/send?text=', 'whatsapp');
        popShareButton('linkedin-share-button', 'https://www.linkedin.com/sharing/share-offsite/?url=', 'linkedin');
    
        $('#mail-share').attr('href', `mailto:?body=${url}`);
    
        copyButton.tooltip();
        copyButton.click(function (event) {
            console.log('bura girir')
            event.preventDefault();
            const newInput = $('<input>')
            newInput.attr({
                id: 'input-for-url',
                type: 'text',
                style: 'width:5px; border:none;',
                value: location.href,
            });
            $('#share-section').append(newInput);
            rawInput = newInput[0];
            rawInput.select();
            rawInput.setSelectionRange(0, rawInput.value.length);
            document.execCommand('copy');
            newInput.remove();
            setTimeout(() => {
                $(this).tooltip('hide');
            }, 800)
        });
    }

    return {
        init: init
    };
})();

shareController.init();