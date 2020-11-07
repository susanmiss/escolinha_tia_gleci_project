
document.addEventListener("DOMContentLoaded", function (event) {
    console.log('This is school.js  :) ');
    let sc = document.createElement('script');
    sc.setAttribute('src', 'https://cdn.tiny.cloud/1/jmtexy221mrzqvcizjju46pi2ve2leis67a09mlp1qhjj9si/tinymce/5/tinymce.min.js');

    document.head.appendChild(sc)

    sc.onload = () => {
        // tinymce.init({
        //     selector: '#id_description'
        // });

        var useDarkMode = window.matchMedia('(prefers-color-scheme: dark)').matches;

        tinymce.init({
            selector: 'textarea#id_description',
            menubar: 'file edit view insert format tools table tc help',
            toolbar: 'undo redo | bold italic underline strikethrough |  alignleft aligncenter alignright alignjustify | outdent indent | forecolor backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | a11ycheck ltr rtl | showcomments addcomment',
            image_class_list: [
                { title: 'None', value: '' },
                { title: 'Some class', value: 'class-name' }
            ],
            height: 600,
            image_caption: true,
            quickbars_selection_toolbar: 'bold italic | quicklink h2 h3 blockquote quickimage quicktable',
            noneditable_noneditable_class: 'mceNonEditable',
            toolbar_mode: 'sliding',
            spellchecker_whitelist: ['Ephox', 'Moxiecode'],
            tinycomments_mode: 'embedded',
            content_style: '.mymention{ color: gray; }',
            contextmenu: 'link image imagetools table configurepermanentpen',
            a11y_advanced_options: true,
            skin: useDarkMode ? 'oxide-dark' : 'oxide',
            content_css: useDarkMode ? 'dark' : 'default',
        });
    }

});



