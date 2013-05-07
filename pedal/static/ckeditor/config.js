/*
Copyright (c) 2003-2011, CKSource - Frederico Knabben. All rights reserved.
For licensing, see LICENSE.html or http://ckeditor.com/license
*/

window.onload = function() {
    if (document.getElementsByTagName('textarea').length >0 ) {
	CKEDITOR.replace( 'content', {
            skin: 'BootstrapCK-Skin',
            extraPlugins : 'MediaEmbed',
            toolbar: [
            { 'name': 'document', 'items' : [ 'NewPage','Preview' ] },
            { 'name': 'clipboard', 'items' : [ 'Cut','Copy','Paste','PasteText','PasteFromWord','-','Undo','Redo' ] },
            { 'name': 'insert', 'items' : [ 'Image','MediaEmbed','HorizontalRule',,
                                            , ] },
            { 'name': 'basicstyles', 'items' : [ 'Bold','Italic','Strike','-' ] },
            { 'name': 'paragraph', 'items' : [ 'NumberedList','BulletedList','-' ] },
            { 'name': 'links', 'items' : [ 'Link'] },
            { 'name': 'tools', 'items' : [ 'Maximize','-','About', ] },
            { name: 'styles', items : ['Format','FontSize', 'TextColor' ] },
            ],
            resize_enabled: false,
            filebrowserBrowseUrl: window.location.href+'get_pics/',
            filebrowserWindowWidth: '50%',
            forcePasteAsPlainText: true,
            fillEmptyBlocks: false,
            entities: false,
            autoParagraph: false,
            tabSpaces: 0
        } );
    }
};

CKEDITOR.on('dialogDefinition', function(ev)
            {
	        var dialogName = ev.data.name;
	        var dialogDefinition = ev.data.definition;
	        if (dialogName == 'image') {
		    dialogDefinition.removeContents('advanced');
                    dialogDefinition.minHeight = 250;
                    dialogDefinition.removeContents('Link');
                }
                if (dialogName == 'link') {
                    dialogDefinition.removeContents('advanced');
                    dialogDefinition.removeContents('target');
                }
});
