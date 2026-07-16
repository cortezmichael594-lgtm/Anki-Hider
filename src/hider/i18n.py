# Copyright (C) 2026 AnkiCraft
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
from __future__ import annotations

from functools import lru_cache

FALLBACK: str = "en"

TRANSLATIONS: dict[str, dict[str, str]] = {
    "en": {
        "button_hidden": "That button is hidden. You can only answer \u00abAgain\u00bb or \u00abGood\u00bb.",
        "hook_error": "Hider ran into a problem and disabled that part for safety. "
        "Check the add-on's configuration.",
        "dialog_title": "Hider",
        "group_review": "While reviewing, hide:",
        "group_behaviour": "Behaviour",
        "opt_menu_bar": "The menu bar (File, Edit, Tools...)",
        "opt_menu_bar_tip": "Reappears as soon as you leave review.",
        "opt_toolbar": "The top toolbar (Decks, Add, Browse, Stats)",
        "opt_toolbar_tip": "Reappears as soon as you leave review.",
        "opt_bottom_bar": "The bottom bar of the window",
        "opt_bottom_bar_tip": "Reappears as soon as you leave review.",
        "opt_scrollbar": "The card's scrollbar",
        "opt_scrollbar_tip": "Visual only: you can still scroll with the mouse wheel. "
        "The change takes effect on the next card.",
        "opt_hard_easy": "The \u00abHard\u00bb and \u00abEasy\u00bb buttons",
        "opt_hard_easy_tip": "Leaves only \u00abAgain\u00bb and \u00abGood\u00bb. Their keyboard shortcuts "
        "are also blocked, so you don't accidentally answer with a button you can't see.",
        "opt_cursor": "The mouse pointer when idle for:",
        "opt_cursor_tip": "Reappears as soon as you move the mouse.",
        "opt_cursor_suffix": " s",
        "opt_auto_start": "Start reviewing automatically when opening a deck",
        "opt_auto_start_tip": "Only if there are due cards. If you're the one who leaves review, "
        "Hider won't put you back in.",
        "btn_save": "OK",
        "btn_cancel": "Cancel",
        "btn_defaults": "Restore default values",
        "saved": "Hider configuration saved.",
        "save_failed": "Could not save Hider's configuration.",
        "version_line": "{name} v{version}",
        "welcome_title": "{name} v{version}",
        "kofi_button": "\u2615 Buy me a coffee",
        "kofi_tooltip": "Support development on Ko-fi",
        "patreon_button": "\u2665 Patreon",
        "rate_button": "\U0001f44d Rate this add-on",
        "report_button": "Report a bug",
        "welcome_close": "Close",
        "welcome_body": (
            "Hider keeps your Anki screen clean while you study. "
            "It can hide the menu bar, top toolbar, bottom bar, scrollbar, "
            "and Hard/Easy buttons during review \u2014 everything reappears "
            "the moment you leave.\n\n"
            "You can also hide the mouse cursor when idle and start reviewing "
            "automatically when you open a deck.\n\n"
            "To adjust what gets hidden, go to "
            "Tools \u2192 Add-ons \u2192 {name} \u2192 Config."
        ),
        "welcome_support_note": (
            "This add-on is free and open source (AGPLv3). "
            "If it saves you time, consider supporting its development."
        ),
    },
    "es": {
        "button_hidden": "Ese bot\u00f3n est\u00e1 oculto. Solo puedes responder \u00abDe nuevo\u00bb o \u00abBien\u00bb.",
        "hook_error": "Hider ha encontrado un problema y ha desactivado esa parte por seguridad. "
        "Revisa la configuraci\u00f3n del complemento.",
        "dialog_title": "Hider",
        "group_review": "Durante el repaso, ocultar:",
        "group_behaviour": "Comportamiento",
        "opt_menu_bar": "La barra de men\u00fa (Archivo, Editar, Herramientas...)",
        "opt_menu_bar_tip": "Vuelve a aparecer en cuanto sales del repaso.",
        "opt_toolbar": "La barra superior (Mazos, A\u00f1adir, Explorar, Estad\u00edsticas)",
        "opt_toolbar_tip": "Vuelve a aparecer en cuanto sales del repaso.",
        "opt_bottom_bar": "La barra inferior de la ventana",
        "opt_bottom_bar_tip": "Vuelve a aparecer en cuanto sales del repaso.",
        "opt_scrollbar": "La barra de desplazamiento de la tarjeta",
        "opt_scrollbar_tip": "Solo visual: puedes seguir bajando con la rueda del rat\u00f3n. "
        "El cambio se nota en la tarjeta siguiente.",
        "opt_hard_easy": "Los botones \u00abDif\u00edcil\u00bb y \u00abF\u00e1cil\u00bb",
        "opt_hard_easy_tip": "Deja solo \u00abDe nuevo\u00bb y \u00abBien\u00bb. Sus atajos de teclado tambi\u00e9n "
        "quedan bloqueados, para que no respondas sin querer con un bot\u00f3n que no ves.",
        "opt_cursor": "El puntero del rat\u00f3n cuando lleva quieto:",
        "opt_cursor_tip": "Reaparece en cuanto mueves el rat\u00f3n.",
        "opt_cursor_suffix": " s",
        "opt_auto_start": "Empezar el repaso autom\u00e1ticamente al abrir un mazo",
        "opt_auto_start_tip": "Solo si hay tarjetas pendientes. Si eres t\u00fa quien sale del repaso, "
        "Hider no te vuelve a meter dentro.",
        "btn_save": "Aceptar",
        "btn_cancel": "Cancelar",
        "btn_defaults": "Restaurar los valores predeterminados",
        "saved": "Configuraci\u00f3n de Hider guardada.",
        "save_failed": "No se ha podido guardar la configuraci\u00f3n de Hider.",
        "version_line": "{name} v{version}",
        "welcome_title": "{name} v{version}",
        "kofi_button": "\u2615 Ko-fi",
        "kofi_tooltip": "Apoya el desarrollo en Ko-fi",
        "patreon_button": "\u2665 Patreon",
        "rate_button": "\U0001f44d Valorar este complemento",
        "report_button": "Reportar un error",
        "welcome_close": "Cerrar",
        "welcome_body": (
            "Hider mantiene tu pantalla de Anki limpia mientras estudias. "
            "Puede ocultar la barra de men\u00fa, la barra superior, la barra inferior, "
            "la barra de desplazamiento y los botones Dif\u00edcil/F\u00e1cil durante el repaso "
            "\u2014 todo vuelve a aparecer en cuanto sales.\n\n"
            "Tambi\u00e9n puedes ocultar el cursor del rat\u00f3n cuando est\u00e1 inactivo "
            "e iniciar el repaso autom\u00e1ticamente al abrir un mazo.\n\n"
            "Para ajustar qu\u00e9 se oculta, ve a "
            "Herramientas \u2192 Complementos \u2192 {name} \u2192 Config."
        ),
        "welcome_support_note": (
            "Este complemento es gratuito y de c\u00f3digo abierto (AGPLv3). "
            "Si te ahorra tiempo, considera apoyar su desarrollo."
        ),
    },
    "fr": {
        "button_hidden": "Ce bouton est masqu\u00e9. Vous ne pouvez r\u00e9pondre qu'avec \u00ab\u00a0\u00c0 revoir\u00a0\u00bb ou \u00ab\u00a0Correct\u00a0\u00bb.",
        "hook_error": "Hider a rencontr\u00e9 un probl\u00e8me et a d\u00e9sactiv\u00e9 cette partie par s\u00e9curit\u00e9. "
        "V\u00e9rifiez la configuration du module.",
        "dialog_title": "Hider",
        "group_review": "Pendant la r\u00e9vision, masquer\u00a0:",
        "group_behaviour": "Comportement",
        "opt_menu_bar": "La barre de menus (Fichier, \u00c9dition, Outils...)",
        "opt_menu_bar_tip": "R\u00e9appara\u00eet d\u00e8s que vous quittez la r\u00e9vision.",
        "opt_toolbar": "La barre d'outils sup\u00e9rieure (Paquets, Ajouter, Parcourir, Statistiques)",
        "opt_toolbar_tip": "R\u00e9appara\u00eet d\u00e8s que vous quittez la r\u00e9vision.",
        "opt_bottom_bar": "La barre inf\u00e9rieure de la fen\u00eatre",
        "opt_bottom_bar_tip": "R\u00e9appara\u00eet d\u00e8s que vous quittez la r\u00e9vision.",
        "opt_scrollbar": "La barre de d\u00e9filement de la carte",
        "opt_scrollbar_tip": "Uniquement visuel\u00a0: vous pouvez toujours d\u00e9filer avec la molette. "
        "Le changement s'applique \u00e0 la carte suivante.",
        "opt_hard_easy": "Les boutons \u00ab\u00a0Difficile\u00a0\u00bb et \u00ab\u00a0Facile\u00a0\u00bb",
        "opt_hard_easy_tip": "Ne laisse que \u00ab\u00a0\u00c0 revoir\u00a0\u00bb et \u00ab\u00a0Correct\u00a0\u00bb. Leurs raccourcis clavier "
        "sont aussi bloqu\u00e9s, pour \u00e9viter de r\u00e9pondre par erreur avec un bouton invisible.",
        "opt_cursor": "Le pointeur de la souris apr\u00e8s une inactivit\u00e9 de\u00a0:",
        "opt_cursor_tip": "R\u00e9appara\u00eet d\u00e8s que vous bougez la souris.",
        "opt_cursor_suffix": " s",
        "opt_auto_start": "D\u00e9marrer la r\u00e9vision automatiquement \u00e0 l'ouverture d'un paquet",
        "opt_auto_start_tip": "Seulement s'il y a des cartes \u00e0 revoir. Si c'est vous qui quittez la r\u00e9vision, "
        "Hider ne vous y remet pas.",
        "btn_save": "Accepter",
        "btn_cancel": "Annuler",
        "btn_defaults": "Restaurer les valeurs par défaut",
        "saved": "Configuration de Hider enregistr\u00e9e.",
        "save_failed": "Impossible d'enregistrer la configuration de Hider.",
        "version_line": "{name} v{version}",
        "welcome_title": "{name} v{version}",
        "kofi_button": "\u2615 Ko-fi",
        "kofi_tooltip": "Soutenir le d\u00e9veloppement sur Ko-fi",
        "patreon_button": "\u2665 Patreon",
        "rate_button": "\U0001f44d \u00c9valuer ce module",
        "report_button": "Signaler un bug",
        "welcome_close": "Fermer",
        "welcome_body": (
            "Hider garde votre \u00e9cran Anki propre pendant la r\u00e9vision. "
            "Il peut masquer la barre de menus, la barre d'outils sup\u00e9rieure, "
            "la barre inf\u00e9rieure, la barre de d\u00e9filement et les boutons "
            "Difficile/Facile \u2014 tout r\u00e9appara\u00eet d\u00e8s que vous quittez.\n\n"
            "Vous pouvez aussi masquer le curseur de la souris au repos et d\u00e9marrer "
            "la r\u00e9vision automatiquement \u00e0 l'ouverture d'un paquet.\n\n"
            "Pour ajuster ce qui est masqu\u00e9\u00a0: "
            "Outils \u2192 Extensions \u2192 {name} \u2192 Config."
        ),
        "welcome_support_note": (
            "Cette extension est gratuite et open source (AGPLv3). "
            "Si elle vous fait gagner du temps, pensez \u00e0 soutenir son d\u00e9veloppement."
        ),
    },
    "de": {
        "button_hidden": "Diese Schaltfl\u00e4che ist ausgeblendet. Du kannst nur mit \u00abErneut\u00bb oder \u00abGut\u00bb antworten.",
        "hook_error": "Hider ist auf ein Problem gesto\u00dfen und hat diesen Teil aus Sicherheitsgr\u00fcnden deaktiviert. "
        "\u00dcberpr\u00fcfe die Einstellungen des Add-ons.",
        "dialog_title": "Hider",
        "group_review": "W\u00e4hrend der Wiederholung ausblenden:",
        "group_behaviour": "Verhalten",
        "opt_menu_bar": "Die Men\u00fcleiste (Datei, Bearbeiten, Extras...)",
        "opt_menu_bar_tip": "Erscheint wieder, sobald du die Wiederholung verl\u00e4sst.",
        "opt_toolbar": "Die obere Symbolleiste (Stapel, Hinzuf\u00fcgen, Durchsuchen, Statistiken)",
        "opt_toolbar_tip": "Erscheint wieder, sobald du die Wiederholung verl\u00e4sst.",
        "opt_bottom_bar": "Die untere Leiste des Fensters",
        "opt_bottom_bar_tip": "Erscheint wieder, sobald du die Wiederholung verl\u00e4sst.",
        "opt_scrollbar": "Die Bildlaufleiste der Karte",
        "opt_scrollbar_tip": "Nur optisch: Du kannst weiterhin mit dem Mausrad scrollen. "
        "Die \u00c4nderung wirkt sich auf die n\u00e4chste Karte aus.",
        "opt_hard_easy": "Die Schaltfl\u00e4chen \u00abSchwer\u00bb und \u00abLeicht\u00bb",
        "opt_hard_easy_tip": "L\u00e4sst nur \u00abErneut\u00bb und \u00abGut\u00bb \u00fcbrig. Auch die Tastenk\u00fcrzel daf\u00fcr werden "
        "blockiert, damit du nicht versehentlich mit einer unsichtbaren Schaltfl\u00e4che antwortest.",
        "opt_cursor": "Den Mauszeiger, wenn er still steht f\u00fcr:",
        "opt_cursor_tip": "Erscheint wieder, sobald du die Maus bewegst.",
        "opt_cursor_suffix": " s",
        "opt_auto_start": "Wiederholung automatisch starten beim \u00d6ffnen eines Stapels",
        "opt_auto_start_tip": "Nur wenn f\u00e4llige Karten vorhanden sind. Wenn du selbst die Wiederholung verl\u00e4sst, "
        "bringt Hider dich nicht wieder hinein.",
        "btn_save": "OK",
        "btn_cancel": "Abbrechen",
        "btn_defaults": "Standardwerte wiederherstellen",
        "saved": "Hider-Konfiguration gespeichert.",
        "save_failed": "Die Hider-Konfiguration konnte nicht gespeichert werden.",
        "version_line": "{name} v{version}",
        "welcome_title": "{name} v{version}",
        "kofi_button": "\u2615 Ko-fi",
        "kofi_tooltip": "Entwicklung auf Ko-fi unterst\u00fctzen",
        "patreon_button": "\u2665 Patreon",
        "rate_button": "\U0001f44d Add-on bewerten",
        "report_button": "Fehler melden",
        "welcome_close": "Schlie\u00dfen",
        "welcome_body": (
            "Hider h\u00e4lt deinen Anki-Bildschirm beim Lernen aufger\u00e4umt. "
            "Es kann die Men\u00fcleiste, die obere Symbolleiste, die untere Leiste, "
            "die Bildlaufleiste und die Schwer/Leicht-Schaltfl\u00e4chen w\u00e4hrend der "
            "Wiederholung ausblenden \u2014 alles erscheint wieder, sobald du die "
            "Wiederholung verl\u00e4sst.\n\n"
            "Du kannst auch den Mauszeiger bei Inaktivit\u00e4t ausblenden und die "
            "Wiederholung automatisch starten, wenn du einen Stapel \u00f6ffnest.\n\n"
            "Um einzustellen, was ausgeblendet wird: "
            "Werkzeuge \u2192 Add-ons \u2192 {name} \u2192 Einstellungen."
        ),
        "welcome_support_note": (
            "Dieses Add-on ist kostenlos und Open Source (AGPLv3). "
            "Wenn es dir Zeit spart, erw\u00e4ge, die Entwicklung zu unterst\u00fctzen."
        ),
    },
    "it": {
        "button_hidden": "Quel pulsante \u00e8 nascosto. Puoi rispondere solo con \u00abDi nuovo\u00bb o \u00abBene\u00bb.",
        "hook_error": "Hider ha riscontrato un problema e ha disattivato quella parte per sicurezza. "
        "Controlla la configurazione del componente aggiuntivo.",
        "dialog_title": "Hider",
        "group_review": "Durante la revisione, nascondi:",
        "group_behaviour": "Comportamento",
        "opt_menu_bar": "La barra dei menu (File, Modifica, Strumenti...)",
        "opt_menu_bar_tip": "Riappare non appena esci dalla revisione.",
        "opt_toolbar": "La barra degli strumenti superiore (Mazzi, Aggiungi, Sfoglia, Statistiche)",
        "opt_toolbar_tip": "Riappare non appena esci dalla revisione.",
        "opt_bottom_bar": "La barra inferiore della finestra",
        "opt_bottom_bar_tip": "Riappare non appena esci dalla revisione.",
        "opt_scrollbar": "La barra di scorrimento della scheda",
        "opt_scrollbar_tip": "Solo visivo: puoi comunque scorrere con la rotella del mouse. "
        "La modifica ha effetto dalla scheda successiva.",
        "opt_hard_easy": "I pulsanti \u00abDifficile\u00bb e \u00abFacile\u00bb",
        "opt_hard_easy_tip": "Lascia solo \u00abDi nuovo\u00bb e \u00abBene\u00bb. Anche le rispettive scorciatoie da tastiera "
        "vengono bloccate, cos\u00ec non rispondi per sbaglio con un pulsante che non vedi.",
        "opt_cursor": "Il puntatore del mouse quando \u00e8 fermo per:",
        "opt_cursor_tip": "Riappare non appena muovi il mouse.",
        "opt_cursor_suffix": " s",
        "opt_auto_start": "Avvia automaticamente la revisione all'apertura di un mazzo",
        "opt_auto_start_tip": "Solo se ci sono schede da rivedere. Se sei tu ad uscire dalla revisione, "
        "Hider non ti ci riporta.",
        "btn_save": "Accetta",
        "btn_cancel": "Annulla",
        "btn_defaults": "Ripristina i valori predefiniti",
        "saved": "Configurazione di Hider salvata.",
        "save_failed": "Impossibile salvare la configurazione di Hider.",
    },
    "pt_BR": {
        "button_hidden": "Esse bot\u00e3o est\u00e1 oculto. Voc\u00ea s\u00f3 pode responder \u00abNovamente\u00bb ou \u00abBom\u00bb.",
        "hook_error": "O Hider encontrou um problema e desativou essa parte por seguran\u00e7a. "
        "Verifique a configura\u00e7\u00e3o do add-on.",
        "dialog_title": "Hider",
        "group_review": "Durante a revis\u00e3o, ocultar:",
        "group_behaviour": "Comportamento",
        "opt_menu_bar": "A barra de menus (Arquivo, Editar, Ferramentas...)",
        "opt_menu_bar_tip": "Reaparece assim que voc\u00ea sai da revis\u00e3o.",
        "opt_toolbar": "A barra de ferramentas superior (Baralhos, Adicionar, Navegar, Estat\u00edsticas)",
        "opt_toolbar_tip": "Reaparece assim que voc\u00ea sai da revis\u00e3o.",
        "opt_bottom_bar": "A barra inferior da janela",
        "opt_bottom_bar_tip": "Reaparece assim que voc\u00ea sai da revis\u00e3o.",
        "opt_scrollbar": "A barra de rolagem do cart\u00e3o",
        "opt_scrollbar_tip": "Apenas visual: voc\u00ea ainda pode rolar com a roda do mouse. "
        "A mudan\u00e7a se aplica no pr\u00f3ximo cart\u00e3o.",
        "opt_hard_easy": "Os bot\u00f5es \u00abDif\u00edcil\u00bb e \u00abF\u00e1cil\u00bb",
        "opt_hard_easy_tip": "Deixa apenas \u00abNovamente\u00bb e \u00abBom\u00bb. Os atalhos de teclado tamb\u00e9m "
        "ficam bloqueados, para que voc\u00ea n\u00e3o responda sem querer com um bot\u00e3o que n\u00e3o v\u00ea.",
        "opt_cursor": "O ponteiro do mouse quando parado por:",
        "opt_cursor_tip": "Reaparece assim que voc\u00ea move o mouse.",
        "opt_cursor_suffix": " s",
        "opt_auto_start": "Iniciar a revis\u00e3o automaticamente ao abrir um baralho",
        "opt_auto_start_tip": "Somente se houver cart\u00f5es pendentes. Se for voc\u00ea quem sair da revis\u00e3o, "
        "o Hider n\u00e3o vai te colocar de volta.",
        "btn_save": "Aceitar",
        "btn_cancel": "Cancelar",
        "btn_defaults": "Restaurar os valores padrão",
        "saved": "Configura\u00e7\u00e3o do Hider salva.",
        "save_failed": "N\u00e3o foi poss\u00edvel salvar a configura\u00e7\u00e3o do Hider.",
    },
    "pt_PT": {
        "button_hidden": "Esse bot\u00e3o est\u00e1 oculto. S\u00f3 podes responder \u00abNovamente\u00bb ou \u00abBom\u00bb.",
        "hook_error": "O Hider encontrou um problema e desativou essa parte por seguran\u00e7a. "
        "Verifica a configura\u00e7\u00e3o do extra.",
        "dialog_title": "Hider",
        "group_review": "Durante a revis\u00e3o, ocultar:",
        "group_behaviour": "Comportamento",
        "opt_menu_bar": "A barra de menus (Ficheiro, Editar, Ferramentas...)",
        "opt_menu_bar_tip": "Reaparece assim que sais da revis\u00e3o.",
        "opt_toolbar": "A barra de ferramentas superior (Baralhos, Adicionar, Explorar, Estat\u00edsticas)",
        "opt_toolbar_tip": "Reaparece assim que sais da revis\u00e3o.",
        "opt_bottom_bar": "A barra inferior da janela",
        "opt_bottom_bar_tip": "Reaparece assim que sais da revis\u00e3o.",
        "opt_scrollbar": "A barra de deslocamento do cart\u00e3o",
        "opt_scrollbar_tip": "Apenas visual: podes continuar a deslocar com a roda do rato. "
        "A altera\u00e7\u00e3o aplica-se no cart\u00e3o seguinte.",
        "opt_hard_easy": "Os bot\u00f5es \u00abDif\u00edcil\u00bb e \u00abF\u00e1cil\u00bb",
        "opt_hard_easy_tip": "Deixa apenas \u00abNovamente\u00bb e \u00abBom\u00bb. Os atalhos de teclado tamb\u00e9m "
        "ficam bloqueados, para que n\u00e3o respondas sem querer com um bot\u00e3o que n\u00e3o v\u00eas.",
        "opt_cursor": "O ponteiro do rato quando parado durante:",
        "opt_cursor_tip": "Reaparece assim que moves o rato.",
        "opt_cursor_suffix": " s",
        "opt_auto_start": "Iniciar a revis\u00e3o automaticamente ao abrir um baralho",
        "opt_auto_start_tip": "Apenas se houver cart\u00f5es pendentes. Se f\u00f6res tu a sair da revis\u00e3o, "
        "o Hider n\u00e3o te volta a p\u00f4r l\u00e1 dentro.",
        "btn_save": "Aceitar",
        "btn_cancel": "Cancelar",
        "btn_defaults": "Restaurar os valores predefinidos",
        "saved": "Configura\u00e7\u00e3o do Hider guardada.",
        "save_failed": "N\u00e3o foi poss\u00edvel guardar a configura\u00e7\u00e3o do Hider.",
    },
    "nl": {
        "button_hidden": "Die knop is verborgen. Je kunt alleen antwoorden met \u00abOpnieuw\u00bb of \u00abGoed\u00bb.",
        "hook_error": "Hider is op een probleem gestuit en heeft dat onderdeel voor de veiligheid uitgeschakeld. "
        "Controleer de instellingen van de add-on.",
        "dialog_title": "Hider",
        "group_review": "Tijdens het overhoren verbergen:",
        "group_behaviour": "Gedrag",
        "opt_menu_bar": "De menubalk (Bestand, Bewerken, Extra's...)",
        "opt_menu_bar_tip": "Verschijnt weer zodra je het overhoren verlaat.",
        "opt_toolbar": "De bovenste werkbalk (Pakketten, Toevoegen, Bladeren, Statistieken)",
        "opt_toolbar_tip": "Verschijnt weer zodra je het overhoren verlaat.",
        "opt_bottom_bar": "De onderste balk van het venster",
        "opt_bottom_bar_tip": "Verschijnt weer zodra je het overhoren verlaat.",
        "opt_scrollbar": "De schuifbalk van de kaart",
        "opt_scrollbar_tip": "Alleen visueel: je kunt nog steeds scrollen met het muiswiel. "
        "De wijziging is zichtbaar bij de volgende kaart.",
        "opt_hard_easy": "De knoppen \u00abMoeilijk\u00bb en \u00abMakkelijk\u00bb",
        "opt_hard_easy_tip": "Laat alleen \u00abOpnieuw\u00bb en \u00abGoed\u00bb over. De sneltoetsen hiervoor worden ook "
        "geblokkeerd, zodat je niet per ongeluk antwoordt met een knop die je niet ziet.",
        "opt_cursor": "De muisaanwijzer wanneer die stilstaat gedurende:",
        "opt_cursor_tip": "Verschijnt weer zodra je de muis beweegt.",
        "opt_cursor_suffix": " s",
        "opt_auto_start": "Automatisch beginnen met overhoren bij het openen van een pakket",
        "opt_auto_start_tip": "Alleen als er kaarten klaarstaan. Als jij zelf het overhoren verlaat, "
        "zet Hider je er niet weer in.",
        "btn_save": "Accepteren",
        "btn_cancel": "Annuleren",
        "btn_defaults": "Standaardwaarden herstellen",
        "saved": "Hider-configuratie opgeslagen.",
        "save_failed": "Kon de Hider-configuratie niet opslaan.",
    },
    "ca": {
        "button_hidden": "Aquest bot\u00f3 est\u00e0 amagat. Nom\u00e9s pots respondre \u00abUn altre cop\u00bb o \u00abB\u00e9\u00bb.",
        "hook_error": "Hider ha trobat un problema i ha desactivat aquesta part per seguretat. "
        "Revisa la configuraci\u00f3 del complement.",
        "dialog_title": "Hider",
        "group_review": "Durant el repas, amaga:",
        "group_behaviour": "Comportament",
        "opt_menu_bar": "La barra de men\u00fa (Fitxer, Edita, Eines...)",
        "opt_menu_bar_tip": "Torna a aparixer tan bon punt surts del repas.",
        "opt_toolbar": "La barra superior (Baralles, Afegeix, Explora, Estad\u00edstiques)",
        "opt_toolbar_tip": "Torna a aparixer tan bon punt surts del repas.",
        "opt_bottom_bar": "La barra inferior de la finestra",
        "opt_bottom_bar_tip": "Torna a aparixer tan bon punt surts del repas.",
        "opt_scrollbar": "La barra de desplazament de la targeta",
        "opt_scrollbar_tip": "Nom\u00e9s visual: pots continuar baixant amb la rodeta del ratol\u00ed. "
        "El canvi es nota a la targeta seg\u00fcent.",
        "opt_hard_easy": "Els botons \u00abDif\u00edcil\u00bb i \u00abF\u00e0cil\u00bb",
        "opt_hard_easy_tip": "Nom\u00e9s deixa \u00abUn altre cop\u00bb i \u00abB\u00e9\u00bb. Les seves dreceres de teclat tamb\u00e9 "
        "queden bloquejades, perqu\u00e8 no responguis sense voler amb un bot\u00f3 que no veus.",
        "opt_cursor": "El punter del ratol\u00ed quan porta quiet:",
        "opt_cursor_tip": "Reapareix tan bon punt mous el ratol\u00ed.",
        "opt_cursor_suffix": " s",
        "opt_auto_start": "Comen\u00e7a el repas autom\u00e0ticament en obrir una barreja",
        "opt_auto_start_tip": "Nom\u00e9s si hi ha targetes pendents. Si ets tu qui surt del repas, "
        "Hider no et torna a ficar dins.",
        "btn_save": "Accepta",
        "btn_cancel": "Cancel\u00b7la",
        "btn_defaults": "Restaura els valors predeterminats",
        "saved": "Configuraci\u00f3 de Hider desada.",
        "save_failed": "No s'ha pogut desar la configuraci\u00f3 de Hider.",
    },
    "gl": {
        "button_hidden": "Ese bot\u00f3n est\u00e1 agochado. S\u00f3 podes responder \u00abDe novo\u00bb ou \u00abBen\u00bb.",
        "hook_error": "Hider atopou un problema e desactivou esa parte por seguranza. "
        "Revisa a configuraci\u00f3n do complemento.",
        "dialog_title": "Hider",
        "group_review": "Durante o repaso, agochar:",
        "group_behaviour": "Comportamento",
        "opt_menu_bar": "A barra de men\u00fa (Ficheiro, Editar, Ferramentas...)",
        "opt_menu_bar_tip": "Volve aparecer en canto sa\u00edas do repaso.",
        "opt_toolbar": "A barra superior (Barallas, Engadir, Explorar, Estat\u00edsticas)",
        "opt_toolbar_tip": "Volve aparecer en canto sa\u00edas do repaso.",
        "opt_bottom_bar": "A barra inferior da fiestra",
        "opt_bottom_bar_tip": "Volve aparecer en canto sa\u00edas do repaso.",
        "opt_scrollbar": "A barra de desprazamento da tarxeta",
        "opt_scrollbar_tip": "S\u00f3 visual: podes seguir baixando coa roda do rato. "
        "O cambio n\u00f3tase na seguinte tarxeta.",
        "opt_hard_easy": "Os bot\u00f3ns \u00abDif\u00edcil\u00bb e \u00abF\u00e1cil\u00bb",
        "opt_hard_easy_tip": "Dixe s\u00f3 \u00abDe novo\u00bb e \u00abBen\u00bb. Os seus atallos de teclado tam\u00e9n "
        "quedan bloqueados, para que non respondas sen querer cun bot\u00f3n que non ves.",
        "opt_cursor": "O punteiro do rato cando leva quieto:",
        "opt_cursor_tip": "Reaparece en canto mov\u00e9s o rato.",
        "opt_cursor_suffix": " s",
        "opt_auto_start": "Comezar o repaso automaticamente ao abrir unha baralla",
        "opt_auto_start_tip": "S\u00f3 se hai tarxetas pendentes. Se es t\u00fa quen sae do repaso, "
        "Hider non te volve meter dentro.",
        "btn_save": "Aceptar",
        "btn_cancel": "Cancelar",
        "btn_defaults": "Restaurar os valores predeterminados",
        "saved": "Configuraci\u00f3n de Hider gardada.",
        "save_failed": "Non se puido gardar a configuraci\u00f3n de Hider.",
    },
    "ro": {
        "button_hidden": "Acel buton este ascuns. Po\u021bi r\u0103spunde doar cu \u00abDin nou\u00bb sau \u00abBine\u00bb.",
        "hook_error": "Hider a \u00eent\u00e2mpinat o problem\u0103 \u0219i a dezactivat acea parte din motive de siguran\u021b\u0103. "
        "Verific\u0103 configura\u021bia suplimentului.",
        "dialog_title": "Hider",
        "group_review": "\u00cen timpul repet\u0103rii, ascunde:",
        "group_behaviour": "Comportament",
        "opt_menu_bar": "Bara de meniu (Fi\u0219ier, Editare, Instrumente...)",
        "opt_menu_bar_tip": "Reapare imediat ce ie\u0219i din repetare.",
        "opt_toolbar": "Bara de instrumente de sus (Pachete, Adaug\u0103, R\u0103sfoie\u0219te, Statistici)",
        "opt_toolbar_tip": "Reapare imediat ce ie\u0219i din repetare.",
        "opt_bottom_bar": "Bara de jos a ferestrei",
        "opt_bottom_bar_tip": "Reapare imediat ce ie\u0219i din repetare.",
        "opt_scrollbar": "Bara de derulare a c\u0103r\u021bii",
        "opt_scrollbar_tip": "Doar vizual: po\u021bi derula \u00een continuare cu rotia mausului. "
        "Schimbarea se observ\u0103 la urm\u0103toarea carte.",
        "opt_hard_easy": "Butoanele \u00abGreu\u00bb \u0219i \u00abU\u0219or\u00bb",
        "opt_hard_easy_tip": "L\u0103sa doar \u00abDin nou\u00bb \u0219i \u00abBine\u00bb. Scurt\u0103turile lor de tastatur\u0103 sunt "
        "de asemenea blocate, ca s\u0103 nu r\u0103spunzi din gre\u0219eal\u0103 cu un buton pe care nu-l vezi.",
        "opt_cursor": "Cursorul mausului c\u00e2nd st\u0103 nemi\u0219cat timp de:",
        "opt_cursor_tip": "Reapare imediat ce mi\u0219ti mausul.",
        "opt_cursor_suffix": " s",
        "opt_auto_start": "Pornire automat\u0103 a repet\u0103rii la deschiderea unui pachet",
        "opt_auto_start_tip": "Doar dac\u0103 exist\u0103 c\u0103r\u021bi scadente. Dac\u0103 tu ie\u0219i din repetare, "
        "Hider nu te mai bag\u0103 \u00eenapoi.",
        "btn_save": "Acceptă",
        "btn_cancel": "Anuleaz\u0103",
        "btn_defaults": "Restabilește valorile implicite",
        "saved": "Configura\u021bia Hider a fost salvat\u0103.",
        "save_failed": "Configura\u021bia Hider nu a putut fi salvat\u0103.",
    },
    "ru": {
        "button_hidden": "\u042d\u0442\u0430 \u043a\u043d\u043e\u043f\u043a\u0430 \u0441\u043a\u0440\u044b\u0442\u0430. \u041c\u043e\u0436\u043d\u043e \u043e\u0442\u0432\u0435\u0442\u0438\u0442\u044c \u0442\u043e\u043b\u044c\u043a\u043e \u00ab\u0417\u0430\u0431\u044b\u043b\u00bb \u0438\u043b\u0438 \u00ab\u0425\u043e\u0440\u043e\u0448\u043e\u00bb.",
        "hook_error": "Hider \u0441\u0442\u043e\u043b\u043a\u043d\u0443\u043b\u0441\u044f \u0441 \u043f\u0440\u043e\u0431\u043b\u0435\u043c\u043e\u0439 \u0438 \u043e\u0442\u043a\u043b\u044e\u0447\u0438\u043b \u044d\u0442\u0443 \u0447\u0430\u0441\u0442\u044c \u0432 \u0446\u0435\u043b\u044f\u0445 \u0431\u0435\u0437\u043e\u043f\u0430\u0441\u043d\u043e\u0441\u0442\u0438. "
        "\u041f\u0440\u043e\u0432\u0435\u0440\u044c\u0442\u0435 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0430\u0434\u0434\u043e\u043d\u0430.",
        "dialog_title": "Hider",
        "group_review": "\u0412\u043e \u0432\u0440\u0435\u043c\u044f \u043f\u043e\u0432\u0442\u043e\u0440\u0435\u043d\u0438\u044f \u0441\u043a\u0440\u044b\u0432\u0430\u0442\u044c:",
        "group_behaviour": "\u041f\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u0435",
        "opt_menu_bar": "\u0421\u0442\u0440\u043e\u043a\u0443 \u043c\u0435\u043d\u044e (\u0424\u0430\u0439\u043b, \u041f\u0440\u0430\u0432\u043a\u0430, \u0418\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u044b...)",
        "opt_menu_bar_tip": "\u041f\u043e\u044f\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u0441\u043d\u043e\u0432\u0430, \u043a\u0430\u043a \u0442\u043e\u043b\u044c\u043a\u043e \u0432\u044b \u0432\u044b\u0439\u0434\u0435\u0442\u0435 \u0438\u0437 \u043f\u043e\u0432\u0442\u043e\u0440\u0435\u043d\u0438\u044f.",
        "opt_toolbar": "\u0412\u0435\u0440\u0445\u043d\u044e\u044e \u043f\u0430\u043d\u0435\u043b\u044c (\u041a\u043e\u043b\u043e\u0434\u044b, \u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c, \u041e\u0431\u0437\u043e\u0440, \u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430)",
        "opt_toolbar_tip": "\u041f\u043e\u044f\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u0441\u043d\u043e\u0432\u0430, \u043a\u0430\u043a \u0442\u043e\u043b\u044c\u043a\u043e \u0432\u044b \u0432\u044b\u0439\u0434\u0435\u0442\u0435 \u0438\u0437 \u043f\u043e\u0432\u0442\u043e\u0440\u0435\u043d\u0438\u044f.",
        "opt_bottom_bar": "\u041d\u0438\u0436\u043d\u044e\u044e \u043f\u0430\u043d\u0435\u043b\u044c \u043e\u043a\u043d\u0430",
        "opt_bottom_bar_tip": "\u041f\u043e\u044f\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u0441\u043d\u043e\u0432\u0430, \u043a\u0430\u043a \u0442\u043e\u043b\u044c\u043a\u043e \u0432\u044b \u0432\u044b\u0439\u0434\u0435\u0442\u0435 \u0438\u0437 \u043f\u043e\u0432\u0442\u043e\u0440\u0435\u043d\u0438\u044f.",
        "opt_scrollbar": "\u041f\u043e\u043b\u043e\u0441\u0443 \u043f\u0440\u043e\u043a\u0440\u0443\u0442\u043a\u0438 \u043a\u0430\u0440\u0442\u043e\u0447\u043a\u0438",
        "opt_scrollbar_tip": "\u0422\u043e\u043b\u044c\u043a\u043e \u0432\u0438\u0437\u0443\u0430\u043b\u044c\u043d\u043e: \u043f\u0440\u043e\u043a\u0440\u0443\u0447\u0438\u0432\u0430\u0442\u044c \u043a\u043e\u043b\u0435\u0441\u0438\u043a\u043e\u043c \u043c\u044b\u0448\u0438 \u0432\u0441\u0451 \u0440\u0430\u0432\u043d\u043e \u043c\u043e\u0436\u043d\u043e. "
        "\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u0437\u0430\u043c\u0435\u0442\u043d\u043e \u043d\u0430 \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0435\u0439 \u043a\u0430\u0440\u0442\u043e\u0447\u043a\u0435.",
        "opt_hard_easy": "\u041a\u043d\u043e\u043f\u043a\u0438 \u00ab\u0421\u043b\u043e\u0436\u043d\u043e\u00bb \u0438 \u00ab\u041b\u0435\u0433\u043a\u043e\u00bb",
        "opt_hard_easy_tip": "\u041e\u0441\u0442\u0430\u0432\u043b\u044f\u0435\u0442 \u0442\u043e\u043b\u044c\u043a\u043e \u00ab\u0417\u0430\u0431\u044b\u043b\u00bb \u0438 \u00ab\u0425\u043e\u0440\u043e\u0448\u043e\u00bb. \u0413\u043e\u0440\u044f\u0447\u0438\u0435 \u043a\u043b\u0430\u0432\u0438\u0448\u0438 \u0442\u0430\u043a\u0436\u0435 "
        "\u0431\u043b\u043e\u043a\u0438\u0440\u0443\u044e\u0442\u0441\u044f, \u0447\u0442\u043e\u0431\u044b \u0432\u044b \u0441\u043b\u0443\u0447\u0430\u0439\u043d\u043e \u043d\u0435 \u043e\u0442\u0432\u0435\u0442\u0438\u043b\u0438 \u043d\u0435\u0432\u0438\u0434\u0438\u043c\u043e\u0439 \u043a\u043d\u043e\u043f\u043a\u043e\u0439.",
        "opt_cursor": "\u041a\u0443\u0440\u0441\u043e\u0440 \u043c\u044b\u0448\u0438 \u043f\u0440\u0438 \u043d\u0435\u043f\u043e\u0434\u0432\u0438\u0436\u043d\u043e\u0441\u0442\u0438 \u0431\u043e\u043b\u0435\u0435:",
        "opt_cursor_tip": "\u041f\u043e\u044f\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u0441\u043d\u043e\u0432\u0430, \u043a\u0430\u043a \u0442\u043e\u043b\u044c\u043a\u043e \u0432\u044b \u0434\u0432\u0438\u0433\u0430\u0435\u0442\u0435 \u043c\u044b\u0448\u044c\u044e.",
        "opt_cursor_suffix": " \u0441",
        "opt_auto_start": "\u0410\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438 \u043d\u0430\u0447\u0438\u043d\u0430\u0442\u044c \u043f\u043e\u0432\u0442\u043e\u0440\u0435\u043d\u0438\u0435 \u043f\u0440\u0438 \u043e\u0442\u043a\u0440\u044b\u0442\u0438\u0438 \u043a\u043e\u043b\u043e\u0434\u044b",
        "opt_auto_start_tip": "\u0422\u043e\u043b\u044c\u043a\u043e \u0435\u0441\u043b\u0438 \u0435\u0441\u0442\u044c \u043a\u0430\u0440\u0442\u043e\u0447\u043a\u0438 \u043a \u043f\u043e\u0432\u0442\u043e\u0440\u0435\u043d\u0438\u044e. \u0415\u0441\u043b\u0438 \u0432\u044b \u0441\u0430\u043c\u0438 \u0432\u044b\u0448\u043b\u0438 \u0438\u0437 \u043f\u043e\u0432\u0442\u043e\u0440\u0435\u043d\u0438\u044f, "
        "Hider \u043d\u0435 \u0432\u0435\u0440\u043d\u0451\u0442 \u0432\u0430\u0441 \u043e\u0431\u0440\u0430\u0442\u043d\u043e.",
        "btn_save": "Принять",
        "btn_cancel": "\u041e\u0442\u043c\u0435\u043d\u0430",
        "btn_defaults": "Восстановить значения по умолчанию",
        "saved": "\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 Hider \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u044b.",
        "save_failed": "\u041d\u0435 \u0443\u0434\u0430\u043b\u043e\u0441\u044c \u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 Hider.",
    },
    "uk": {
        "button_hidden": "\u0426\u044f \u043a\u043d\u043e\u043f\u043a\u0430 \u043f\u0440\u0438\u0445\u043e\u0432\u0430\u043d\u0430. \u041c\u043e\u0436\u043d\u0430 \u0432\u0456\u0434\u043f\u043e\u0432\u0456\u0441\u0442\u0438 \u043b\u0438\u0448\u0435 \u00ab\u0417\u043d\u043e\u0432\u0443\u00bb \u0430\u0431\u043e \u00ab\u0414\u043e\u0431\u0440\u0435\u00bb.",
        "hook_error": "Hider \u0437\u0456\u0442\u043a\u043d\u0443\u0432\u0441\u044f \u0437 \u043f\u0440\u043e\u0431\u043b\u0435\u043c\u043e\u044e \u0456 \u0432\u0438\u043c\u043a\u043d\u0443\u0432 \u0446\u044e \u0447\u0430\u0441\u0442\u0438\u043d\u0443 \u0437 \u043c\u0456\u0440\u043a\u0443\u0432\u0430\u043d\u044c \u0431\u0435\u0437\u043f\u0435\u043a\u0438. "
        "\u041f\u0435\u0440\u0435\u0432\u0456\u0440\u0442\u0435 \u043d\u0430\u043b\u0430\u0448\u0442\u0443\u0432\u0430\u043d\u043d\u044f \u0434\u043e\u0434\u0430\u0442\u043a\u0430.",
        "dialog_title": "Hider",
        "group_review": "\u041f\u0456\u0434 \u0447\u0430\u0441 \u043f\u043e\u0432\u0442\u043e\u0440\u0435\u043d\u043d\u044f \u043f\u0440\u0438\u0445\u043e\u0432\u0443\u0432\u0430\u0442\u0438:",
        "group_behaviour": "\u041f\u043e\u0432\u0435\u0434\u0456\u043d\u043a\u0430",
        "opt_menu_bar": "\u041f\u0430\u043d\u0435\u043b\u044c \u043c\u0435\u043d\u044e (\u0424\u0430\u0439\u043b, \u0420\u0435\u0434\u0430\u0433\u0443\u0432\u0430\u0442\u0438, \u0406\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u0438...)",
        "opt_menu_bar_tip": "\u0417\u043d\u043e\u0432\u0443 з'\u044f\u0432\u043b\u044f\u0454\u0442\u044c\u0441\u044f, \u0449\u043e\u0439\u043d\u043e \u0432\u0438 \u0432\u0438\u0439\u0434\u0435\u0442\u0435 \u0437 \u043f\u043e\u0432\u0442\u043e\u0440\u0435\u043d\u043d\u044f.",
        "opt_toolbar": "\u0412\u0435\u0440\u0445\u043d\u044e \u043f\u0430\u043d\u0435\u043b\u044c (\u041a\u043e\u043b\u043e\u0434\u0438, \u0414\u043e\u0434\u0430\u0442\u0438, \u041e\u0433\u043b\u044f\u0434, \u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430)",
        "opt_toolbar_tip": "\u0417\u043d\u043e\u0432\u0443 з'\u044f\u0432\u043b\u044f\u0454\u0442\u044c\u0441\u044f, \u0449\u043e\u0439\u043d\u043e \u0432\u0438 \u0432\u0438\u0439\u0434\u0435\u0442\u0435 \u0437 \u043f\u043e\u0432\u0442\u043e\u0440\u0435\u043d\u043d\u044f.",
        "opt_bottom_bar": "\u041d\u0438\u0436\u043d\u044e \u043f\u0430\u043d\u0435\u043b\u044c \u0432\u0456\u043a\u043d\u0430",
        "opt_bottom_bar_tip": "\u0417\u043d\u043e\u0432\u0443 з'\u044f\u0432\u043b\u044f\u0454\u0442\u044c\u0441\u044f, \u0449\u043e\u0439\u043d\u043e \u0432\u0438 \u0432\u0438\u0439\u0434\u0435\u0442\u0435 \u0437 \u043f\u043e\u0432\u0442\u043e\u0440\u0435\u043d\u043d\u044f.",
        "opt_scrollbar": "\u041f\u043e\u043b\u043e\u0441\u0443 \u043f\u0440\u043e\u043a\u0440\u0443\u0447\u0443\u0432\u0430\u043d\u043d\u044f \u043a\u0430\u0440\u0442\u043a\u0438",
        "opt_scrollbar_tip": "\u041b\u0438\u0448\u0435 \u0432\u0456\u0437\u0443\u0430\u043b\u044c\u043d\u043e: \u043c\u043e\u0436\u043d\u0430 \u0439 \u0434\u0430\u043b\u0456 \u043f\u0440\u043e\u043a\u0440\u0443\u0447\u0443\u0432\u0430\u0442\u0438 \u043a\u043e\u043b\u0456\u0441\u0446\u0435\u043c \u043c\u0438\u0448\u0456. "
        "\u0417\u043c\u0456\u043d\u0430 \u043f\u043e\u043c\u0456\u0442\u043d\u0430 \u043d\u0430 \u043d\u0430\u0441\u0442\u0443\u043f\u043d\u0456\u0439 \u043a\u0430\u0440\u0442\u0446\u0456.",
        "opt_hard_easy": "\u041a\u043d\u043e\u043f\u043a\u0438 \u00ab\u0412\u0430\u0436\u043a\u043e\u00bb \u0456 \u00ab\u041b\u0435\u0433\u043a\u043e\u00bb",
        "opt_hard_easy_tip": "\u0417\u0430\u043b\u0438\u0448\u0430\u0454 \u043b\u0438\u0448\u0435 \u00ab\u0417\u043d\u043e\u0432\u0443\u00bb \u0456 \u00ab\u0414\u043e\u0431\u0440\u0435\u00bb. \u0413\u0430\u0440\u044f\u0447\u0456 \u043a\u043b\u0430\u0432\u0456\u0448\u0456 \u0442\u0430\u043a\u043e\u0436 "
        "\u0431\u043b\u043e\u043a\u0443\u044e\u0442\u044c\u0441\u044f, \u0449\u043e\u0431 \u0432\u0438 \u0432\u0438\u043f\u0430\u0434\u043a\u043e\u0432\u043e \u043d\u0435 \u0432\u0456\u0434\u043f\u043e\u0432\u0456\u043b\u0438 \u043d\u0435\u0432\u0438\u0434\u0438\u043c\u043e\u044e \u043a\u043d\u043e\u043f\u043a\u043e\u044e.",
        "opt_cursor": "\u041a\u0443\u0440\u0441\u043e\u0440 \u043c\u0438\u0448\u0456 \u043f\u0440\u0438 \u043d\u0435\u0440\u0443\u0445\u043e\u043c\u043e\u0441\u0442\u0456 \u043f\u043e\u043d\u0430\u0434:",
        "opt_cursor_tip": "\u0417\u043d\u043e\u0432\u0443 з'\u044f\u0432\u043b\u044f\u0454\u0442\u044c\u0441\u044f, \u0449\u043e\u0439\u043d\u043e \u0432\u0438 \u0440\u0443\u0445\u0430\u0454\u0442\u0435 \u043c\u0438\u0448\u0448\u044e.",
        "opt_cursor_suffix": " \u0441",
        "opt_auto_start": "\u0410\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u043d\u043e \u043f\u043e\u0447\u0438\u043d\u0430\u0442\u0438 \u043f\u043e\u0432\u0442\u043e\u0440\u0435\u043d\u043d\u044f \u043f\u0440\u0438 \u0432\u0456\u0434\u043a\u0440\u0438\u0442\u0442\u0456 \u043a\u043e\u043b\u043e\u0434\u0438",
        "opt_auto_start_tip": "\u041b\u0438\u0448\u0435 \u044f\u043a\u0449\u043e \u0454 \u043a\u0430\u0440\u0442\u043a\u0438 \u0434\u043e \u043f\u043e\u0432\u0442\u043e\u0440\u0435\u043d\u043d\u044f. \u042f\u043a\u0449\u043e \u0432\u0438 \u0441\u0430\u043c\u0456 \u0432\u0438\u0439\u0434\u0435\u0442\u0435 \u0437 \u043f\u043e\u0432\u0442\u043e\u0440\u0435\u043d\u043d\u044f, "
        "Hider \u043d\u0435 \u043f\u043e\u0432\u0435\u0440\u043d\u0435 \u0432\u0430\u0441 \u043d\u0430\u0437\u0430\u0434.",
        "btn_save": "Прийняти",
        "btn_cancel": "\u0421\u043a\u0430\u0441\u0443\u0432\u0430\u0442\u0438",
        "btn_defaults": "Відновити типові значення",
        "saved": "\u041d\u0430\u043b\u0430\u0448\u0442\u0443\u0432\u0430\u043d\u043d\u044f Hider \u0437\u0431\u0435\u0440\u0435\u0436\u0435\u043d\u043e.",
        "save_failed": "\u041d\u0435 \u0432\u0434\u0430\u043b\u043e\u0441\u044f \u0437\u0431\u0435\u0440\u0435\u0433\u0442\u0438 \u043d\u0430\u043b\u0430\u0448\u0442\u0443\u0432\u0430\u043d\u043d\u044f Hider.",
    },
    "pl": {
        "button_hidden": "Ten przycisk jest ukryty. Mo\u017cesz odpowiedzie\u0107 tylko \u00abJeszcze raz\u00bb lub \u00abDobrze\u00bb.",
        "hook_error": "Hider napotka\u0142 problem i wy\u0142\u0105czy\u0142 t\u0119 cz\u0119\u015b\u0107 dla bezpiecze\u0144stwa. "
        "Sprawd\u017a konfiguracj\u0119 dodatku.",
        "dialog_title": "Hider",
        "group_review": "Podczas powtarzania ukryj:",
        "group_behaviour": "Zachowanie",
        "opt_menu_bar": "Pasek menu (Plik, Edycja, Narz\u0119dzia...)",
        "opt_menu_bar_tip": "Pojawia si\u0119 ponownie zaraz po opuszczeniu powtarzania.",
        "opt_toolbar": "G\u00f3rny pasek narz\u0119dzi (Talie, Dodaj, Przegl\u0105daj, Statystyki)",
        "opt_toolbar_tip": "Pojawia si\u0119 ponownie zaraz po opuszczeniu powtarzania.",
        "opt_bottom_bar": "Dolny pasek okna",
        "opt_bottom_bar_tip": "Pojawia si\u0119 ponownie zaraz po opuszczeniu powtarzania.",
        "opt_scrollbar": "Pasek przewijania karty",
        "opt_scrollbar_tip": "Tylko wizualnie: nadal mo\u017cna przewija\u0107 k\u00f3\u0142kiem myszy. "
        "Zmiana widoczna jest na kolejnej karcie.",
        "opt_hard_easy": "Przyciski \u00abTrudne\u00bb i \u00abLatwe\u00bb",
        "opt_hard_easy_tip": "Zostawia tylko \u00abJeszcze raz\u00bb i \u00abDobrze\u00bb. Ich skr\u00f3ty klawiszowe s\u0105 "
        "r\u00f3wnie\u017c zablokowane, aby\u015b nie odpowiedzia\u0142 przypadkowo niewidocznym przyciskiem.",
        "opt_cursor": "Kursor myszy po bezczynno\u015bci przez:",
        "opt_cursor_tip": "Pojawia si\u0119 ponownie zaraz po poruszeniu myszy\u0105.",
        "opt_cursor_suffix": " s",
        "opt_auto_start": "Automatycznie rozpocznij powtarzanie po otwarciu talii",
        "opt_auto_start_tip": "Tylko je\u015bli s\u0105 zaleg\u0142e karty. Je\u015bli sam opu\u015bcisz powtarzanie, "
        "Hider nie wci\u0105gnie ci\u0119 z powrotem.",
        "btn_save": "Akceptuj",
        "btn_cancel": "Anuluj",
        "btn_defaults": "Przywróć wartości domyślne",
        "saved": "Konfiguracja Hider zapisana.",
        "save_failed": "Nie uda\u0142o si\u0119 zapisa\u0107 konfiguracji Hider.",
    },
    "cs": {
        "button_hidden": "Toto tla\u010d\u00edtko je skryt\u00e9. M\u016f\u017eete odpov\u011bd\u011bt pouze \u00abZnovu\u00bb nebo \u00abDobr\u00e9\u00bb.",
        "hook_error": "Hider narazil na probl\u00e9m a tuto \u010d\u00e1st z bezpe\u010dnostn\u00edch d\u016fvod\u016f vypnul. "
        "Zkontrolujte nastaven\u00ed doplňku.",
        "dialog_title": "Hider",
        "group_review": "B\u011bhem opakov\u00e1n\u00ed skr\u00fdt:",
        "group_behaviour": "Chov\u00e1n\u00ed",
        "opt_menu_bar": "Panel nab\u00eddek (Soubor, Upravit, N\u00e1stroje...)",
        "opt_menu_bar_tip": "Znovu se objev\u00ed, jakmile opust\u00edte opakov\u00e1n\u00ed.",
        "opt_toolbar": "Horn\u00ed panel n\u00e1stroj\u016f (Bal\u00ed\u010dky, P\u0159idat, Proch\u00e1zet, Statistiky)",
        "opt_toolbar_tip": "Znovu se objev\u00ed, jakmile opust\u00edte opakov\u00e1n\u00ed.",
        "opt_bottom_bar": "Spodn\u00ed li\u0161ta okna",
        "opt_bottom_bar_tip": "Znovu se objev\u00ed, jakmile opust\u00edte opakov\u00e1n\u00ed.",
        "opt_scrollbar": "Posuvn\u00edk kartu",
        "opt_scrollbar_tip": "Pouze vizu\u00e1ln\u011b: st\u00e1le m\u016f\u017eete posouvat kole\u010dkem my\u0161i. "
        "Zm\u011bna se projev\u00ed na dal\u0161\u00ed kart\u011b.",
        "opt_hard_easy": "Tla\u010d\u00edtka \u00abT\u011b\u017ek\u00e9\u00bb a \u00abLehk\u00e9\u00bb",
        "opt_hard_easy_tip": "Ponech\u00e1 pouze \u00abZnovu\u00bb a \u00abDobr\u00e9\u00bb. Jejich kl\u00e1vesov\u00e9 zkratky jsou "
        "tak\u00e9 zablokov\u00e1ny, abyste omylem neodpov\u011bd\u011bli tla\u010d\u00edtkem, kter\u00e9 nevid\u00edte.",
        "opt_cursor": "Ukazatel my\u0161i, kdy\u017e je nehybn\u00fd po dobu:",
        "opt_cursor_tip": "Znovu se objev\u00ed, jakmile pohnete my\u0161\u00ed.",
        "opt_cursor_suffix": " s",
        "opt_auto_start": "Automaticky zah\u00e1jit opakov\u00e1n\u00ed p\u0159i otev\u0159en\u00ed bal\u00ed\u010dku",
        "opt_auto_start_tip": "Pouze pokud jsou k dispozici karty. Pokud opakov\u00e1n\u00ed opust\u00edte sami, "
        "Hider v\u00e1s zp\u011bt nevr\u00e1t\u00ed.",
        "btn_save": "Přijmout",
        "btn_cancel": "Zru\u0161it",
        "btn_defaults": "Obnovit výchozí hodnoty",
        "saved": "Konfigurace Hider ulo\u017eena.",
        "save_failed": "Konfiguraci Hider se nepoda\u0159ilo ulo\u017eit.",
    },
    "sk": {
        "button_hidden": "T\u00e9to tla\u010didlo je skryt\u00e9. M\u00f4\u017eete odpoveda\u0165 iba \u00abZnova\u00bb alebo \u00abDobre\u00bb.",
        "hook_error": "Hider narazil na probl\u00e9m a t\u00fato \u010das\u0165 z bezpe\u010dnostn\u00fdch d\u00f4vodov vypol. "
        "Skontrolujte nastavenia doplnku.",
        "dialog_title": "Hider",
        "group_review": "Po\u010das opakovania skry\u0165:",
        "group_behaviour": "Spr\u00e1vanie",
        "opt_menu_bar": "Panel pon\u00fak (S\u00fabor, Upravi\u0165, N\u00e1stroje...)",
        "opt_menu_bar_tip": "Znova sa objav\u00ed, hne\u010f ako opust\u00edte opakovanie.",
        "opt_toolbar": "Horn\u00fd panel n\u00e1strojov (Bal\u00edky, Prida\u0165, Prehliada\u0165, \u0160tatistiky)",
        "opt_toolbar_tip": "Znova sa objav\u00ed, hne\u010f ako opust\u00edte opakovanie.",
        "opt_bottom_bar": "Doln\u00fd panel okna",
        "opt_bottom_bar_tip": "Znova sa objav\u00ed, hne\u010f ako opust\u00edte opakovanie.",
        "opt_scrollbar": "Posuvn\u00edk kartu",
        "opt_scrollbar_tip": "Iba vizu\u00e1lne: st\u00e1le m\u00f4\u017eete posiel\u00e1 kolieskom my\u0161i. "
        "Zmena sa prejav\u00ed na \u010fal\u0161ej karte.",
        "opt_hard_easy": "Tla\u010didl\u00e1 \u00abT\u0159a\u017ek\u00e9\u00bb a \u00abLahk\u00e9\u00bb",
        "opt_hard_easy_tip": "Ponech\u00e1 iba \u00abZnova\u00bb a \u00abDobre\u00bb. Ich kl\u00e1vesov\u00e9 skratky s\u00fa "
        "tie\u017e zablokovan\u00e9, aby ste omylom neodpovedali tla\u010didlom, ktor\u00e9 nevid\u00edte.",
        "opt_cursor": "Kurzor my\u0161i, ke\u010f je nehybn\u00fd po dobu:",
        "opt_cursor_tip": "Znova sa objav\u00ed, hne\u010f ako pohnete my\u0161ou.",
        "opt_cursor_suffix": " s",
        "opt_auto_start": "Automaticky za\u010da\u0165 opakovanie pri otvoren\u00ed bal\u00edka",
        "opt_auto_start_tip": "Iba ak s\u00fa k dispoz\u00edcii karty. Ak opakovanie opust\u00edte sami, "
        "Hider v\u00e1s sp\u00e4\u0165 nevr\u00e1ti.",
        "btn_save": "Prijať",
        "btn_cancel": "Zru\u0161i\u0165",
        "btn_defaults": "Obnoviť predvolené hodnoty",
        "saved": "Konfigur\u00e1cia Hider ulo\u017een\u00e1.",
        "save_failed": "Konfigur\u00e1ciu Hider sa nepodarilo ulo\u017ei\u0165.",
    },
    "sl": {
        "button_hidden": "Ta gumb je skrit. Odgovoriti mora\u0161 lahko le z \u00abPonovno\u00bb ali \u00abDobro\u00bb.",
        "hook_error": "Hider je naletel na te\u017eavo in je ta del zaradi varnosti onemogo\u010dil. "
        "Preverite nastavitve dodatka.",
        "dialog_title": "Hider",
        "group_review": "Med ponavljanjem skrij:",
        "group_behaviour": "Obna\u0161anje",
        "opt_menu_bar": "Vrstica menija (Datoteka, Uredi, Orodja...)",
        "opt_menu_bar_tip": "Znova se prika\u017ee, takoj ko zapusti\u0161 ponavljanje.",
        "opt_toolbar": "Zgornja orodna vrstica (Kupi, Dodaj, Prebrskaj, Statistika)",
        "opt_toolbar_tip": "Znova se prika\u017ee, takoj ko zapusti\u0161 ponavljanje.",
        "opt_bottom_bar": "Spodnja vrstica okna",
        "opt_bottom_bar_tip": "Znova se prika\u017ee, takoj ko zapusti\u0161 ponavljanje.",
        "opt_scrollbar": "Drsnik kartice",
        "opt_scrollbar_tip": "Samo vizualno: \u0161e vedno lahko drsi\u0161 s kolescem mi\u0161ke. "
        "Sprememba se pozna na naslednji kartici.",
        "opt_hard_easy": "Gumba \u00abTe\u017eko\u00bb in \u00abLahko\u00bb",
        "opt_hard_easy_tip": "Pusti le \u00abPonovno\u00bb in \u00abDobro\u00bb. Njuni bli\u017enjici na tipkovnici sta "
        "prav tako blokirani, da po nesre\u010di ne odgovori\u0161 z gumbom, ki ga ne vidi\u0161.",
        "opt_cursor": "Ka\u017eipuc mi\u0161ke, ko je nepremi\u010den:",
        "opt_cursor_tip": "Znova se prika\u017ee, takoj ko premakne\u0161 mi\u0161ko.",
        "opt_cursor_suffix": " s",
        "opt_auto_start": "Samodejno za\u010dni ponavljanje ob odprtju kupa",
        "opt_auto_start_tip": "Le \u010de so na voljo kartice. \u010ce sam zapusti\u0161 ponavljanje, "
        "te Hider ne vrne nazaj.",
        "btn_save": "Sprejmi",
        "btn_cancel": "Prekli\u010di",
        "btn_defaults": "Obnovi privzete vrednosti",
        "saved": "Nastavitve Hider shranjene.",
        "save_failed": "Nastavitev Hider ni bilo mogo\u010de shraniti.",
    },
    "hr": {
        "button_hidden": "Ta tipka je skrivena. Mo\u017ee\u0161 odgovoriti samo \u00abPonovno\u00bb ili \u00abDobro\u00bb.",
        "hook_error": "Hider je naletio na problem i iz sigurnosnih razloga onemogu\u0107io taj dio. "
        "Provjeri postavke dodatka.",
        "dialog_title": "Hider",
        "group_review": "Tijekom ponavljanja skrij:",
        "group_behaviour": "Pona\u0161anje",
        "opt_menu_bar": "Traka izbornika (Datoteka, Uredi, Alati...)",
        "opt_menu_bar_tip": "Ponovno se pojavljuje \u010dim napusti\u0161 ponavljanje.",
        "opt_toolbar": "Gornja alatna traka (Spremnici, Dodaj, Pregledaj, Statistika)",
        "opt_toolbar_tip": "Ponovno se pojavljuje \u010dim napusti\u0161 ponavljanje.",
        "opt_bottom_bar": "Donja traka prozora",
        "opt_bottom_bar_tip": "Ponovno se pojavljuje \u010dim napusti\u0161 ponavljanje.",
        "opt_scrollbar": "Traka za pomicanje kartice",
        "opt_scrollbar_tip": "Samo vizualno: i dalje mo\u017ee\u0161 pomicati kota\u010di\u0107em mi\u0161a. "
        "Promjena se vidi na sljede\u0107oj kartici.",
        "opt_hard_easy": "Tipke \u00abTe\u0161ko\u00bb i \u00abLagano\u00bb",
        "opt_hard_easy_tip": "Ostavlja samo \u00abPonovno\u00bb i \u00abDobro\u00bb. Njihove tipkovni\u010dke pre\u010dice su "
        "tako\u0111er blokirane, kako slu\u010dajno ne bi odgovorio tipkom koju ne vidi\u0161.",
        "opt_cursor": "Pokaziva\u010d mi\u0161a kada je nepomi\u010dan:",
        "opt_cursor_tip": "Ponovno se pojavljuje \u010dim pomakne\u0161 mi\u0161.",
        "opt_cursor_suffix": " s",
        "opt_auto_start": "Automatski zapo\u010dni ponavljanje pri otvaranju spremnika",
        "opt_auto_start_tip": "Samo ako ima kartica na redu. Ako sam napusti\u0161 ponavljanje, "
        "Hider te ne vra\u0107a natrag.",
        "btn_save": "Prihvati",
        "btn_cancel": "Odustani",
        "btn_defaults": "Vrati zadane vrijednosti",
        "saved": "Postavke Hidera spremljene.",
        "save_failed": "Postavke Hidera nije mogu\u0107e spremiti.",
    },
    "sr": {
        "button_hidden": "\u0422\u043e \u0434\u0443\u0433\u043c\u0435 \u0458\u0435 \u0441\u0430\u043a\u0440\u0438\u0432\u0435\u043d\u043e. \u041c\u043e\u0436\u0435\u0448 \u043e\u0434\u0433\u043e\u0432\u043e\u0440\u0438\u0442\u0438 \u0441\u0430\u043c\u043e \u00ab\u041f\u043e\u043d\u043e\u0432\u043e\u00bb \u0438\u043b\u0438 \u00ab\u0414\u043e\u0431\u0440\u043e\u00bb.",
        "hook_error": "Hider \u0458\u0435 \u043d\u0430\u0438\u0448\u0430\u043e \u043d\u0430 \u043f\u0440\u043e\u0431\u043b\u0435\u043c \u0438 \u0438\u0437 \u0431\u0435\u0437\u0431\u0435\u0434\u043d\u043e\u0441\u043d\u0438\u0445 \u0440\u0430\u0437\u043b\u043e\u0433\u0430 \u043e\u043d\u0435\u043c\u043e\u0433\u0443\u045b\u0438\u043e \u0442\u0430\u0458 \u0434\u0435\u043e. "
        "\u041f\u0440\u043e\u0432\u0435\u0440\u0438 \u043f\u043e\u0434\u0435\u0448\u0430\u0432\u0430\u045a\u0430 \u0434\u043e\u0434\u0430\u0442\u043a\u0430.",
        "dialog_title": "Hider",
        "group_review": "\u0422\u043e\u043a\u043e\u043c \u043f\u043e\u043d\u0430\u0432\u0459\u0430\u045a\u0430, \u0441\u0430\u043a\u0440\u0438\u0458:",
        "group_behaviour": "\u041f\u043e\u043d\u0430\u0448\u0430\u045a\u0435",
        "opt_menu_bar": "\u0422\u0440\u0430\u043a\u0430 \u0438\u0437\u0431\u043e\u0440\u043d\u0438\u043a\u0430 (\u0424\u0430\u0458\u043b, \u0418\u0437\u043c\u0435\u043d\u0438, \u0410\u043b\u0430\u0442\u0438...)",
        "opt_menu_bar_tip": "\u041f\u043e\u043d\u043e\u0432\u043e \u0441\u0435 \u043f\u043e\u0458\u0430\u0432\u0459\u0443\u0458\u0435 \u0447\u0438\u043c \u043d\u0430\u043f\u0443\u0441\u0442\u0438\u0448 \u043f\u043e\u043d\u0430\u0432\u0459\u0430\u045a\u0435.",
        "opt_toolbar": "Горња алатна трака (Шпилови, Додај, Прегледај, Статистика)",
        "opt_toolbar_tip": "Поново се појављује чим напустиш понављање.",
        "opt_bottom_bar": "\u0414\u043e\u045a\u0430 \u0442\u0440\u0430\u043a\u0430 \u043f\u0440\u043e\u0437\u043e\u0440\u0430",
        "opt_bottom_bar_tip": "\u041f\u043e\u043d\u043e\u0432\u043e \u0441\u0435 \u043f\u043e\u0458\u0430\u0432\u0459\u0443\u0458\u0435 \u0447\u0438\u043c \u043d\u0430\u043f\u0443\u0441\u0442\u0438\u0448 \u043f\u043e\u043d\u0430\u0432\u0459\u0430\u045a\u0435.",
        "opt_scrollbar": "\u0422\u0440\u0430\u043a\u0430 \u0437\u0430 \u043f\u043e\u043c\u0435\u0440\u0430\u045a\u0435 \u043a\u0430\u0440\u0442\u0438\u0446\u0435",
        "opt_scrollbar_tip": "\u0421\u0430\u043c\u043e \u0432\u0438\u0437\u0443\u0435\u043b\u043d\u043e: \u0438 \u0434\u0430\u0459\u0435 \u043c\u043e\u0436\u0435\u0448 \u043f\u043e\u043c\u0435\u0440\u0430\u0442\u0438 \u0442\u043e\u0447\u043a\u0438\u045b\u0435\u043c \u043c\u0438\u0448\u0430. "
        "\u041f\u0440\u043e\u043c\u0435\u043d\u0430 \u0441\u0435 \u0432\u0438\u0434\u0438 \u043d\u0430 \u0441\u043b\u0435\u0434\u0435\u045b\u043e\u0458 \u043a\u0430\u0440\u0442\u0438\u0446\u0438.",
        "opt_hard_easy": "\u0414\u0443\u0433\u043c\u0430\u0434\u0438 \u00ab\u0422\u0435\u0448\u043a\u043e\u00bb \u0438 \u00ab\u041b\u0430\u043a\u043e\u00bb",
        "opt_hard_easy_tip": "\u041e\u0441\u0442\u0430\u0432\u0459\u0430 \u0441\u0430\u043c\u043e \u00ab\u041f\u043e\u043d\u043e\u0432\u043e\u00bb \u0438 \u00ab\u0414\u043e\u0431\u0440\u043e\u00bb. \u0418 \u045a\u0438\u0445\u043e\u0432\u0435 \u043f\u0440\u0435\u0447\u0438\u0446\u0435 \u043d\u0430 \u0442\u0430\u0441\u0442\u0430\u0442\u0443\u0440\u0438 \u0441\u0443 "
        "\u0442\u0430\u043a\u043e\u0453\u0435 \u0431\u043b\u043e\u043a\u0438\u0440\u0430\u043d\u0435, \u0434\u0430 \u0441\u043b\u0443\u0447\u0430\u0458\u043d\u043e \u043d\u0435 \u043e\u0434\u0433\u043e\u0432\u043e\u0440\u0438\u0448 \u0434\u0443\u0433\u043c\u0435\u0442\u043e\u043c \u043a\u043e\u0458\u0438 \u043d\u0435 \u0432\u0438\u0434\u0438\u0448.",
        "opt_cursor": "\u041f\u043e\u043a\u0430\u0437\u0438\u0432\u0430\u0447 \u043c\u0438\u0448\u0430 \u043a\u0430\u0434\u0430 \u043c\u0438\u0440\u0443\u0458\u0435 \u0434\u0443\u0436\u0435 \u043e\u0434:",
        "opt_cursor_tip": "\u041f\u043e\u043d\u043e\u0432\u043e \u0441\u0435 \u043f\u043e\u0458\u0430\u0432\u0459\u0443\u0458\u0435 \u0447\u0438\u043c \u043f\u043e\u043c\u0435\u0440\u0438\u0448 \u043c\u0438\u0448\u0430.",
        "opt_cursor_suffix": " \u0441",
        "opt_auto_start": "\u0410\u0443\u0442\u043e\u043c\u0430\u0442\u0441\u043a\u0438 \u0437\u0430\u043f\u043e\u0447\u043d\u0438 \u043f\u043e\u043d\u0430\u0432\u0459\u0430\u045a\u0435 \u043f\u0440\u0438 \u043e\u0442\u0432\u0430\u0440\u0430\u045a\u0443 \u0448\u043f\u0438\u043b\u0430",
        "opt_auto_start_tip": "\u0421\u0430\u043c\u043e \u0430\u043a\u043e \u043f\u043e\u0441\u0442\u043e\u0458\u0435 \u043a\u0430\u0440\u0442\u0438\u0446\u0435 \u043d\u0430 \u0440\u0435\u0434\u0443. \u0410\u043a\u043e \u0441\u0430\u043c \u043d\u0430\u043f\u0443\u0441\u0442\u0438\u0448 \u043f\u043e\u043d\u0430\u0432\u0459\u0430\u045a\u0435, "
        "Hider \u0442\u0435 \u043d\u0435 \u0432\u0440\u0430\u045b\u0430 \u043d\u0430\u0437\u0430\u0434.",
        "btn_save": "Прихвати",
        "btn_cancel": "\u041e\u0442\u043a\u0430\u0436\u0438",
        "btn_defaults": "Врати подразумеване вредности",
        "saved": "\u041f\u043e\u0434\u0435\u0448\u0430\u0432\u0430\u045a\u0430 Hider-\u0430 \u0441\u0430\u0447\u0443\u0432\u0430\u043d\u0430.",
        "save_failed": "\u041d\u0435 \u043c\u043e\u0433\u0443 \u0434\u0430 \u0441\u0430\u0447\u0443\u0432\u0430\u043c \u043f\u043e\u0434\u0435\u0448\u0430\u0432\u0430\u045a\u0430 Hider-\u0430.",
    },
    "bg": {
        "button_hidden": "\u0422\u043e\u0437\u0438 \u0431\u0443\u0442\u043e\u043d \u0435 \u0441\u043a\u0440\u0438\u0442. \u041c\u043e\u0436\u0435\u0448 \u0434\u0430 \u043e\u0442\u0433\u043e\u0432\u043e\u0440\u0438\u0448 \u0441\u0430\u043c\u043e \u0441 \u00ab\u041e\u0442\u043d\u043e\u0432\u043e\u00bb \u0438\u043b\u0438 \u00ab\u0414\u043e\u0431\u0440\u0435\u00bb.",
        "hook_error": "Hider \u0441\u0440\u0435\u0449\u043d\u0430 \u043f\u0440\u043e\u0431\u043b\u0435\u043c \u0438 \u0438\u0437\u043a\u043b\u044e\u0447\u0438 \u0442\u0430\u0437\u0438 \u0447\u0430\u0441\u0442 \u043e\u0442 \u0441\u044a\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f. "
        "\u041f\u0440\u043e\u0432\u0435\u0440\u0438 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438\u0442\u0435 \u043d\u0430 \u0434\u043e\u0431\u0430\u0432\u043a\u0430\u0442\u0430.",
        "dialog_title": "Hider",
        "group_review": "\u041f\u043e \u0432\u0440\u0435\u043c\u0435 \u043d\u0430 \u043f\u043e\u0432\u0442\u043e\u0440\u0435\u043d\u0438\u0435\u0442\u043e, \u0441\u043a\u0440\u0438\u0432\u0430\u0439:",
        "group_behaviour": "\u041f\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u0435",
        "opt_menu_bar": "\u041b\u0435\u043d\u0442\u0430\u0442\u0430 \u0441 \u043c\u0435\u043d\u044e\u0442\u0430\u0442\u0430 (\u0424\u0430\u0439\u043b, \u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u0430\u043d\u0435, \u0418\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u0438...)",
        "opt_menu_bar_tip": "\u041f\u043e\u044f\u0432\u044f\u0432\u0430 \u0441\u0435 \u043e\u0442\u043d\u043e\u0432\u043e, \u0432\u0435\u0434\u043d\u0430\u0433\u0430 \u0449\u043e\u043c \u043d\u0430\u043f\u0443\u0441\u043d\u0435\u0448 \u043f\u043e\u0432\u0442\u043e\u0440\u0435\u043d\u0438\u0435\u0442\u043e.",
        "opt_toolbar": "\u0413\u043e\u0440\u043d\u0430\u0442\u0430 \u043b\u0435\u043d\u0442\u0430 \u0441 \u0438\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u0438 (\u0422\u0435\u0441\u0442\u0435\u0442\u0430, \u0414\u043e\u0431\u0430\u0432\u0438, \u0420\u0430\u0437\u0433\u043b\u0435\u0436\u0434\u0430\u0439, \u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0438)",
        "opt_toolbar_tip": "\u041f\u043e\u044f\u0432\u044f\u0432\u0430 \u0441\u0435 \u043e\u0442\u043d\u043e\u0432\u043e, \u0432\u0435\u0434\u043d\u0430\u0433\u0430 \u0449\u043e\u043c \u043d\u0430\u043f\u0443\u0441\u043d\u0435\u0448 \u043f\u043e\u0432\u0442\u043e\u0440\u0435\u043d\u0438\u0435\u0442\u043e.",
        "opt_bottom_bar": "\u0414\u043e\u043b\u043d\u0430\u0442\u0430 \u043b\u0435\u043d\u0442\u0430 \u043d\u0430 \u043f\u0440\u043e\u0437\u043e\u0440\u0435\u0446\u0430",
        "opt_bottom_bar_tip": "\u041f\u043e\u044f\u0432\u044f\u0432\u0430 \u0441\u0435 \u043e\u0442\u043d\u043e\u0432\u043e, \u0432\u0435\u0434\u043d\u0430\u0433\u0430 \u0449\u043e\u043c \u043d\u0430\u043f\u0443\u0441\u043d\u0435\u0448 \u043f\u043e\u0432\u0442\u043e\u0440\u0435\u043d\u0438\u0435\u0442\u043e.",
        "opt_scrollbar": "\u041b\u0435\u043d\u0442\u0430\u0442\u0430 \u0437\u0430 \u043f\u0440\u0435\u0432\u044a\u0440\u0442\u0430\u043d\u0435 \u043d\u0430 \u043a\u0430\u0440\u0442\u0430\u0442\u0430",
        "opt_scrollbar_tip": "\u0421\u0430\u043c\u043e \u0432\u0438\u0437\u0443\u0430\u043b\u043d\u043e: \u043c\u043e\u0436\u0435\u0448 \u0434\u0430 \u043f\u0440\u043e\u0434\u044a\u043b\u0436\u0430\u0432\u0430\u0448 \u0434\u0430 \u0441\u043a\u0440\u043e\u043b\u0438\u0440\u0430\u0448 \u0441 \u043a\u043e\u043b\u0435\u043b\u043e\u0442\u043e \u043d\u0430 \u043c\u0438\u0448\u043a\u0430\u0442\u0430. "
        "\u041f\u0440\u043e\u043c\u044f\u043d\u0430\u0442\u0430 \u0441\u0435 \u0437\u0430\u0431\u0435\u043b\u044f\u0437\u0432\u0430 \u043e\u0442 \u0441\u043b\u0435\u0434\u0432\u0430\u0449\u0430\u0442\u0430 \u043a\u0430\u0440\u0442\u0430.",
        "opt_hard_easy": "\u0411\u0443\u0442\u043e\u043d\u0438\u0442\u0435 \u00ab\u0422\u0440\u0443\u0434\u043d\u043e\u00bb \u0438 \u00ab\u041b\u0435\u0441\u043d\u043e\u00bb",
        "opt_hard_easy_tip": "\u041e\u0441\u0442\u0430\u0432\u044f \u0441\u0430\u043c\u043e \u00ab\u041e\u0442\u043d\u043e\u0432\u043e\u00bb \u0438 \u00ab\u0414\u043e\u0431\u0440\u0435\u00bb. \u0422\u0435\u0445\u043d\u0438\u0442\u0435 \u043a\u043b\u0430\u0432\u0438\u0448\u043d\u0438 \u043a\u043e\u043c\u0431\u0438\u043d\u0430\u0446\u0438\u0438 \u0441\u044a\u0449\u043e "
        "\u0441\u0430 \u0431\u043b\u043e\u043a\u0438\u0440\u0430\u043d\u0438, \u0437\u0430 \u0434\u0430 \u043d\u0435 \u043e\u0442\u0433\u043e\u0432\u043e\u0440\u0438\u0448 \u0441\u043b\u0443\u0447\u0430\u0439\u043d\u043e \u0441 \u043d\u0435\u0432\u0438\u0434\u0438\u043c \u0431\u0443\u0442\u043e\u043d.",
        "opt_cursor": "\u041f\u043e\u043a\u0430\u0437\u0430\u043b\u0435\u0446\u044a\u0442 \u043d\u0430 \u043c\u0438\u0448\u043a\u0430\u0442\u0430, \u043a\u043e\u0433\u0430\u0442\u043e \u0435 \u043d\u0435\u043f\u043e\u0434\u0432\u0438\u0436\u0435\u043d \u0437\u0430:",
        "opt_cursor_tip": "\u041f\u043e\u044f\u0432\u044f\u0432\u0430 \u0441\u0435 \u043e\u0442\u043d\u043e\u0432\u043e, \u0432\u0435\u0434\u043d\u0430\u0433\u0430 \u0449\u043e\u043c \u0434\u0432\u0438\u0436\u043d\u0435\u0448 \u043c\u0438\u0448\u043a\u0430\u0442\u0430.",
        "opt_cursor_suffix": " \u0441",
        "opt_auto_start": "\u0410\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u043d\u043e \u0437\u0430\u043f\u043e\u0447\u0432\u0430\u043d\u0435 \u043d\u0430 \u043f\u043e\u0432\u0442\u043e\u0440\u0435\u043d\u0438\u0435\u0442\u043e \u043f\u0440\u0438 \u043e\u0442\u0432\u0430\u0440\u044f\u043d\u0435 \u043d\u0430 \u0442\u0435\u0441\u0442\u0435",
        "opt_auto_start_tip": "\u0421\u0430\u043c\u043e \u0430\u043a\u043e \u0438\u043c\u0430 \u0447\u0430\u043a\u0430\u0449\u0438 \u043a\u0430\u0440\u0442\u0438. \u0410\u043a\u043e \u0441\u0430\u043c \u043d\u0430\u043f\u0443\u0441\u043d\u0435\u0448 \u043f\u043e\u0432\u0442\u043e\u0440\u0435\u043d\u0438\u0435\u0442\u043e, "
        "Hider \u043d\u044f\u043c\u0430 \u0434\u0430 \u0442\u0435 \u0432\u044a\u0440\u043d\u0435 \u043e\u0431\u0440\u0430\u0442\u043d\u043e.",
        "btn_save": "Приеми",
        "btn_cancel": "\u041e\u0442\u043a\u0430\u0437",
        "btn_defaults": "Възстанови стойностите по подразбиране",
        "saved": "\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438\u0442\u0435 \u043d\u0430 Hider \u0441\u0430 \u0437\u0430\u043f\u0430\u0437\u0435\u043d\u0438.",
        "save_failed": "\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438\u0442\u0435 \u043d\u0430 Hider \u043d\u0435 \u043c\u043e\u0433\u0430\u0442 \u0434\u0430 \u0431\u044a\u0434\u0430\u0442 \u0437\u0430\u043f\u0430\u0437\u0435\u043d\u0438.",
    },
    "sv": {
        "button_hidden": "Den knappen \u00e4r dold. Du kan bara svara \u00abIgen\u00bb eller \u00abBra\u00bb.",
        "hook_error": "Hider st\u00f6tte p\u00e5 ett problem och inaktiverade den delen av s\u00e4kerhetssk\u00e4l. "
        "Kontrollera till\u00e4ggets inst\u00e4llningar.",
        "dialog_title": "Hider",
        "group_review": "D\u00f6lj under genomg\u00e5ng:",
        "group_behaviour": "Beteende",
        "opt_menu_bar": "Menyraden (Arkiv, Redigera, Verktyg...)",
        "opt_menu_bar_tip": "Visas igen s\u00e5 fort du l\u00e4mnar genomg\u00e5ngen.",
        "opt_toolbar": "\u00d6vre verktygsf\u00e4ltet (Kortlekar, L\u00e4gg till, Bl\u00e4ddra, Statistik)",
        "opt_toolbar_tip": "Visas igen s\u00e5 fort du l\u00e4mnar genomg\u00e5ngen.",
        "opt_bottom_bar": "F\u00f6nstrets nedre f\u00e4lt",
        "opt_bottom_bar_tip": "Visas igen s\u00e5 fort du l\u00e4mnar genomg\u00e5ngen.",
        "opt_scrollbar": "Kortets rullningslist",
        "opt_scrollbar_tip": "Endast visuellt: du kan fortfarande scrolla med mushjulet. "
        "\u00c4ndringen syns p\u00e5 n\u00e4sta kort.",
        "opt_hard_easy": "Knapparna \u00abSv\u00e5rt\u00bb och \u00abL\u00e4tt\u00bb",
        "opt_hard_easy_tip": "L\u00e4mnar bara \u00abIgen\u00bb och \u00abBra\u00bb. Deras kortkommandon blockeras "
        "ocks\u00e5, s\u00e5 att du inte svarar av misstag med en knapp du inte ser.",
        "opt_cursor": "Muspekaren n\u00e4r den varit stilla i:",
        "opt_cursor_tip": "Visas igen s\u00e5 fort du r\u00f6r musen.",
        "opt_cursor_suffix": " s",
        "opt_auto_start": "B\u00f6rja genomg\u00e5ngen automatiskt n\u00e4r en kortlek \u00f6ppnas",
        "opt_auto_start_tip": "Bara om det finns kort att g\u00e5 igenom. Om det \u00e4r du sj\u00e4lv som l\u00e4mnar "
        "genomg\u00e5ngen s\u00e4tter Hider inte in dig igen.",
        "btn_save": "Acceptera",
        "btn_cancel": "Avbryt",
        "btn_defaults": "Återställ standardvärden",
        "saved": "Hider-inst\u00e4llningarna sparade.",
        "save_failed": "Kunde inte spara Hider-inst\u00e4llningarna.",
    },
    "da": {
        "button_hidden": "Den knap er skjult. Du kan kun svare \u00abIgen\u00bb eller \u00abGodt\u00bb.",
        "hook_error": "Hider st\u00f8dte p\u00e5 et problem og deaktiverede den del af sikkerhedshensyn. "
        "Tjek tilf\u00f8jelsens indstillinger.",
        "dialog_title": "Hider",
        "group_review": "Skjul under gennemgang:",
        "group_behaviour": "Adf\u00e6rd",
        "opt_menu_bar": "Menulinjen (Filer, Rediger, V\u00e6rkt\u00f8jer...)",
        "opt_menu_bar_tip": "Vises igen, s\u00e5 snart du forlader gennemgangen.",
        "opt_toolbar": "Den \u00f8verste v\u00e6rkt\u00f8jslinje (Bunker, Tilf\u00f8j, Gennemse, Statistik)",
        "opt_toolbar_tip": "Vises igen, s\u00e5 snart du forlader gennemgangen.",
        "opt_bottom_bar": "Vinduets nederste linje",
        "opt_bottom_bar_tip": "Vises igen, s\u00e5 snart du forlader gennemgangen.",
        "opt_scrollbar": "Kortets rullebj\u00e6lke",
        "opt_scrollbar_tip": "Kun visuelt: du kan stadig scrolle med musehjulet. "
        "\u00c6ndringen ses p\u00e5 det n\u00e6ste kort.",
        "opt_hard_easy": "Knapperne \u00abSv\u00e6rt\u00bb og \u00abLet\u00bb",
        "opt_hard_easy_tip": "Efterlader kun \u00abIgen\u00bb og \u00abGodt\u00bb. Deres genvejstaster blokeres "
        "ogs\u00e5, s\u00e5 du ikke ved et uheld svarer med en knap, du ikke kan se.",
        "opt_cursor": "Musemarker\u00f8ren, n\u00e5r den st\u00e5r stille i:",
        "opt_cursor_tip": "Vises igen, s\u00e5 snart du flytter musen.",
        "opt_cursor_suffix": " s",
        "opt_auto_start": "Start gennemgang automatisk, n\u00e5r en bunke \u00e5bnes",
        "opt_auto_start_tip": "Kun hvis der er kort forfaldne. Hvis du selv forlader gennemgangen, "
        "s\u00e6tter Hider dig ikke tilbage.",
        "btn_save": "Accepter",
        "btn_cancel": "Annuller",
        "btn_defaults": "Gendan standardværdier",
        "saved": "Hider-konfiguration gemt.",
        "save_failed": "Kunne ikke gemme Hider-konfigurationen.",
    },
    "nb": {
        "button_hidden": "Den knappen er skjult. Du kan bare svare \u00abIgjen\u00bb eller \u00abBra\u00bb.",
        "hook_error": "Hider st\u00f8tte p\u00e5 et problem og slo av den delen av sikkerhetshensyn. "
        "Sjekk innstillingene for tillegget.",
        "dialog_title": "Hider",
        "group_review": "Skjul under gjennomgang:",
        "group_behaviour": "Oppf\u00f8rsel",
        "opt_menu_bar": "Menylinjen (Fil, Rediger, Verkt\u00f8y...)",
        "opt_menu_bar_tip": "Vises igjen s\u00e5 snart du forlater gjennomgangen.",
        "opt_toolbar": "Den \u00f8verste verkt\u00f8ylinjen (Kortstokker, Legg til, Bla gjennom, Statistikk)",
        "opt_toolbar_tip": "Vises igjen s\u00e5 snart du forlater gjennomgangen.",
        "opt_bottom_bar": "Vinduets nederste linje",
        "opt_bottom_bar_tip": "Vises igjen s\u00e5 snart du forlater gjennomgangen.",
        "opt_scrollbar": "Kortets rullefelt",
        "opt_scrollbar_tip": "Kun visuelt: du kan fortsatt rulle med mushjulet. "
        "Endringen vises p\u00e5 neste kort.",
        "opt_hard_easy": "Knappene \u00abVanskelig\u00bb og \u00abLett\u00bb",
        "opt_hard_easy_tip": "Etterlater bare \u00abIgjen\u00bb og \u00abBra\u00bb. Hurtigtastene deres blokkeres "
        "ogs\u00e5, s\u00e5 du ikke svarer ved et uhell med en knapp du ikke ser.",
        "opt_cursor": "Musepekeren n\u00e5r den st\u00e5r stille i:",
        "opt_cursor_tip": "Vises igjen s\u00e5 snart du beveger musen.",
        "opt_cursor_suffix": " s",
        "opt_auto_start": "Start gjennomgangen automatisk n\u00e5r en kortstokk \u00e5pnes",
        "opt_auto_start_tip": "Bare hvis det finnes kort som forfaller. Hvis du selv forlater "
        "gjennomgangen, setter Hider deg ikke tilbake.",
        "btn_save": "Godta",
        "btn_cancel": "Avbryt",
        "btn_defaults": "Gjenopprett standardverdier",
        "saved": "Hider-innstillinger lagret.",
        "save_failed": "Kunne ikke lagre Hider-innstillingene.",
    },
    "fi": {
        "button_hidden": "Tuo painike on piilotettu. Voit vastata vain \u00abUudelleen\u00bb tai \u00abHyv\u00e4\u00bb.",
        "hook_error": "Hider t\u00f6rm\u00e4si ongelmaan ja poisti kyseisen osan k\u00e4yt\u00f6st\u00e4 turvallisuussyist\u00e4. "
        "Tarkista lis\u00e4osan asetukset.",
        "dialog_title": "Hider",
        "group_review": "Kertauksen aikana piilota:",
        "group_behaviour": "K\u00e4ytt\u00e4ytyminen",
        "opt_menu_bar": "Valikkorivi (Tiedosto, Muokkaa, Ty\u00f6kalut...)",
        "opt_menu_bar_tip": "Palautuu heti, kun poistut kertauksesta.",
        "opt_toolbar": "Yl\u00e4ty\u00f6kalurivi (Pakat, Lis\u00e4\u00e4, Selaa, Tilastot)",
        "opt_toolbar_tip": "Palautuu heti, kun poistut kertauksesta.",
        "opt_bottom_bar": "Ikkunan alapalkki",
        "opt_bottom_bar_tip": "Palautuu heti, kun poistut kertauksesta.",
        "opt_scrollbar": "Kortin vierityspalkki",
        "opt_scrollbar_tip": "Vain visuaalinen: voit silti vierit\u00e4\u00e4 hiiren rullalla. "
        "Muutos n\u00e4kyy seuraavassa kortissa.",
        "opt_hard_easy": "Painikkeet \u00abVaikea\u00bb ja \u00abHelppo\u00bb",
        "opt_hard_easy_tip": "J\u00e4tt\u00e4\u00e4 vain \u00abUudelleen\u00bb ja \u00abHyv\u00e4\u00bb. My\u00f6s niiden pikan\u00e4pp\u00e4imet "
        "est\u00e4\u00e4n, ettet vahingossa vastaa n\u00e4kym\u00e4tt\u00f6m\u00e4ll\u00e4 painikkeella.",
        "opt_cursor": "Hiiren osoitin, kun se on liikkumatta:",
        "opt_cursor_tip": "Palautuu heti, kun liikutat hiirt\u00e4.",
        "opt_cursor_suffix": " s",
        "opt_auto_start": "Aloita kertaus automaattisesti pakkaa avattaessa",
        "opt_auto_start_tip": "Vain jos on er\u00e4\u00e4ntyneit\u00e4 kortteja. Jos poistut kertauksesta itse, "
        "Hider ei laita sinua takaisin.",
        "btn_save": "Hyväksy",
        "btn_cancel": "Peruuta",
        "btn_defaults": "Palauta oletusarvot",
        "saved": "Hiderin asetukset tallennettu.",
        "save_failed": "Hiderin asetuksia ei voitu tallentaa.",
    },
    "et": {
        "button_hidden": "See nupp on peidetud. V\u00f5id vastata ainult \u00abUuesti\u00bb v\u00f5i \u00abHea\u00bb.",
        "hook_error": "Hider sattus probleemi ja keelas selle osa turvalisuse huvides. "
        "Kontrolli lisandi seadeid.",
        "dialog_title": "Hider",
        "group_review": "Kordamise ajal peida:",
        "group_behaviour": "K\u00e4itumine",
        "opt_menu_bar": "Men\u00fc\u00fcriba (Fail, Redigeeri, T\u00f6\u00f6riistad...)",
        "opt_menu_bar_tip": "Ilmub uuesti kohe, kui lahkud kordamisest.",
        "opt_toolbar": "\u00dclemine t\u00f6\u00f6riistariba (Pakid, Lisa, Sirvi, Statistika)",
        "opt_toolbar_tip": "Ilmub uuesti kohe, kui lahkud kordamisest.",
        "opt_bottom_bar": "Akna alumine riba",
        "opt_bottom_bar_tip": "Ilmub uuesti kohe, kui lahkud kordamisest.",
        "opt_scrollbar": "Kaardi kerimisriba",
        "opt_scrollbar_tip": "Ainult visuaalne: saad ikka hiireratta abil kerida. "
        "Muudatus n\u00e4hakse j\u00e4rgmisel kaardil.",
        "opt_hard_easy": "Nupud \u00abRaske\u00bb ja \u00abKerge\u00bb",
        "opt_hard_easy_tip": "J\u00e4tab alles ainult \u00abUuesti\u00bb ja \u00abHea\u00bb. Ka nende kiirklahvid "
        "blokeeritakse, et sa ei vastaks kogemata nupuga, mida ei n\u00e4e.",
        "opt_cursor": "Hiirekursor, kui see on liikumatu:",
        "opt_cursor_tip": "Ilmub uuesti kohe, kui liigutad hiirt.",
        "opt_cursor_suffix": " s",
        "opt_auto_start": "Alusta kordamist automaatselt paki avamisel",
        "opt_auto_start_tip": "Ainult kui on t\u00e4htaegseid kaarte. Kui lahkud kordamisest ise, "
        "ei pane Hider sind tagasi.",
        "btn_save": "Nõustu",
        "btn_cancel": "T\u00fchista",
        "btn_defaults": "Taasta vaikeväärtused",
        "saved": "Hideri seaded salvestatud.",
        "save_failed": "Hideri seadeid ei \u00f5nnestunud salvestada.",
    },
    "lt": {
        "button_hidden": "\u0160is mygtukas pasl\u0117ptas. Gali atsakyti tik \u00abI\u0161 naujo\u00bb arba \u00abGerai\u00bb.",
        "hook_error": "Hider susid\u016br\u0117 su problema ir sauga sumetimais i\u0161jung\u0117 t\u0105 dal\u012f. "
        "Patikrink priedo nustatymus.",
        "dialog_title": "Hider",
        "group_review": "Kartojimo metu sl\u0117pti:",
        "group_behaviour": "Elgsena",
        "opt_menu_bar": "Meniu juosta (Failas, Redaguoti, \u012erankiai...)",
        "opt_menu_bar_tip": "V\u0117l pasirodo, kai tik i\u0161eini i\u0161 kartojimo.",
        "opt_toolbar": "Vir\u0161utin\u0117 \u012frank\u012f juosta (Kaladel\u0117s, Prid\u0117ti, Nar\u0161yti, Statistika)",
        "opt_toolbar_tip": "V\u0117l pasirodo, kai tik i\u0161eini i\u0161 kartojimo.",
        "opt_bottom_bar": "Apatin\u0117 lango juosta",
        "opt_bottom_bar_tip": "V\u0117l pasirodo, kai tik i\u0161eini i\u0161 kartojimo.",
        "opt_scrollbar": "Kortel\u0117s slinkties juosta",
        "opt_scrollbar_tip": "Tik vizualiai: vis tiek gali slinkti pel\u0117s ratuku. "
        "Pakeitimas pastebimas kitoje kortel\u0117je.",
        "opt_hard_easy": "Mygtukai \u00abSunku\u00bb ir \u00abLengva\u00bb",
        "opt_hard_easy_tip": "Palieka tik \u00abI\u0161 naujo\u00bb ir \u00abGerai\u00bb. J\u0173 sparti\u0119j\u0173 klavi\u0161\u0173 kombinacijos "
        "taip pat blokuojamos, kad netyčia neatsakytum nematomu mygtuku.",
        "opt_cursor": "Pel\u0117s ymeklis, kai jis nejuda:",
        "opt_cursor_tip": "V\u0117l pasirodo, kai tik pajudini pel\u0119.",
        "opt_cursor_suffix": " s",
        "opt_auto_start": "Automati\u0161kai prad\u0117ti kartojim\u0105 atidarius kaladel\u0119",
        "opt_auto_start_tip": "Tik jei yra kartotin\u0173 korteli\u0173. Jei pats i\u0161eini i\u0161 kartojimo, "
        "Hider tavęs atgal ne\u012ftraukia.",
        "btn_save": "Priimti",
        "btn_cancel": "At\u0161aukti",
        "btn_defaults": "Atkurti numatytąsias reikšmes",
        "saved": "Hider konfig\u016bracija \u012fra\u0161yta.",
        "save_failed": "Nepavyko \u012fra\u0161yti Hider konfig\u016bracijos.",
    },
    "hu": {
        "button_hidden": "Ez a gomb el van rejtve. Csak \u00abIsm\u00e9t\u00bb vagy \u00abJ\u00f3\u00bb v\u00e1lasszal felelhetsz.",
        "hook_error": "A Hider hib\u00e1ba \u00fctk\u00f6z\u00f6tt, \u00e9s biztons\u00e1gi okokb\u00f3l kikapcsolta azt a r\u00e9szt. "
        "Ellen\u0151rizd a b\u0151v\u00edtm\u00e9ny be\u00e1ll\u00edt\u00e1sait.",
        "dialog_title": "Hider",
        "group_review": "Ism\u00e9tl\u00e9s k\u00f6zben rejtsd el:",
        "group_behaviour": "Viselked\u00e9s",
        "opt_menu_bar": "A men\u00fcsor (F\u00e1jl, Szerkeszt\u00e9s, Eszk\u00f6z\u00f6k...)",
        "opt_menu_bar_tip": "Azonnal visszat\u00e9r, amint kil\u00e9psz az ism\u00e9tl\u00e9sb\u0151l.",
        "opt_toolbar": "A fels\u0151 eszk\u00f6zt\u00e1r (Paklik, Hozz\u00e1ad\u00e1s, B\u00f6ng\u00e9sz\u00e9s, Statisztika)",
        "opt_toolbar_tip": "Azonnal visszat\u00e9r, amint kil\u00e9psz az ism\u00e9tl\u00e9sb\u0151l.",
        "opt_bottom_bar": "Az ablak als\u00f3 s\u00e1vja",
        "opt_bottom_bar_tip": "Azonnal visszat\u00e9r, amint kil\u00e9psz az ism\u00e9tl\u00e9sb\u0151l.",
        "opt_scrollbar": "A k\u00e1rtya g\u00f6rget\u0151s\u00e1vja",
        "opt_scrollbar_tip": "Csak vizu\u00e1lis: az eg\u00e9r gomb\u00e1val tov\u00e1bbra is g\u00f6rgethetsz. "
        "A v\u00e1ltoz\u00e1s a k\u00f6vetkez\u0151 k\u00e1rty\u00e1n l\u00e1tszik.",
        "opt_hard_easy": "A \u00abNeh\u00e9z\u00bb \u00e9s \u00abK\u00f6nny\u0171\u00bb gombok",
        "opt_hard_easy_tip": "Csak \u00abIsm\u00e9t\u00bb-et \u00e9s \u00abJ\u00f3\u00bb-t hagyja meg. A hozz\u00e1juk tartoz\u00f3 gyorsbillenty\u0171k is "
        "le vannak tiltva, hogy v\u00e9letlen\u00fcl se v\u00e1laszolj egy l\u00e1thatatlan gombbal.",
        "opt_cursor": "Az eg\u00e9rmutat\u00f3, ha mozdulatlan ennyi ideig:",
        "opt_cursor_tip": "Azonnal visszat\u00e9r, amint mozgatod az eg\u00e9ret.",
        "opt_cursor_suffix": " mp",
        "opt_auto_start": "Ism\u00e9tl\u00e9s automatikus ind\u00edt\u00e1sa pakli megnyit\u00e1sakor",
        "opt_auto_start_tip": "Csak ha van esed\u00e9kes k\u00e1rtya. Ha te magad l\u00e9psz ki az ism\u00e9tl\u00e9sb\u0151l, "
        "a Hider nem tesz vissza.",
        "btn_save": "Elfogadás",
        "btn_cancel": "M\u00e9gse",
        "btn_defaults": "Alapértelmezett értékek visszaállítása",
        "saved": "Hider be\u00e1ll\u00edt\u00e1sai mentve.",
        "save_failed": "Nem siker\u00fclt menteni a Hider be\u00e1ll\u00edt\u00e1sait.",
    },
    "el": {
        "button_hidden": "\u0391\u03c5\u03c4\u03cc \u03c4\u03bf \u03ba\u03bf\u03c5\u03bc\u03c0\u03af \u03b5\u03af\u03bd\u03b1\u03b9 \u03ba\u03c1\u03c5\u03bc\u03bc\u03ad\u03bd\u03bf. \u039c\u03c0\u03bf\u03c1\u03b5\u03af\u03c2 \u03bd\u03b1 \u03b1\u03c0\u03b1\u03bd\u03c4\u03ae\u03c3\u03b5\u03b9\u03c2 \u03bc\u03cc\u03bd\u03bf \u00ab\u039e\u03b1\u03bd\u03ac\u00bb \u03ae \u00ab\u039a\u03b1\u03bb\u03ac\u00bb.",
        "hook_error": "\u03a4\u03bf Hider \u03b1\u03bd\u03c4\u03b9\u03bc\u03b5\u03c4\u03ce\u03c0\u03b9\u03c3\u03b5 \u03ad\u03bd\u03b1 \u03c0\u03c1\u03cc\u03b2\u03bb\u03b7\u03bc\u03b1 \u03ba\u03b1\u03b9 \u03b1\u03c0\u03b5\u03bd\u03b5\u03c1\u03b3\u03bf\u03c0\u03bf\u03af\u03b7\u03c3\u03b5 \u03b1\u03c5\u03c4\u03cc \u03c4\u03bf \u03bc\u03ad\u03c1\u03bf\u03c2 \u03b3\u03b9\u03b1 \u03bb\u03cc\u03b3\u03bf\u03c5\u03c2 \u03b1\u03c3\u03c6\u03ac\u03bb\u03b5\u03b9\u03b1\u03c2. "
        "\u0388\u03bb\u03b5\u03b3\u03be\u03b5 \u03c4\u03b9\u03c2 \u03c1\u03c5\u03b8\u03bc\u03af\u03c3\u03b5\u03b9\u03c2 \u03c4\u03bf\u03c5 \u03c0\u03c1\u03cc\u03c3\u03b8\u03b5\u03c4\u03bf\u03c5.",
        "dialog_title": "Hider",
        "group_review": "\u039a\u03b1\u03c4\u03ac \u03c4\u03b7\u03bd \u03b5\u03c0\u03b1\u03bd\u03ac\u03bb\u03b7\u03c8\u03b7, \u03b1\u03c0\u03cc\u03ba\u03c1\u03c5\u03c8\u03b5:",
        "group_behaviour": "\u03a3\u03c5\u03bc\u03c0\u03b5\u03c1\u03b9\u03c6\u03bf\u03c1\u03ac",
        "opt_menu_bar": "\u0397 \u03bc\u03c0\u03ac\u03c1\u03b1 \u03bc\u03b5\u03bd\u03bf\u03cd (\u0391\u03c1\u03c7\u03b5\u03af\u03bf, \u0395\u03c0\u03b5\u03be\u03b5\u03c1\u03b3\u03b1\u03c3\u03af\u03b1, \u0395\u03c1\u03b3\u03b1\u03bb\u03b5\u03af\u03b1...)",
        "opt_menu_bar_tip": "\u0395\u03bc\u03c6\u03b1\u03bd\u03af\u03b6\u03b5\u03c4\u03b1\u03b9 \u03be\u03b1\u03bd\u03ac \u03bc\u03cc\u03bb\u03b9\u03c2 \u03b2\u03b3\u03b5\u03b9\u03c2 \u03b1\u03c0\u03cc \u03c4\u03b7\u03bd \u03b5\u03c0\u03b1\u03bd\u03ac\u03bb\u03b7\u03c8\u03b7.",
        "opt_toolbar": "\u0397 \u03ac\u03bd\u03c9 \u03bc\u03c0\u03ac\u03c1\u03b1 \u03b5\u03c1\u03b3\u03b1\u03bb\u03b5\u03af\u03c9\u03bd (\u03a4\u03c1\u03ac\u03c0\u03bf\u03c5\u03bb\u03b5\u03c2, \u03a0\u03c1\u03bf\u03c3\u03b8\u03ae\u03ba\u03b7, \u03a0\u03b5\u03c1\u03b9\u03ae\u03b3\u03b7\u03c3\u03b7, \u03a3\u03c4\u03b1\u03c4\u03b9\u03c3\u03c4\u03b9\u03ba\u03ac)",
        "opt_toolbar_tip": "\u0395\u03bc\u03c6\u03b1\u03bd\u03af\u03b6\u03b5\u03c4\u03b1\u03b9 \u03be\u03b1\u03bd\u03ac \u03bc\u03cc\u03bb\u03b9\u03c2 \u03b2\u03b3\u03b5\u03b9\u03c2 \u03b1\u03c0\u03cc \u03c4\u03b7\u03bd \u03b5\u03c0\u03b1\u03bd\u03ac\u03bb\u03b7\u03c8\u03b7.",
        "opt_bottom_bar": "\u0397 \u03ba\u03ac\u03c4\u03c9 \u03bc\u03c0\u03ac\u03c1\u03b1 \u03c4\u03bf\u03c5 \u03c0\u03b1\u03c1\u03b1\u03b8\u03cd\u03c1\u03bf\u03c5",
        "opt_bottom_bar_tip": "\u0395\u03bc\u03c6\u03b1\u03bd\u03af\u03b6\u03b5\u03c4\u03b1\u03b9 \u03be\u03b1\u03bd\u03ac \u03bc\u03cc\u03bb\u03b9\u03c2 \u03b2\u03b3\u03b5\u03b9\u03c2 \u03b1\u03c0\u03cc \u03c4\u03b7\u03bd \u03b5\u03c0\u03b1\u03bd\u03ac\u03bb\u03b7\u03c8\u03b7.",
        "opt_scrollbar": "\u0397 \u03bc\u03c0\u03ac\u03c1\u03b1 \u03ba\u03cd\u03bb\u03b9\u03c3\u03b7\u03c2 \u03c4\u03b7\u03c2 \u03ba\u03ac\u03c1\u03c4\u03b1\u03c2",
        "opt_scrollbar_tip": "\u039c\u03cc\u03bd\u03bf \u03bf\u03c0\u03c4\u03b9\u03ba\u03ac: \u03bc\u03c0\u03bf\u03c1\u03b5\u03af\u03c2 \u03bd\u03b1 \u03c3\u03c5\u03bd\u03b5\u03c7\u03af\u03c3\u03b5\u03b9\u03c2 \u03bd\u03b1 \u03ba\u03c5\u03bb\u03ac\u03c2 \u03bc\u03b5 \u03c4\u03b7 \u03c1\u03cc\u03b4\u03b1 \u03c4\u03bf\u03c5 \u03c0\u03bf\u03bd\u03c4\u03b9\u03bf\u03cd. "
        "\u0397 \u03b1\u03bb\u03bb\u03b1\u03b3\u03ae \u03c6\u03b1\u03af\u03bd\u03b5\u03c4\u03b1\u03b9 \u03c3\u03c4\u03b7\u03bd \u03b5\u03c0\u03cc\u03bc\u03b5\u03bd\u03b7 \u03ba\u03ac\u03c1\u03c4\u03b1.",
        "opt_hard_easy": "\u03a4\u03b1 \u03ba\u03bf\u03c5\u03bc\u03c0\u03b9\u03ac \u00ab\u0394\u03cd\u03c3\u03ba\u03bf\u03bb\u03bf\u00bb \u03ba\u03b1\u03b9 \u00ab\u0395\u03cd\u03ba\u03bf\u03bb\u03bf\u00bb",
        "opt_hard_easy_tip": "\u0391\u03c6\u03ae\u03bd\u03b5\u03b9 \u03bc\u03cc\u03bd\u03bf \u00ab\u039e\u03b1\u03bd\u03ac\u00bb \u03ba\u03b1\u03b9 \u00ab\u039a\u03b1\u03bb\u03ac\u00bb. \u039f\u03b9 \u03c3\u03c5\u03bd\u03c4\u03bf\u03bc\u03b5\u03cd\u03c3\u03b5\u03b9\u03c2 \u03c0\u03bb\u03b7\u03ba\u03c4\u03c1\u03bf\u03bb\u03bf\u03b3\u03af\u03bf\u03c5 \u03c4\u03bf\u03c5\u03c2 "
        "\u03b5\u03af\u03bd\u03b1\u03b9 \u03b5\u03c0\u03af\u03c3\u03b7\u03c2 \u03bc\u03c0\u03bb\u03bf\u03ba\u03b1\u03c1\u03b9\u03c3\u03bc\u03ad\u03bd\u03b5\u03c2, \u03ce\u03c3\u03c4\u03b5 \u03bd\u03b1 \u03bc\u03b7\u03bd \u03b1\u03c0\u03b1\u03bd\u03c4\u03ae\u03c3\u03b5\u03b9\u03c2 \u03ba\u03b1\u03c4\u03ac \u03bb\u03ac\u03b8\u03bf\u03c2 \u03bc\u03b5 \u03ba\u03bf\u03c5\u03bc\u03c0\u03af \u03c0\u03bf\u03c5 \u03b4\u03b5\u03bd \u03b2\u03bb\u03ad\u03c0\u03b5\u03b9\u03c2.",
        "opt_cursor": "\u039f \u03b4\u03b5\u03af\u03ba\u03c4\u03b7\u03c2 \u03c4\u03bf\u03c5 \u03c0\u03bf\u03bd\u03c4\u03b9\u03bf\u03cd \u03cc\u03c4\u03b1\u03bd \u03bc\u03ad\u03bd\u03b5\u03b9 \u03b1\u03ba\u03af\u03bd\u03b7\u03c4\u03bf\u03c2 \u03b3\u03b9\u03b1:",
        "opt_cursor_tip": "\u0395\u03bc\u03c6\u03b1\u03bd\u03af\u03b6\u03b5\u03c4\u03b1\u03b9 \u03be\u03b1\u03bd\u03ac \u03bc\u03cc\u03bb\u03b9\u03c2 \u03ba\u03bf\u03c5\u03bd\u03ae\u03c3\u03b5\u03b9\u03c2 \u03c4\u03bf \u03c0\u03bf\u03bd\u03c4\u03af\u03ba\u03b9.",
        "opt_cursor_suffix": " \u03b4",
        "opt_auto_start": "\u0391\u03c5\u03c4\u03cc\u03bc\u03b1\u03c4\u03b7 \u03ad\u03bd\u03b1\u03c1\u03be\u03b7 \u03b5\u03c0\u03b1\u03bd\u03ac\u03bb\u03b7\u03c8\u03b7\u03c2 \u03ba\u03b1\u03c4\u03ac \u03c4\u03bf \u03ac\u03bd\u03bf\u03b9\u03b3\u03bc\u03b1 \u03c4\u03c1\u03ac\u03c0\u03bf\u03c5\u03bb\u03b1\u03c2",
        "opt_auto_start_tip": "\u039c\u03cc\u03bd\u03bf \u03b1\u03bd \u03c5\u03c0\u03ac\u03c1\u03c7\u03bf\u03c5\u03bd \u03b5\u03ba\u03ba\u03c1\u03b5\u03bc\u03b5\u03af\u03c2 \u03ba\u03ac\u03c1\u03c4\u03b5\u03c2. \u0391\u03bd \u03b5\u03c3\u03cd \u03b1\u03c6\u03ae\u03c3\u03b5\u03b9\u03c2 \u03c4\u03b7\u03bd \u03b5\u03c0\u03b1\u03bd\u03ac\u03bb\u03b7\u03c8\u03b7, "
        "\u03c4\u03bf Hider \u03b4\u03b5 \u03c3\u03b5 \u03be\u03b1\u03bd\u03b1\u03b2\u03ac\u03b6\u03b5\u03b9 \u03bc\u03ad\u03c3\u03b1.",
        "btn_save": "Αποδοχή",
        "btn_cancel": "\u0391\u03ba\u03cd\u03c1\u03c9\u03c3\u03b7",
        "btn_defaults": "Επαναφορά προεπιλογών",
        "saved": "\u0397 \u03c1\u03cd\u03b8\u03bc\u03b9\u03c3\u03b7 \u03c4\u03bf\u03c5 Hider \u03b1\u03c0\u03bf\u03b8\u03b7\u03ba\u03b5\u03cd\u03c4\u03b7\u03ba\u03b5.",
        "save_failed": "\u0394\u03b5\u03bd \u03ae\u03c4\u03b1\u03bd \u03b4\u03c5\u03bd\u03b1\u03c4\u03ae \u03b7 \u03b1\u03c0\u03bf\u03b8\u03ae\u03ba\u03b5\u03c5\u03c3\u03b7 \u03c4\u03b7\u03c2 \u03c1\u03cd\u03b8\u03bc\u03b9\u03c3\u03b7\u03c2 \u03c4\u03bf\u03c5 Hider.",
    },
    "tr": {
        "button_hidden": "Bu d\u00fc\u011fme gizli. Yaln\u0131zca \u00abTekrar\u00bb veya \u00abiyi\u00bb ile cevap verebilirsin.",
        "hook_error": "Hider bir sorunla kar\u015f\u0131la\u015ft\u0131 ve g\u00fcvenlik i\u00e7in o b\u00f6l\u00fcm\u00fc devre d\u0131\u015f\u0131 b\u0131rakt\u0131. "
        "Eklentinin yap\u0131land\u0131rmas\u0131n\u0131 kontrol et.",
        "dialog_title": "Hider",
        "group_review": "Tekrar s\u0131ras\u0131nda gizle:",
        "group_behaviour": "Davran\u0131\u015f",
        "opt_menu_bar": "Men\u00fc \u00e7ubu\u011fu (Dosya, D\u00fczen, Ara\u00e7lar...)",
        "opt_menu_bar_tip": "Tekrardan \u00e7\u0131kar \u00e7\u0131kmaz yeniden g\u00f6r\u00fcn\u00fcr.",
        "opt_toolbar": "\u00dcst ara\u00e7 \u00e7ubu\u011fu (Desteler, Ekle, G\u00f6zat, \u0130statistikler)",
        "opt_toolbar_tip": "Tekrardan \u00e7\u0131kar \u00e7\u0131kmaz yeniden g\u00f6r\u00fcn\u00fcr.",
        "opt_bottom_bar": "Pencerenin alt \u00e7ubu\u011fu",
        "opt_bottom_bar_tip": "Tekrardan \u00e7\u0131kar \u00e7\u0131kmaz yeniden g\u00f6r\u00fcn\u00fcr.",
        "opt_scrollbar": "Kart\u0131n kayd\u0131rma \u00e7ubu\u011fu",
        "opt_scrollbar_tip": "Sadece g\u00f6rsel: fare tekerle\u011fiyle hala kayd\u0131rabilirsin. "
        "De\u011fi\u015fiklik bir sonraki kartta g\u00f6r\u00fcl\u00fcr.",
        "opt_hard_easy": "\u00abZor\u00bb ve \u00abKolay\u00bb d\u00fc\u011fmeleri",
        "opt_hard_easy_tip": "Sadece \u00abTekrar\u00bb ve \u00abiyi\u00bb b\u0131rak\u0131r. Klavye k\u0131sayollar\u0131 da "
        "engellenir, b\u00f6ylece g\u00f6remedi\u011fin bir d\u00fc\u011fmeyle yanl\u0131\u015fl\u0131kla cevap vermezsin.",
        "opt_cursor": "Fare imleci \u015fu s\u00fcre hareketsiz kald\u0131\u011f\u0131nda:",
        "opt_cursor_tip": "Fareyi hareket ettirir ettirmez yeniden g\u00f6r\u00fcn\u00fcr.",
        "opt_cursor_suffix": " sn",
        "opt_auto_start": "Deste a\u00e7\u0131ld\u0131\u011f\u0131nda tekrar\u0131 otomatik ba\u015flat",
        "opt_auto_start_tip": "Sadece vadesi gelen kart varsa. Tekrardan kendin \u00e7\u0131karsan, "
        "Hider seni geri sokmaz.",
        "btn_save": "Kabul Et",
        "btn_cancel": "\u0130ptal",
        "btn_defaults": "Varsayılan değerleri geri yükle",
        "saved": "Hider yap\u0131land\u0131rmas\u0131 kaydedildi.",
        "save_failed": "Hider yap\u0131land\u0131rmas\u0131 kaydedilemedi.",
    },
    "ar": {
        "button_hidden": "\u0630\u0644\u0643 \u0627\u0644\u0632\u0631 \u0645\u062e\u0641\u064a. \u064a\u0645\u0643\u0646\u0643 \u0627\u0644\u0625\u062c\u0627\u0628\u0629 \u0641\u0642\u0637 \u0628\u0640 \u00ab\u0645\u0631\u0629 \u0623\u062e\u0631\u0649\u00bb \u0623\u0648 \u00ab\u062c\u064a\u062f\u00bb.",
        "hook_error": "\u0648\u0627\u062c\u0647 Hider \u0645\u0634\u0643\u0644\u0629 \u0648\u0642\u0627\u0645 \u0628\u062a\u0639\u0637\u064a\u0644 \u0630\u0644\u0643 \u0627\u0644\u062c\u0632\u0621 \u0644\u0644\u0633\u0644\u0627\u0645\u0629. "
        "\u062a\u062d\u0642\u0642 \u0645\u0646 \u0625\u0639\u062f\u0627\u062f\u0627\u062a \u0627\u0644\u0625\u0636\u0627\u0641\u0629.",
        "dialog_title": "Hider",
        "group_review": "\u0623\u062b\u0646\u0627\u0621 \u0627\u0644\u0645\u0631\u0627\u062c\u0639\u0629\u060c \u0623\u062e\u0641\u0650:",
        "group_behaviour": "\u0627\u0644\u0633\u0644\u0648\u0643",
        "opt_menu_bar": "\u0634\u0631\u064a\u0637 \u0627\u0644\u0642\u0648\u0627\u0626\u0645 (\u0645\u0644\u0641\u060c \u062a\u062d\u0631\u064a\u0631\u060c \u0623\u062f\u0648\u0627\u062a...)",
        "opt_menu_bar_tip": "\u064a\u0638\u0647\u0631 \u0645\u062c\u062f\u062f\u064b\u0627 \u0628\u0645\u062c\u0631\u062f \u0645\u063a\u0627\u062f\u0631\u062a\u0643 \u0627\u0644\u0645\u0631\u0627\u062c\u0639\u0629.",
        "opt_toolbar": "\u0634\u0631\u064a\u0637 \u0627\u0644\u0623\u062f\u0648\u0627\u062a \u0627\u0644\u0639\u0644\u0648\u064a (\u0627\u0644\u0631\u0632\u0645\u060c \u0625\u0636\u0627\u0641\u0629\u060c \u062a\u0635\u0641\u062d\u060c \u0625\u062d\u0635\u0627\u0626\u064a\u0627\u062a)",
        "opt_toolbar_tip": "\u064a\u0638\u0647\u0631 \u0645\u062c\u062f\u062f\u064b\u0627 \u0628\u0645\u062c\u0631\u062f \u0645\u063a\u0627\u062f\u0631\u062a\u0643 \u0627\u0644\u0645\u0631\u0627\u062c\u0639\u0629.",
        "opt_bottom_bar": "\u0627\u0644\u0634\u0631\u064a\u0637 \u0627\u0644\u0633\u0641\u0644\u064a \u0644\u0644\u0646\u0627\u0641\u0630\u0629",
        "opt_bottom_bar_tip": "\u064a\u0638\u0647\u0631 \u0645\u062c\u062f\u062f\u064b\u0627 \u0628\u0645\u062c\u0631\u062f \u0645\u063a\u0627\u062f\u0631\u062a\u0643 \u0627\u0644\u0645\u0631\u0627\u062c\u0639\u0629.",
        "opt_scrollbar": "\u0634\u0631\u064a\u0637 \u062a\u0645\u0631\u064a\u0631 \u0627\u0644\u0628\u0637\u0627\u0642\u0629",
        "opt_scrollbar_tip": "\u0645\u0631\u0626\u064a \u0641\u0642\u0637: \u064a\u0645\u0643\u0646\u0643 \u0627\u0644\u062a\u0645\u0631\u064a\u0631 \u0628\u0639\u062c\u0644\u0629 \u0627\u0644\u0641\u0623\u0631\u0629. "
        "\u064a\u0638\u0647\u0631 \u0627\u0644\u062a\u063a\u064a\u064a\u0631 \u0641\u064a \u0627\u0644\u0628\u0637\u0627\u0642\u0629 \u0627\u0644\u062a\u0627\u0644\u064a\u0629.",
        "opt_hard_easy": "\u0632\u0631\u0627 \u00ab\u0635\u0639\u0628\u00bb \u0648\u00ab\u0633\u0647\u0644\u00bb",
        "opt_hard_easy_tip": "\u064a\u0628\u0642\u064a \u0641\u0642\u0637 \u00ab\u0645\u0631\u0629 \u0623\u062e\u0631\u0649\u00bb \u0648\u00ab\u062c\u064a\u062f\u00bb. \u0648\u064a\u062a\u0645 \u0623\u064a\u0636\u064b\u0627 \u062d\u0638\u0631 "
        "\u0627\u062e\u062a\u0635\u0627\u0631\u0627\u062a\u0647\u0645\u0627 \u0644\u0644\u0648\u062d \u0644\u064a\u0644\u0627 \u062a\u062c\u064a\u0628 \u0639\u0646 \u0637\u0631\u064a\u0642 \u0627\u0644\u062e\u0637\u0623 \u0628\u0632\u0631 \u0644\u0627 \u062a\u0631\u0627\u0647.",
        "opt_cursor": "\u0645\u0624\u0634\u0631 \u0627\u0644\u0641\u0623\u0631\u0629 \u0639\u0646\u062f \u0628\u0642\u0627\u0626\u0647 \u0628\u0644\u0627 \u062d\u0631\u0643\u0629 \u0644\u0645\u062f\u0629:",
        "opt_cursor_tip": "\u064a\u0638\u0647\u0631 \u0645\u062c\u062f\u062f\u064b\u0627 \u0628\u0645\u062c\u0631\u062f \u062a\u062d\u0631\u064a\u0643 \u0627\u0644\u0641\u0623\u0631\u0629.",
        "opt_cursor_suffix": " \u062b",
        "opt_auto_start": "\u0628\u062f\u0621 \u0627\u0644\u0645\u0631\u0627\u062c\u0639\u0629 \u062a\u0644\u0642\u0627\u0626\u064a\u064b\u0627 \u0639\u0646\u062f \u0641\u062a\u062d \u0631\u0632\u0645\u0629",
        "opt_auto_start_tip": "\u0641\u0642\u0637 \u0625\u0630\u0627 \u0648\u062c\u062f\u062a \u0628\u0637\u0627\u0642\u0627\u062a \u0645\u0633\u062a\u062d\u0642\u0629. \u0625\u0630\u0627 \u062e\u0631\u062c\u062a \u0623\u0646\u062a \u0645\u0646 \u0627\u0644\u0645\u0631\u0627\u062c\u0639\u0629\u060c "
        "\u0644\u0646 \u064a\u0639\u064a\u062f\u0643 Hider \u0625\u0644\u064a\u0647\u0627.",
        "btn_save": "قبول",
        "btn_cancel": "\u0625\u0644\u063a\u0627\u0621",
        "btn_defaults": "استعادة القيم الافتراضية",
        "saved": "\u062a\u0645 \u062d\u0641\u0638 \u0625\u0639\u062f\u0627\u062f\u0627\u062a Hider.",
        "save_failed": "\u062a\u0639\u0630\u0631 \u062d\u0641\u0638 \u0625\u0639\u062f\u0627\u062f\u0627\u062a Hider.",
    },
    "he": {
        "button_hidden": "\u05d4\u05db\u05e4\u05ea\u05d5\u05e8 \u05d4\u05d6\u05d4 \u05de\u05d5\u05e1\u05ea\u05e8. \u05d0\u05e4\u05e9\u05e8 \u05dc\u05d4\u05e9\u05d9\u05d1 \u05e8\u05e7 \u05d1\u05e2\u05d6\u05e8\u05ea \u00ab\u05e9\u05d5\u05d1\u00bb \u05d0\u05d5 \u00ab\u05d8\u05d5\u05d1\u00bb.",
        "hook_error": "\u05dc-Hider \u05e0\u05ea\u05e7\u05dc\u05d4 \u05d1\u05e2\u05d9\u05d4 \u05d5\u05d4\u05d5\u05d0 \u05d4\u05e9\u05d1\u05d9\u05ea \u05d0\u05ea \u05d4\u05d7\u05dc\u05e7 \u05d4\u05d6\u05d4 \u05de\u05d8\u05e2\u05de\u05d9 \u05d1\u05d8\u05d9\u05d7\u05d5\u05ea. "
        "\u05d1\u05d3\u05d5\u05e7 \u05d0\u05ea \u05d4\u05d2\u05d3\u05e8\u05d5\u05ea \u05d4\u05ea\u05d5\u05e1\u05e3.",
        "dialog_title": "Hider",
        "group_review": "\u05d1\u05de\u05d4\u05dc\u05da \u05d7\u05d6\u05e8\u05d4, \u05d4\u05e1\u05ea\u05e8:",
        "group_behaviour": "\u05d4\u05ea\u05e0\u05d4\u05d2\u05d5\u05ea",
        "opt_menu_bar": "\u05e1\u05e8\u05d2\u05dc \u05d4\u05ea\u05e4\u05e8\u05d9\u05d8\u05d9\u05dd (\u05e7\u05d5\u05d1\u05e5\u05f4\u05d0, \u05e2\u05e8\u05d9\u05db\u05d4, \u05db\u05dc\u05d9\u05dd...)",
        "opt_menu_bar_tip": "\u05de\u05d5\u05e4\u05d9\u05e2 \u05de\u05d7\u05d3\u05e9 \u05de\u05d9\u05d3 \u05e9\u05d0\u05ea\u05d4 \u05e2\u05d5\u05d6\u05d1 \u05d0\u05ea \u05d4\u05d7\u05d6\u05e8\u05d4.",
        "opt_toolbar": "\u05e1\u05e8\u05d2\u05dc \u05d4\u05db\u05dc\u05d9\u05dd \u05d4\u05e2\u05dc\u05d9\u05d5\u05df (\u05d7\u05d1\u05d9\u05dc\u05d5\u05ea, \u05d4\u05d5\u05e1\u05e3, \u05e2\u05d9\u05d5\u05df, \u05e1\u05d8\u05d8\u05d9\u05e1\u05d8\u05d9\u05e7\u05d5\u05ea)",
        "opt_toolbar_tip": "\u05de\u05d5\u05e4\u05d9\u05e2 \u05de\u05d7\u05d3\u05e9 \u05de\u05d9\u05d3 \u05e9\u05d0\u05ea\u05d4 \u05e2\u05d5\u05d6\u05d1 \u05d0\u05ea \u05d4\u05d7\u05d6\u05e8\u05d4.",
        "opt_bottom_bar": "\u05e1\u05e8\u05d2\u05dc \u05d4\u05ea\u05d7\u05ea\u05d5\u05df \u05e9\u05dc \u05d4\u05d7\u05dc\u05d5\u05df",
        "opt_bottom_bar_tip": "\u05de\u05d5\u05e4\u05d9\u05e2 \u05de\u05d7\u05d3\u05e9 \u05de\u05d9\u05d3 \u05e9\u05d0\u05ea\u05d4 \u05e2\u05d5\u05d6\u05d1 \u05d0\u05ea \u05d4\u05d7\u05d6\u05e8\u05d4.",
        "opt_scrollbar": "\u05e4\u05e1 \u05d4\u05d2\u05dc\u05d9\u05dc\u05d4 \u05e9\u05dc \u05d4\u05db\u05e8\u05d8\u05d9\u05e1",
        "opt_scrollbar_tip": "\u05d5\u05d9\u05d6\u05d5\u05d0\u05dc\u05d9 \u05d1\u05dc\u05d1\u05d3: \u05e2\u05d3\u05d9\u05d9\u05df \u05d0\u05e4\u05e9\u05e8 \u05dc\u05d2\u05dc\u05d5\u05dc \u05e2\u05dd \u05d2\u05dc\u05d2\u05dc\u05ea \u05d4\u05e2\u05db\u05d1\u05e8. "
        "\u05d4\u05e9\u05d9\u05e0\u05d5\u05d9 \u05e0\u05e8\u05d0\u05d4 \u05d1\u05db\u05e8\u05d8\u05d9\u05e1 \u05d4\u05d1\u05d0.",
        "opt_hard_easy": "\u05d4\u05db\u05e4\u05ea\u05d5\u05e8\u05d9\u05dd \u00ab\u05e7\u05e9\u05d4\u00bb \u05d5\u00ab\u05e7\u05dc\u05d4\u00bb",
        "opt_hard_easy_tip": "\u05de\u05e9\u05d0\u05d9\u05e8 \u05e8\u05e7 \u00ab\u05e9\u05d5\u05d1\u00bb \u05d5\u00ab\u05d8\u05d5\u05d1\u00bb. \u05d2\u05dd \u05e7\u05d9\u05e6\u05d5\u05e8\u05d9 \u05d4\u05de\u05e7\u05dc\u05d3\u05ea "
        "\u05e9\u05dc\u05d4\u05dd \u05e0\u05d7\u05e1\u05de\u05d9\u05dd, \u05db\u05d3\u05d9 \u05e9\u05dc\u05d0 \u05ea\u05e2\u05e0\u05d4 \u05d1\u05d8\u05e2\u05d5\u05ea \u05e2\u05dd \u05db\u05e4\u05ea\u05d5\u05e8 \u05e9\u05d0\u05ea\u05d4 \u05dc\u05d0 \u05e8\u05d5\u05d0\u05d4.",
        "opt_cursor": "\u05e1\u05de\u05df \u05d4\u05e2\u05db\u05d1\u05e8 \u05db\u05d0\u05e9\u05e8 \u05d4\u05d5\u05d0 \u05e0\u05d9\u05d7 \u05dc\u05de\u05e9\u05da:",
        "opt_cursor_tip": "\u05de\u05d5\u05e4\u05d9\u05e2 \u05de\u05d7\u05d3\u05e9 \u05de\u05d9\u05d3 \u05e9\u05d0\u05ea\u05d4 \u05de\u05d6\u05d9\u05d6 \u05d0\u05ea \u05d4\u05e2\u05db\u05d1\u05e8.",
        "opt_cursor_suffix": " \u05e9\u05e0'",
        "opt_auto_start": "\u05d4\u05ea\u05d7\u05dc \u05d0\u05ea \u05d4\u05d7\u05d6\u05e8\u05d4 \u05d0\u05d5\u05d8\u05d5\u05de\u05d8\u05d9\u05ea \u05e2\u05dd \u05e4\u05ea\u05d9\u05d7\u05ea \u05d7\u05d1\u05d9\u05dc\u05d4",
        "opt_auto_start_tip": "\u05e8\u05e7 \u05d0\u05dd \u05d9\u05e9 \u05e7\u05dc\u05e4\u05d9\u05dd \u05de\u05de\u05ea\u05d9\u05e0\u05d9\u05dd. \u05d0\u05dd \u05d0\u05ea\u05d4 \u05e2\u05d5\u05d6\u05d1 \u05d0\u05ea \u05d4\u05d7\u05d6\u05e8\u05d4, "
        "Hider \u05dc\u05d0 \u05d9\u05d7\u05d6\u05d9\u05e8 \u05d0\u05d5\u05ea\u05da \u05d0\u05dc\u05d9\u05d4.",
        "btn_save": "אישור",
        "btn_cancel": "\u05d1\u05d9\u05d8\u05d5\u05dc",
        "btn_defaults": "שחזור ברירות המחדל",
        "saved": "\u05ea\u05e6\u05d5\u05e8\u05ea \u05d4-Hider \u05e0\u05e9\u05de\u05e8\u05d4.",
        "save_failed": "\u05dc\u05d0 \u05e0\u05d9\u05ea\u05df \u05dc\u05e9\u05de\u05d5\u05e8 \u05d0\u05ea \u05ea\u05e6\u05d5\u05e8\u05ea \u05d4-Hider.",
    },
    "fa": {
        "button_hidden": "\u0622\u0646 \u062f\u06a9\u0645\u0647 \u067e\u0646\u0647\u0627\u0646 \u0627\u0633\u062a. \u0641\u0642\u0637 \u0645\u06cc\u200c\u062a\u0648\u0627\u0646\u06cc \u0628\u0627 \u00ab\u062f\u0648\u0628\u0627\u0631\u0647\u00bb \u06cc\u0627 \u00ab\u062e\u0648\u0628\u00bb \u067e\u0627\u0633\u062e \u062f\u0647\u06cc.",
        "hook_error": "Hider \u0628\u0627 \u0645\u0634\u06a9\u0644\u06cc \u0645\u0648\u0627\u062c\u0647 \u0634\u062f \u0648 \u0622\u0646 \u0628\u062e\u0634 \u0631\u0627 \u0628\u0631\u0627\u06cc \u0627\u06cc\u0645\u0646\u06cc \u063a\u06cc\u0631\u0641\u0639\u0627\u0644 \u06a9\u0631\u062f. "
        "\u062a\u0646\u0638\u06cc\u0645\u0627\u062a \u0627\u0641\u0632\u0648\u0646\u0647 \u0631\u0627 \u0628\u0631\u0631\u0633\u06cc \u06a9\u0646.",
        "dialog_title": "Hider",
        "group_review": "\u062d\u06cc\u0646 \u0645\u0631\u0648\u0631\u060c \u067e\u0646\u0647\u0627\u0646 \u06a9\u0646:",
        "group_behaviour": "\u0631\u0641\u062a\u0627\u0631",
        "opt_menu_bar": "\u0646\u0648\u0627\u0631 \u0645\u0646\u0648 (\u0641\u0627\u06cc\u0644\u060c \u0648\u06cc\u0631\u0627\u06cc\u0634\u060c \u0627\u0628\u0632\u0627\u0631\u0647\u0627...)",
        "opt_menu_bar_tip": "\u0628\u0647 \u0645\u062d\u0636 \u062e\u0631\u0648\u062c \u0627\u0632 \u0645\u0631\u0648\u0631 \u062f\u0648\u0628\u0627\u0631\u0647 \u0638\u0627\u0647\u0631 \u0645\u06cc\u200c\u0634\u0648\u062f.",
        "opt_toolbar": "\u0646\u0648\u0627\u0631 \u0627\u0628\u0632\u0627\u0631\u0647\u0627\u06cc \u0628\u0627\u0644\u0627 (\u062f\u0633\u062a\u0647\u200c\u0647\u0627\u060c \u0627\u0641\u0632\u0648\u062f\u0646\u060c \u0645\u0631\u0648\u0631\u060c \u0622\u0645\u0627\u0631)",
        "opt_toolbar_tip": "\u0628\u0647 \u0645\u062d\u0636 \u062e\u0631\u0648\u062c \u0627\u0632 \u0645\u0631\u0648\u0631 \u062f\u0648\u0628\u0627\u0631\u0647 \u0638\u0627\u0647\u0631 \u0645\u06cc\u200c\u0634\u0648\u062f.",
        "opt_bottom_bar": "\u0646\u0648\u0627\u0631 \u067e\u0627\u06cc\u06cc\u0646 \u067e\u0646\u062c\u0631\u0647",
        "opt_bottom_bar_tip": "\u0628\u0647 \u0645\u062d\u0636 \u062e\u0631\u0648\u062c \u0627\u0632 \u0645\u0631\u0648\u0631 \u062f\u0648\u0628\u0627\u0631\u0647 \u0638\u0627\u0647\u0631 \u0645\u06cc\u200c\u0634\u0648\u062f.",
        "opt_scrollbar": "\u0646\u0648\u0627\u0631 \u0627\u0633\u06a9\u0631\u0648\u0644 \u06a9\u0627\u0631\u062a",
        "opt_scrollbar_tip": "\u0641\u0642\u0637 \u0628\u0635\u0631\u06cc: \u0647\u0645\u0686\u0646\u0627\u0646 \u0645\u06cc\u200c\u062a\u0648\u0627\u0646\u06cc \u0628\u0627 \u0686\u0631\u062e \u0645\u0627\u0648\u0633 \u0627\u0633\u06a9\u0631\u0648\u0644 \u06a9\u0646\u06cc. "
        "\u062a\u063a\u06cc\u06cc\u0631 \u062f\u0631 \u06a9\u0627\u0631\u062a \u0628\u0639\u062f\u06cc \u062f\u06cc\u062f\u0647 \u0645\u06cc\u200c\u0634\u0648\u062f.",
        "opt_hard_easy": "\u062f\u06a9\u0645\u0647\u200c\u0647\u0627\u06cc \u00ab\u0633\u062e\u062a\u00bb \u0648 \u00ab\u0622\u0633\u0627\u0646\u00bb",
        "opt_hard_easy_tip": "\u0641\u0642\u0637 \u00ab\u062f\u0648\u0628\u0627\u0631\u0647\u00bb \u0648 \u00ab\u062e\u0648\u0628\u00bb \u0631\u0627 \u0628\u0627\u0642\u06cc \u0645\u06cc\u200c\u06af\u0630\u0627\u0631\u062f. \u06a9\u0644\u06cc\u062f\u0647\u0627\u06cc \u0645\u06cc\u0627\u0646\u0628\u0631 \u0622\u0646\u200c\u0647\u0627 \u0646\u06cc\u0632 "
        "\u0645\u0633\u062f\u0648\u062f \u0645\u06cc\u200c\u0634\u0648\u0646\u062f \u062a\u0627 \u0628\u0647 \u0627\u0634\u062a\u0628\u0627\u0647 \u0628\u0627 \u062f\u06a9\u0645\u0647\u200c\u0627\u06cc \u06a9\u0647 \u0646\u0645\u06cc\u200c\u0628\u06cc\u0646\u06cc \u067e\u0627\u0633\u062e \u0646\u062f\u0647\u06cc.",
        "opt_cursor": "\u0627\u0634\u0627\u0631\u0647\u200c\u06af\u0631 \u0645\u0627\u0648\u0633 \u0647\u0646\u06af\u0627\u0645\u06cc \u06a9\u0647 \u0628\u06cc\u200c\u062d\u0631\u06a9\u062a \u0628\u0645\u0627\u0646\u062f \u0628\u0647 \u0645\u062f\u062a:",
        "opt_cursor_tip": "\u0628\u0647 \u0645\u062d\u0636 \u062d\u0631\u06a9\u062a \u0645\u0627\u0648\u0633 \u0638\u0627\u0647\u0631 \u0645\u06cc\u200c\u0634\u0648\u062f.",
        "opt_cursor_suffix": " \u062b",
        "opt_auto_start": "\u0634\u0631\u0648\u0639 \u062e\u0648\u062f\u06a9\u0627\u0631 \u0645\u0631\u0648\u0631 \u0647\u0646\u06af\u0627\u0645 \u0628\u0627\u0632 \u06a9\u0631\u062f\u0646 \u062f\u0633\u062a\u0647",
        "opt_auto_start_tip": "\u0641\u0642\u0637 \u062f\u0631 \u0635\u0648\u0631\u062a \u0648\u062c\u0648\u062f \u06a9\u0627\u0631\u062a\u200c\u0647\u0627\u06cc \u0633\u0631\u0631\u0633\u06cc\u062f. \u0627\u06af\u0631 \u062e\u0648\u062f\u062a \u0627\u0632 \u0645\u0631\u0648\u0631 \u062e\u0627\u0631\u062c \u0634\u0648\u06cc\u060c "
        "Hider \u062a\u0648 \u0631\u0627 \u0628\u0631\u0646\u0645\u06cc\u200c\u06af\u0631\u062f\u0627\u0646\u062f.",
        "btn_save": "تأیید",
        "btn_cancel": "\u0644\u063a\u0648",
        "btn_defaults": "بازگرداندن مقادیر پیش‌فرض",
        "saved": "\u062a\u0646\u0638\u06cc\u0645\u0627\u062a Hider \u0630\u062e\u06cc\u0631\u0647 \u0634\u062f.",
        "save_failed": "\u0630\u062e\u06cc\u0631\u0647 \u062a\u0646\u0638\u06cc\u0645\u0627\u062a Hider \u0645\u0645\u06a9\u0646 \u0646\u0628\u0648\u062f.",
    },
    "hi": {
        "button_hidden": "\u0935\u0939 \u092c\u091f\u0928 \u091b\u093f\u092a\u093e \u0939\u0941\u0906 \u0939\u0948\u0964 \u0906\u092a \u0915\u0947\u0935\u0932 \u00ab\u092b\u093f\u0930 \u0938\u0947\u00bb \u092f\u093e \u00ab\u0905\u091a\u094d\u091b\u093e\u00bb \u0938\u0947 \u091c\u0935\u093e\u092c \u0926\u0947 \u0938\u0915\u0924\u0947 \u0939\u0948\u0902\u0964",
        "hook_error": "Hider \u0915\u094b \u090f\u0915 \u0938\u092e\u0938\u094d\u092f\u093e \u0906\u0908 \u0914\u0930 \u0938\u0941\u0930\u0915\u094d\u0937\u093e \u0915\u0947 \u0932\u093f\u090f \u0909\u0938 \u0939\u093f\u0938\u094d\u0938\u0947 \u0915\u094b \u092c\u0902\u0926 \u0915\u0930 \u0926\u093f\u092f\u093e \u0917\u092f\u093e\u0964 "
        "\u0910\u0921-\u0911\u0928 \u0915\u0940 \u0915\u0949\u0928\u094d\u092b\u093c\u093f\u0917\u0930\u0947\u0936\u0928 \u091c\u093e\u0902\u091a\u0947\u0902\u0964",
        "dialog_title": "Hider",
        "group_review": "\u0926\u094b\u0939\u0930\u093e\u0928\u0947 \u0915\u0947 \u0926\u094c\u0930\u093e\u0928 \u091b\u093f\u092a\u093e\u090f\u0902:",
        "group_behaviour": "\u0935\u094d\u092f\u0935\u0939\u093e\u0930",
        "opt_menu_bar": "\u092e\u0947\u0928\u0942 \u092a\u091f\u094d\u091f\u0940 (\u092b\u093c\u093e\u0907\u0932, \u0938\u0902\u092a\u093e\u0926\u0928, \u0909\u092a\u0915\u0930\u0923...)",
        "opt_menu_bar_tip": "\u0926\u094b\u0939\u0930\u093e\u0928\u0947 \u0938\u0947 \u092c\u093e\u0939\u0930 \u091c\u093e\u0924\u0947 \u0939\u0940 \u092b\u093f\u0930 \u0926\u093f\u0916\u0924\u0940 \u0939\u0948\u0964",
        "opt_toolbar": "\u0936\u0940\u0930\u094d\u0937 \u091f\u0942\u0932\u092c\u093e\u0930 (\u0921\u0947\u0915, \u091c\u094b\u0921\u093c\u0947\u0902, \u092c\u094d\u0930\u093e\u0909\u091c\u093c, \u0906\u0902\u0915\u0921\u093c\u0947)",
        "opt_toolbar_tip": "\u0926\u094b\u0939\u0930\u093e\u0928\u0947 \u0938\u0947 \u092c\u093e\u0939\u0930 \u091c\u093e\u0924\u0947 \u0939\u0940 \u092b\u093f\u0930 \u0926\u093f\u0916\u0924\u0940 \u0939\u0948\u0964",
        "opt_bottom_bar": "\u0935\u093f\u0902\u0921\u094b \u0915\u0940 \u0928\u093f\u091a\u0932\u0940 \u092a\u091f\u094d\u091f\u0940",
        "opt_bottom_bar_tip": "\u0926\u094b\u0939\u0930\u093e\u0928\u0947 \u0938\u0947 \u092c\u093e\u0939\u0930 \u091c\u093e\u0924\u0947 \u0939\u0940 \u092b\u093f\u0930 \u0926\u093f\u0916\u0924\u0940 \u0939\u0948\u0964",
        "opt_scrollbar": "\u0915\u093e\u0930\u094d\u0921 \u0915\u0940 \u0938\u094d\u0915\u094d\u0930\u094b\u0932\u092c\u093e\u0930",
        "opt_scrollbar_tip": "\u0915\u0947\u0935\u0932 \u0926\u0943\u0936\u094d\u092f: \u0906\u092a \u092e\u093e\u0909\u0938 \u0935\u094d\u0939\u0940\u0932 \u0938\u0947 \u0938\u094d\u0915\u094d\u0930\u094b\u0932 \u0915\u0930 \u0938\u0915\u0924\u0947 \u0939\u0948\u0902\u0964 "
        "\u092c\u0926\u0932\u093e\u0935 \u0905\u0917\u0932\u0947 \u0915\u093e\u0930\u094d\u0921 \u092a\u0930 \u0926\u093f\u0916\u0924\u093e \u0939\u0948\u0964",
        "opt_hard_easy": "\u00ab\u0915\u0920\u093f\u0928\u00bb \u0914\u0930 \u00ab\u0906\u0938\u093e\u0928\u00bb \u092c\u091f\u0928",
        "opt_hard_easy_tip": "\u0915\u0947\u0935\u0932 \u00ab\u092b\u093f\u0930 \u0938\u0947\u00bb \u0914\u0930 \u00ab\u0905\u091a\u094d\u091b\u093e\u00bb \u091b\u094b\u0921\u093c\u0924\u093e \u0939\u0948\u0964 \u0909\u0928\u0915\u0947 \u0915\u0940\u092c\u094b\u0930\u094d\u0921 "
        "\u0936\u0949\u0930\u094d\u091f\u0915\u091f \u092d\u0940 \u092c\u094d\u0932\u0949\u0915 \u0939\u094b \u091c\u093e\u0924\u0947 \u0939\u0948\u0902, \u0924\u093e\u0915\u093f \u0906\u092a \u0917\u0932\u0924\u0940 \u0938\u0947 \u0905\u0926\u0943\u0936\u094d\u092f \u092c\u091f\u0928 \u0938\u0947 \u091c\u0935\u093e\u092c \u0928 \u0926\u0947\u0902\u0964",
        "opt_cursor": "\u092e\u093e\u0909\u0938 \u092a\u0949\u0907\u0902\u091f\u0930 \u091c\u092c \u0907\u0924\u0928\u0940 \u0926\u0947\u0930 \u0924\u0915 \u0938\u094d\u0925\u093f\u0930 \u0930\u0939\u0947:",
        "opt_cursor_tip": "\u092e\u093e\u0909\u0938 \u0939\u093f\u0932\u093e\u0924\u0947 \u0939\u0940 \u092b\u093f\u0930 \u0926\u093f\u0916\u0924\u093e \u0939\u0948\u0964",
        "opt_cursor_suffix": " \u0938\u0947\u0915\u0902\u0921",
        "opt_auto_start": "\u0921\u0947\u0915 \u0916\u094b\u0932\u0928\u0947 \u092a\u0930 \u0938\u094d\u0935\u0924\u0903 \u0926\u094b\u0939\u0930\u093e\u0928\u093e \u0936\u0941\u0930\u0942 \u0915\u0930\u0947\u0902",
        "opt_auto_start_tip": "\u0915\u0947\u0935\u0932 \u092f\u0926\u093f \u0932\u0902\u092c\u093f\u0924 \u0915\u093e\u0930\u094d\u0921 \u0939\u094b\u0902\u0964 \u092f\u0926\u093f \u0906\u092a \u0916\u0941\u0926 \u0926\u094b\u0939\u0930\u093e\u0928\u0947 \u0938\u0947 \u092c\u093e\u0939\u0930 \u0928\u093f\u0915\u0932\u0924\u0947 \u0939\u0948\u0902, "
        "\u0924\u094b Hider \u0906\u092a\u0915\u094b \u0935\u093e\u092a\u0938 \u0928\u0939\u0940\u0902 \u0921\u093e\u0932\u0924\u093e\u0964",
        "btn_save": "स्वीकार करें",
        "btn_cancel": "\u0930\u0926\u094d\u0926 \u0915\u0930\u0947\u0902",
        "btn_defaults": "डिफ़ॉल्ट मान पुनर्स्थापित करें",
        "saved": "Hider \u0915\u0949\u0928\u094d\u092b\u093c\u093f\u0917\u0930\u0947\u0936\u0928 \u0938\u0939\u0947\u091c\u093e \u0917\u092f\u093e\u0964",
        "save_failed": "Hider \u0915\u0940 \u0915\u0949\u0928\u094d\u092b\u093c\u093f\u0917\u0930\u0947\u0936\u0928 \u0938\u0939\u0947\u091c\u0940 \u0928\u0939\u0940\u0902 \u091c\u093e \u0938\u0915\u0940\u0964",
    },
    "th": {
        "button_hidden": "\u0e1b\u0e38\u0e48\u0e21\u0e19\u0e35\u0e49\u0e16\u0e39\u0e01\u0e0b\u0e48\u0e2d\u0e19\u0e2d\u0e22\u0e39\u0e48 \u0e04\u0e38\u0e13\u0e2a\u0e32\u0e21\u0e32\u0e23\u0e16\u0e15\u0e2d\u0e1a\u0e44\u0e14\u0e49\u0e40\u0e1e\u0e35\u0e22\u0e07 \u00ab\u0e2d\u0e35\u0e01\u0e04\u0e23\u0e31\u0e49\u0e07\u00bb \u0e2b\u0e23\u0e37\u0e2d \u00ab\u0e14\u0e35\u00bb",
        "hook_error": "Hider \u0e1e\u0e1a\u0e1b\u0e31\u0e0d\u0e2b\u0e32\u0e41\u0e25\u0e30\u0e1b\u0e34\u0e14\u0e43\u0e0a\u0e49\u0e07\u0e32\u0e19\u0e2a\u0e48\u0e27\u0e19\u0e19\u0e31\u0e49\u0e19\u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e04\u0e27\u0e32\u0e21\u0e1b\u0e25\u0e2d\u0e14\u0e20\u0e31\u0e22 "
        "\u0e42\u0e1b\u0e23\u0e14\u0e15\u0e23\u0e27\u0e08\u0e2a\u0e2d\u0e1a\u0e01\u0e32\u0e23\u0e15\u0e31\u0e49\u0e07\u0e04\u0e48\u0e32\u0e02\u0e2d\u0e07\u0e2a\u0e48\u0e27\u0e19\u0e40\u0e2a\u0e23\u0e34\u0e21",
        "dialog_title": "Hider",
        "group_review": "\u0e0b\u0e48\u0e2d\u0e19\u0e23\u0e30\u0e2b\u0e27\u0e48\u0e32\u0e07\u0e01\u0e32\u0e23\u0e17\u0e1a\u0e17\u0e27\u0e19:",
        "group_behaviour": "\u0e1e\u0e24\u0e15\u0e34\u0e01\u0e23\u0e23\u0e21",
        "opt_menu_bar": "\u0e41\u0e16\u0e1a\u0e40\u0e21\u0e19\u0e39 (\u0e44\u0e1f\u0e25\u0e4c, \u0e41\u0e01\u0e49\u0e44\u0e02, \u0e40\u0e04\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e21\u0e37\u0e2d...)",
        "opt_menu_bar_tip": "\u0e08\u0e30\u0e01\u0e25\u0e31\u0e1a\u0e21\u0e32\u0e17\u0e31\u0e19\u0e17\u0e35\u0e40\u0e21\u0e37\u0e48\u0e2d\u0e2d\u0e2d\u0e01\u0e08\u0e32\u0e01\u0e01\u0e32\u0e23\u0e17\u0e1a\u0e17\u0e27\u0e19",
        "opt_toolbar": "\u0e41\u0e16\u0e1a\u0e40\u0e04\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e21\u0e37\u0e2d\u0e14\u0e49\u0e32\u0e19\u0e1a\u0e19 (\u0e2a\u0e33\u0e23\u0e31\u0e1a, \u0e40\u0e1e\u0e34\u0e48\u0e21, \u0e40\u0e23\u0e35\u0e22\u0e01\u0e14\u0e39, \u0e2a\u0e16\u0e34\u0e15\u0e34)",
        "opt_toolbar_tip": "\u0e08\u0e30\u0e01\u0e25\u0e31\u0e1a\u0e21\u0e32\u0e17\u0e31\u0e19\u0e17\u0e35\u0e40\u0e21\u0e37\u0e48\u0e2d\u0e2d\u0e2d\u0e01\u0e08\u0e32\u0e01\u0e01\u0e32\u0e23\u0e17\u0e1a\u0e17\u0e27\u0e19",
        "opt_bottom_bar": "\u0e41\u0e16\u0e1a\u0e14\u0e49\u0e32\u0e19\u0e25\u0e48\u0e32\u0e07\u0e02\u0e2d\u0e07\u0e2b\u0e19\u0e49\u0e32\u0e15\u0e48\u0e32\u0e07",
        "opt_bottom_bar_tip": "\u0e08\u0e30\u0e01\u0e25\u0e31\u0e1a\u0e21\u0e32\u0e17\u0e31\u0e19\u0e17\u0e35\u0e40\u0e21\u0e37\u0e48\u0e2d\u0e2d\u0e2d\u0e01\u0e08\u0e32\u0e01\u0e01\u0e32\u0e23\u0e17\u0e1a\u0e17\u0e27\u0e19",
        "opt_scrollbar": "\u0e41\u0e16\u0e1a\u0e40\u0e25\u0e37\u0e48\u0e2d\u0e19\u0e02\u0e2d\u0e07\u0e01\u0e32\u0e23\u0e4c\u0e14",
        "opt_scrollbar_tip": "\u0e40\u0e1b\u0e47\u0e19\u0e40\u0e1e\u0e35\u0e22\u0e07\u0e20\u0e32\u0e1e: \u0e22\u0e31\u0e07\u0e40\u0e25\u0e37\u0e48\u0e2d\u0e19\u0e14\u0e49\u0e27\u0e22\u0e25\u0e49\u0e2d\u0e40\u0e21\u0e32\u0e2a\u0e4c\u0e44\u0e14\u0e49 "
        "\u0e01\u0e32\u0e23\u0e40\u0e1b\u0e25\u0e35\u0e48\u0e22\u0e19\u0e08\u0e30\u0e21\u0e35\u0e1c\u0e25\u0e01\u0e31\u0e1a\u0e01\u0e32\u0e23\u0e4c\u0e14\u0e16\u0e31\u0e14\u0e44\u0e1b",
        "opt_hard_easy": "\u0e1b\u0e38\u0e48\u0e21 \u00ab\u0e22\u0e32\u0e01\u00bb \u0e41\u0e25\u0e30 \u00ab\u0e07\u0e48\u0e32\u0e22\u00bb",
        "opt_hard_easy_tip": "\u0e40\u0e2b\u0e25\u0e37\u0e2d\u0e40\u0e1e\u0e35\u0e22\u0e07 \u00ab\u0e2d\u0e35\u0e01\u0e04\u0e23\u0e31\u0e49\u0e07\u00bb \u0e41\u0e25\u0e30 \u00ab\u0e14\u0e35\u00bb \u0e1b\u0e38\u0e48\u0e21\u0e25\u0e31\u0e14\u0e14\u0e48\u0e27\u0e19\u0e02\u0e2d\u0e07\u0e21\u0e31\u0e19\u0e01\u0e47 "
        "\u0e16\u0e39\u0e01\u0e1a\u0e25\u0e47\u0e2d\u0e01\u0e14\u0e49\u0e27\u0e22 \u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e44\u0e21\u0e48\u0e43\u0e2b\u0e49\u0e15\u0e2d\u0e1a\u0e42\u0e14\u0e22\u0e1a\u0e31\u0e07\u0e40\u0e2d\u0e34\u0e0d\u0e14\u0e49\u0e27\u0e22\u0e1b\u0e38\u0e48\u0e21\u0e17\u0e35\u0e48\u0e21\u0e2d\u0e07\u0e44\u0e21\u0e48\u0e40\u0e2b\u0e47\u0e19",
        "opt_cursor": "\u0e15\u0e31\u0e27\u0e0a\u0e35\u0e49\u0e40\u0e21\u0e32\u0e2a\u0e4c\u0e40\u0e21\u0e37\u0e48\u0e2d\u0e2b\u0e22\u0e38\u0e14\u0e19\u0e34\u0e48\u0e07\u0e40\u0e1b\u0e47\u0e19\u0e40\u0e27\u0e25\u0e32:",
        "opt_cursor_tip": "\u0e08\u0e30\u0e01\u0e25\u0e31\u0e1a\u0e21\u0e32\u0e17\u0e31\u0e19\u0e17\u0e35\u0e40\u0e21\u0e37\u0e48\u0e2d\u0e02\u0e22\u0e31\u0e1a\u0e40\u0e21\u0e32\u0e2a\u0e4c",
        "opt_cursor_suffix": " \u0e27\u0e34",
        "opt_auto_start": "\u0e40\u0e23\u0e34\u0e48\u0e21\u0e01\u0e32\u0e23\u0e17\u0e1a\u0e17\u0e27\u0e19\u0e2d\u0e31\u0e15\u0e42\u0e19\u0e21\u0e31\u0e15\u0e34\u0e40\u0e21\u0e37\u0e48\u0e2d\u0e40\u0e1b\u0e34\u0e14\u0e2a\u0e33\u0e23\u0e31\u0e1a",
        "opt_auto_start_tip": "\u0e40\u0e09\u0e1e\u0e32\u0e30\u0e40\u0e21\u0e37\u0e48\u0e2d\u0e21\u0e35\u0e01\u0e32\u0e23\u0e4c\u0e14\u0e04\u0e23\u0e1a\u0e01\u0e33\u0e2b\u0e19\u0e14 \u0e16\u0e49\u0e32\u0e04\u0e38\u0e13\u0e2d\u0e2d\u0e01\u0e08\u0e32\u0e01\u0e01\u0e32\u0e23\u0e17\u0e1a\u0e17\u0e27\u0e19\u0e40\u0e2d\u0e07 "
        "Hider \u0e08\u0e30\u0e44\u0e21\u0e48\u0e19\u0e33\u0e04\u0e38\u0e13\u0e01\u0e25\u0e31\u0e1a\u0e40\u0e02\u0e49\u0e32\u0e44\u0e1b\u0e2d\u0e35\u0e01",
        "btn_save": "ยอมรับ",
        "btn_cancel": "\u0e22\u0e01\u0e40\u0e25\u0e34\u0e01",
        "btn_defaults": "คืนค่าเริ่มต้น",
        "saved": "\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01\u0e01\u0e32\u0e23\u0e15\u0e31\u0e49\u0e07\u0e04\u0e48\u0e32 Hider \u0e41\u0e25\u0e49\u0e27",
        "save_failed": "\u0e44\u0e21\u0e48\u0e2a\u0e32\u0e21\u0e32\u0e23\u0e16\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01\u0e01\u0e32\u0e23\u0e15\u0e31\u0e49\u0e07\u0e04\u0e48\u0e32 Hider \u0e44\u0e14\u0e49",
    },
    "ja": {
        "button_hidden": "\u305d\u306e\u30dc\u30bf\u30f3\u306f\u975e\u8868\u793a\u3067\u3059\u3002\u300c\u3082\u3046\u4e00\u5ea6\u300d\u304b\u300c\u826f\u3044\u300d\u3067\u3057\u304b\u56de\u7b54\u3067\u304d\u307e\u305b\u3093\u3002",
        "hook_error": "Hider\u3067\u554f\u984c\u304c\u767a\u751f\u3057\u305f\u305f\u3081\u3001\u5b89\u5168\u306e\u305f\u3081\u305d\u306e\u6a5f\u80fd\u3092\u7121\u52b9\u306b\u3057\u307e\u3057\u305f\u3002"
        "\u30a2\u30c9\u30aa\u30f3\u306e\u8a2d\u5b9a\u3092\u78ba\u8a8d\u3057\u3066\u304f\u3060\u3055\u3044\u3002",
        "dialog_title": "Hider",
        "group_review": "\u5fa9\u7fd2\u4e2d\u306b\u975e\u8868\u793a\u306b\u3059\u308b:",
        "group_behaviour": "\u52d5\u4f5c",
        "opt_menu_bar": "\u30e1\u30cb\u30e5\u30fc\u30d0\u30fc\uff08\u30d5\u30a1\u30a4\u30eb\u3001\u7de8\u96c6\u3001\u30c4\u30fc\u30eb...\uff09",
        "opt_menu_bar_tip": "\u5fa9\u7fd2\u3092\u7d42\u3048\u308b\u3068\u3059\u3050\u306b\u518d\u8868\u793a\u3055\u308c\u307e\u3059\u3002",
        "opt_toolbar": "\u4e0a\u90e8\u30c4\u30fc\u30eb\u30d0\u30fc\uff08\u30c7\u30c3\u30ad\u3001\u8ffd\u52a0\u3001\u53c2\u7167\u3001\u7d71\u8a08\uff09",
        "opt_toolbar_tip": "\u5fa9\u7fd2\u3092\u7d42\u3048\u308b\u3068\u3059\u3050\u306b\u518d\u8868\u793a\u3055\u308c\u307e\u3059\u3002",
        "opt_bottom_bar": "\u30a6\u30a3\u30f3\u30c9\u30a6\u306e\u4e0b\u90e8\u30d0\u30fc",
        "opt_bottom_bar_tip": "\u5fa9\u7fd2\u3092\u7d42\u3048\u308b\u3068\u3059\u3050\u306b\u518d\u8868\u793a\u3055\u308c\u307e\u3059\u3002",
        "opt_scrollbar": "\u30ab\u30fc\u30c9\u306e\u30b9\u30af\u30ed\u30fc\u30eb\u30d0\u30fc",
        "opt_scrollbar_tip": "\u898b\u305f\u76ee\u306e\u307f\u3067\u3059\uff1a\u30de\u30a6\u30b9\u30db\u30a4\u30fc\u30eb\u3067\u306e\u30b9\u30af\u30ed\u30fc\u30eb\u306f\u53ef\u80fd\u3067\u3059\u3002"
        "\u5909\u66f4\u306f\u6b21\u306e\u30ab\u30fc\u30c9\u3067\u53cd\u6620\u3055\u308c\u307e\u3059\u3002",
        "opt_hard_easy": "\u300c\u96e3\u3057\u3044\u300d\u3068\u300c\u7c21\u5358\u300d\u30dc\u30bf\u30f3",
        "opt_hard_easy_tip": "\u300c\u3082\u3046\u4e00\u5ea6\u300d\u3068\u300c\u826f\u3044\u300d\u306e\u307f\u6b8b\u3057\u307e\u3059\u3002\u30b7\u30e7\u30fc\u30c8\u30ab\u30c3\u30c8\u30ad\u30fc\u3082"
        "\u30d6\u30ed\u30c3\u30af\u3055\u308c\u308b\u306e\u3067\u3001\u898b\u3048\u306a\u3044\u30dc\u30bf\u30f3\u3067\u8aa4\u3063\u3066\u56de\u7b54\u3059\u308b\u3053\u3068\u306f\u3042\u308a\u307e\u305b\u3093\u3002",
        "opt_cursor": "\u30de\u30a6\u30b9\u30ab\u30fc\u30bd\u30eb\u304c\u4ee5\u4e0b\u306e\u9593\u52d5\u304b\u306a\u3044\u3068\u304d:",
        "opt_cursor_tip": "\u30de\u30a6\u30b9\u3092\u52d5\u304b\u3059\u3068\u3059\u3050\u306b\u518d\u8868\u793a\u3055\u308c\u307e\u3059\u3002",
        "opt_cursor_suffix": " \u79d2",
        "opt_auto_start": "\u30c7\u30c3\u30ad\u3092\u958b\u3044\u305f\u3068\u304d\u306b\u81ea\u52d5\u3067\u5fa9\u7fd2\u3092\u958b\u59cb",
        "opt_auto_start_tip": "\u671f\u9650\u304c\u6765\u305f\u30ab\u30fc\u30c9\u304c\u3042\u308b\u5834\u5408\u306e\u307f\u3002\u81ea\u5206\u3067\u5fa9\u7fd2\u3092\u7d42\u3048\u305f\u5834\u5408\u3001"
        "Hider\u306f\u518d\u3073\u623b\u3057\u307e\u305b\u3093\u3002",
        "btn_save": "OK",
        "btn_cancel": "\u30ad\u30e3\u30f3\u30bb\u30eb",
        "btn_defaults": "既定値に戻す",
        "saved": "Hider\u306e\u8a2d\u5b9a\u3092\u4fdd\u5b58\u3057\u307e\u3057\u305f\u3002",
        "save_failed": "Hider\u306e\u8a2d\u5b9a\u3092\u4fdd\u5b58\u3067\u304d\u307e\u305b\u3093\u3067\u3057\u305f\u3002",
    },
    "ko": {
        "button_hidden": "\uc774 \ubc84\ud2bc\uc740 \uc228\uaca8\uc838 \uc788\uc2b5\ub2c8\ub2e4. \u00ab\ub2e4\uc2dc\u00bb \ub610\ub294 \u00ab\uc88b\uc74c\u00bb\uc73c\ub85c\ub9cc \ub2f5\ud560 \uc218 \uc788\uc2b5\ub2c8\ub2e4.",
        "hook_error": "Hider\uac00 \ubb38\uc81c\ub97c \ubc1c\uacac\ud558\uc5ec \uc548\uc804\uc744 \uc704\ud574 \ud574\ub2f9 \uae30\ub2a5\uc744 \ube44\ud65c\uc131\ud654\ud588\uc2b5\ub2c8\ub2e4. "
        "\ubd80\uac00\uae30\ub2a5 \uc124\uc815\uc744 \ud655\uc778\ud558\uc138\uc694.",
        "dialog_title": "Hider",
        "group_review": "\ubcf5\uc2b5 \uc911 \uc228\uae30\uae30:",
        "group_behaviour": "\ub3d9\uc791",
        "opt_menu_bar": "\uba54\ub274\ub0a0 \ub9c9\ub300(\ud30c\uc77c, \ud3b8\uc9d1, \ub3c4\uad6c...)",
        "opt_menu_bar_tip": "\ubcf5\uc2b5\uc744 \ub9c8\uce58\uba74 \ubc14\ub85c \ub2e4\uc2dc \ub098\ud0c0\ub0a9\ub2c8\ub2e4.",
        "opt_toolbar": "\uc0c1\ub2e8 \ub3c4\uad6c\ubaa8\uc74c(\ub371, \ucd94\uac00, \ucc3e\uc544\ubcf4\uae30, \ud1b5\uacc4)",
        "opt_toolbar_tip": "\ubcf5\uc2b5\uc744 \ub9c8\uce58\uba74 \ubc14\ub85c \ub2e4\uc2dc \ub098\ud0c0\ub0a9\ub2c8\ub2e4.",
        "opt_bottom_bar": "\ucc3d \ud558\ub2e8 \ub9c9\ub300",
        "opt_bottom_bar_tip": "\ubcf5\uc2b5\uc744 \ub9c8\uce58\uba74 \ubc14\ub85c \ub2e4\uc2dc \ub098\ud0c0\ub0a9\ub2c8\ub2e4.",
        "opt_scrollbar": "\uce74\ub4dc \uc2a4\ud06c\ub864\ubc14",
        "opt_scrollbar_tip": "\uc2dc\uac01\uc801\uc73c\ub85c\ub9cc \uc228\uaca8\uc9d1\ub2c8\ub2e4: \ub9c8\uc6b0\uc2a4 \ud720\ub85c \uc5ec\uc804\ud788 \uc2a4\ud06c\ub864\ud560 \uc218 \uc788\uc2b5\ub2c8\ub2e4. "
        "\ubcc0\uacbd\uc0ac\ud56d\uc740 \ub2e4\uc74c \uce74\ub4dc\uc5d0\uc11c \ub098\ud0c0\ub0a9\ub2c8\ub2e4.",
        "opt_hard_easy": "\u00ab\uc5b4\ub824\uc6c0\u00bb \ubc0f \u00ab\uc26c\uc6c0\u00bb \ubc84\ud2bc",
        "opt_hard_easy_tip": "\u00ab\ub2e4\uc2dc\u00bb\uc640 \u00ab\uc88b\uc74c\u00bb\ub9cc \ub0a8\uae41\ub2c8\ub2e4. \ud574\ub2f9 \ub2e8\ucd95\ud0a4\ub3c4 "
        "\ucc28\ub2e8\ub418\uc5b4 \ubcf4\uc774\uc9c0 \uc54a\ub294 \ubc84\ud2bc\uc73c\ub85c \uc2e4\uc218\ub85c \ub2f5\ud558\ub294 \uc77c\uc774 \uc5c6\uc2b5\ub2c8\ub2e4.",
        "opt_cursor": "\ub9c8\uc6b0\uc2a4 \ucee4\uc11c\uac00 \ub2e4\uc74c \ub3d9\uc548 \uc815\uc9c0\ud574 \uc788\uc744 \ub54c:",
        "opt_cursor_tip": "\ub9c8\uc6b0\uc2a4\ub97c \uc6c0\uc9c1\uc774\uba74 \ubc14\ub85c \ub2e4\uc2dc \ub098\ud0c0\ub0a9\ub2c8\ub2e4.",
        "opt_cursor_suffix": " \ucd08",
        "opt_auto_start": "\ub371\uc744 \uc5f4\uba74 \uc790\ub3d9\uc73c\ub85c \ubcf5\uc2b5 \uc2dc\uc791",
        "opt_auto_start_tip": "\ub9c8\uac10\uc774 \ub41c \uce74\ub4dc\uac00 \uc788\uc744 \ub54c\ub9cc \ud574\ub2f9\ub429\ub2c8\ub2e4. \uc9c1\uc811 \ubcf5\uc2b5\uc744 \ub098\uac00\uba74 "
        "Hider\uac00 \ub2e4\uc2dc \ub370\ub824\ub2e4\ub193\uc9c0 \uc54a\uc2b5\ub2c8\ub2e4.",
        "btn_save": "확인",
        "btn_cancel": "\ucde8\uc18c",
        "btn_defaults": "기본값 복원",
        "saved": "Hider \uc124\uc815\uc774 \uc800\uc7a5\ub418\uc5c8\uc2b5\ub2c8\ub2e4.",
        "save_failed": "Hider \uc124\uc815\uc744 \uc800\uc7a5\ud560 \uc218 \uc5c6\uc5c8\uc2b5\ub2c8\ub2e4.",
    },
    "zh_CN": {
        "button_hidden": "\u8be5\u6309\u94ae\u5df2\u9690\u85cf\u3002\u4f60\u53ea\u80fd\u9009\u62e9\u00ab\u91cd\u6765\u00bb\u6216\u00ab\u826f\u597d\u00bb\u56de\u7b54\u3002",
        "hook_error": "Hider \u9047\u5230\u4e86\u95ee\u9898\uff0c\u4e3a\u4e86\u5b89\u5168\u5df2\u7981\u7528\u8be5\u90e8\u5206\u3002"
        "\u8bf7\u68c0\u67e5\u63d2\u4ef6\u7684\u914d\u7f6e\u3002",
        "dialog_title": "Hider",
        "group_review": "\u590d\u4e60\u65f6\u9690\u85cf\uff1a",
        "group_behaviour": "\u884c\u4e3a",
        "opt_menu_bar": "\u83dc\u5355\u680f\uff08\u6587\u4ef6\u3001\u7f16\u8f91\u3001\u5de5\u5177...\uff09",
        "opt_menu_bar_tip": "\u9000\u51fa\u590d\u4e60\u540e\u4f1a\u7acb\u5373\u91cd\u65b0\u51fa\u73b0\u3002",
        "opt_toolbar": "\u9876\u90e8\u5de5\u5177\u680f\uff08\u724c\u7ec4\u3001\u6dfb\u52a0\u3001\u6d4f\u89c8\u3001\u7edf\u8ba1\uff09",
        "opt_toolbar_tip": "\u9000\u51fa\u590d\u4e60\u540e\u4f1a\u7acb\u5373\u91cd\u65b0\u51fa\u73b0\u3002",
        "opt_bottom_bar": "\u7a97\u53e3\u5e95\u90e8\u680f",
        "opt_bottom_bar_tip": "\u9000\u51fa\u590d\u4e60\u540e\u4f1a\u7acb\u5373\u91cd\u65b0\u51fa\u73b0\u3002",
        "opt_scrollbar": "\u5361\u7247\u7684\u6eda\u52a8\u6761",
        "opt_scrollbar_tip": "\u4ec5\u4e3a\u89c6\u89c9\u6548\u679c\uff1a\u4ecd\u53ef\u4ee5\u7528\u9f20\u6807\u6eda\u8f6e\u6eda\u52a8\u3002"
        "\u66f4\u6539\u5c06\u5728\u4e0b\u4e00\u5f20\u5361\u7247\u4e2d\u751f\u6548\u3002",
        "opt_hard_easy": "\u00ab\u56f0\u96be\u00bb\u548c\u00ab\u5bb9\u6613\u00bb\u6309\u94ae",
        "opt_hard_easy_tip": "\u53ea\u4fdd\u7559\u00ab\u91cd\u6765\u00bb\u548c\u00ab\u826f\u597d\u00bb\u3002\u76f8\u5e94\u7684\u5feb\u6377\u952e\u4e5f"
        "\u4f1a\u88ab\u5c4f\u853d\uff0c\u4ee5\u514d\u4f60\u4e0d\u5c0f\u5fc3\u7528\u4e00\u4e2a\u770b\u4e0d\u5230\u7684\u6309\u94ae\u56de\u7b54\u3002",
        "opt_cursor": "\u9f20\u6807\u6307\u9488\u9759\u6b62\u591a\u4e45\u540e\u9690\u85cf\uff1a",
        "opt_cursor_tip": "\u79fb\u52a8\u9f20\u6807\u540e\u4f1a\u7acb\u5373\u91cd\u65b0\u51fa\u73b0\u3002",
        "opt_cursor_suffix": " \u79d2",
        "opt_auto_start": "\u6253\u5f00\u724c\u7ec4\u65f6\u81ea\u52a8\u5f00\u59cb\u590d\u4e60",
        "opt_auto_start_tip": "\u4ec5\u5f53\u6709\u5f85\u590d\u4e60\u5361\u7247\u65f6\u3002\u5982\u679c\u662f\u4f60\u81ea\u5df1\u9000\u51fa\u590d\u4e60\uff0c"
        "Hider \u4e0d\u4f1a\u628a\u4f60\u91cd\u65b0\u5e26\u56de\u53bb\u3002",
        "btn_save": "确定",
        "btn_cancel": "\u53d6\u6d88",
        "btn_defaults": "恢复默认值",
        "saved": "Hider \u914d\u7f6e\u5df2\u4fdd\u5b58\u3002",
        "save_failed": "\u65e0\u6cd5\u4fdd\u5b58 Hider \u7684\u914d\u7f6e\u3002",
    },
    "zh_TW": {
        "button_hidden": "\u8a72\u6309\u9215\u5df2\u96b1\u85cf\u3002\u4f60\u53ea\u80fd\u9078\u64c7\u00ab\u91cd\u4f86\u00bb\u6216\u00ab\u826f\u597d\u00bb\u56de\u7b54\u3002",
        "hook_error": "Hider \u9047\u5230\u554f\u984c\uff0c\u70ba\u4e86\u5b89\u5168\u5df2\u505c\u7528\u8a72\u90e8\u5206\u3002"
        "\u8acb\u6aa2\u67e5\u5916\u639b\u7684\u8a2d\u5b9a\u3002",
        "dialog_title": "Hider",
        "group_review": "\u5fa9\u7fd2\u6642\u96b1\u85cf\uff1a",
        "group_behaviour": "\u884c\u70ba",
        "opt_menu_bar": "\u529f\u80fd\u8868\u5217\uff08\u6a94\u6848\u3001\u7de8\u8f2f\u3001\u5de5\u5177...\uff09",
        "opt_menu_bar_tip": "\u96e2\u958b\u5fa9\u7fd2\u5f8c\u6703\u7acb\u5373\u91cd\u65b0\u986f\u793a\u3002",
        "opt_toolbar": "\u9802\u90e8\u5de5\u5177\u5217\uff08\u724c\u7d44\u3001\u65b0\u589e\u3001\u700f\u89bd\u3001\u7d71\u8a08\uff09",
        "opt_toolbar_tip": "\u96e2\u958b\u5fa9\u7fd2\u5f8c\u6703\u7acb\u5373\u91cd\u65b0\u986f\u793a\u3002",
        "opt_bottom_bar": "\u8996\u7a97\u5e95\u90e8\u5217",
        "opt_bottom_bar_tip": "\u96e2\u958b\u5fa9\u7fd2\u5f8c\u6703\u7acb\u5373\u91cd\u65b0\u986f\u793a\u3002",
        "opt_scrollbar": "\u5361\u7247\u7684\u6372\u52d5\u689d",
        "opt_scrollbar_tip": "\u50c5\u70ba\u8996\u89ba\u6548\u679c\uff1a\u4ecd\u53ef\u7528\u6ed1\u9f20\u6eda\u8f2a\u6372\u52d5\u3002"
        "\u8b8a\u66f4\u5c07\u5728\u4e0b\u4e00\u5f35\u5361\u7247\u4e2d\u751f\u6548\u3002",
        "opt_hard_easy": "\u00ab\u56f0\u96e3\u00bb\u8207\u00ab\u5bb9\u6613\u00bb\u6309\u9215",
        "opt_hard_easy_tip": "\u50c5\u4fdd\u7559\u00ab\u91cd\u4f86\u00bb\u8207\u00ab\u826f\u597d\u00bb\u3002\u76f8\u61c9\u7684\u5feb\u6377\u9375\u4e5f"
        "\u6703\u88ab\u963b\u64cb\uff0c\u4ee5\u514d\u4f60\u4e0d\u5c0f\u5fc3\u7528\u770b\u4e0d\u5230\u7684\u6309\u9215\u56de\u7b54\u3002",
        "opt_cursor": "\u6ed1\u9f20\u6307\u91dd\u975c\u6b62\u8d85\u904e\u4ee5\u4e0b\u6642\u9593\u5f8c\u96b1\u85cf\uff1a",
        "opt_cursor_tip": "\u79fb\u52d5\u6ed1\u9f20\u5f8c\u6703\u7acb\u5373\u91cd\u65b0\u986f\u793a\u3002",
        "opt_cursor_suffix": " \u79d2",
        "opt_auto_start": "\u6253\u958b\u724c\u7d44\u6642\u81ea\u52d5\u958b\u59cb\u5fa9\u7fd2",
        "opt_auto_start_tip": "\u50c5\u7576\u6709\u5230\u671f\u5361\u7247\u6642\u3002\u5982\u679c\u662f\u4f60\u81ea\u5df1\u96e2\u958b\u5fa9\u7fd2\uff0c"
        "Hider \u4e0d\u6703\u628a\u4f60\u91cd\u65b0\u5e36\u56de\u53bb\u3002",
        "btn_save": "確定",
        "btn_cancel": "\u53d6\u6d88",
        "btn_defaults": "還原預設值",
        "saved": "Hider \u8a2d\u5b9a\u5df2\u5132\u5b58\u3002",
        "save_failed": "\u7121\u6cd5\u5132\u5b58 Hider \u7684\u8a2d\u5b9a\u3002",
    },
    "vi": {
        "button_hidden": "N\u00fat \u0111\u00f3 \u0111ang b\u1ecb \u1ea9n. B\u1ea1n ch\u1ec9 c\u00f3 th\u1ec3 tr\u1ea3 l\u1eddi \u00abL\u1eb7p l\u1ea1i\u00bb ho\u1eb7c \u00abT\u1ed1t\u00bb.",
        "hook_error": "Hider g\u1eb7p s\u1ef1 c\u1ed1 v\u00e0 \u0111\u00e3 t\u1eaft ph\u1ea7n \u0111\u00f3 v\u00ec l\u00fd do an to\u00e0n. "
        "H\u00e3y ki\u1ec3m tra c\u1ea5u h\u00ecnh c\u1ee7a ti\u1ec7n \u00edch.",
        "dialog_title": "Hider",
        "group_review": "\u1ea8n trong khi \u00f4n t\u1eadp:",
        "group_behaviour": "H\u00e0nh vi",
        "opt_menu_bar": "Thanh menu (T\u1eadp tin, Ch\u1ec9nh s\u1eeda, C\u00f4ng c\u1ee5...)",
        "opt_menu_bar_tip": "Hi\u1ec7n l\u1ea1i ngay khi b\u1ea1n r\u1eddi \u00f4n t\u1eadp.",
        "opt_toolbar": "Thanh c\u00f4ng c\u1ee5 tr\u00ean c\u00f9ng (B\u1ed9 th\u1ebb, Th\u00eam, Duy\u1ec7t, Th\u1ed1ng k\u00ea)",
        "opt_toolbar_tip": "Hi\u1ec7n l\u1ea1i ngay khi b\u1ea1n r\u1eddi \u00f4n t\u1eadp.",
        "opt_bottom_bar": "Thanh d\u01b0\u1edbi c\u1ee7a c\u1eeda s\u1ed5",
        "opt_bottom_bar_tip": "Hi\u1ec7n l\u1ea1i ngay khi b\u1ea1n r\u1eddi \u00f4n t\u1eadp.",
        "opt_scrollbar": "Thanh cu\u1ed9n c\u1ee7a th\u1ebb",
        "opt_scrollbar_tip": "Ch\u1ec9 v\u1ec1 h\u00ecnh th\u1ee9c: b\u1ea1n v\u1eabn c\u00f3 th\u1ec3 cu\u1ed9n b\u1eb1ng b\u00e1nh xe chu\u1ed9t. "
        "Thay \u0111\u1ed5i \u00e1p d\u1ee5ng t\u1eeb th\u1ebb ti\u1ebfp theo.",
        "opt_hard_easy": "N\u00fat \u00abKh\u00f3\u00bb v\u00e0 \u00abD\u1ec5\u00bb",
        "opt_hard_easy_tip": "Ch\u1ec9 gi\u1eef l\u1ea1i \u00abL\u1eb7p l\u1ea1i\u00bb v\u00e0 \u00abT\u1ed1t\u00bb. Ph\u00edm t\u1eaft c\u1ee7a ch\u00fang c\u0169ng "
        "b\u1ecb ch\u1eb7n, \u0111\u1ec3 b\u1ea1n kh\u00f4ng v\u00f4 t\u00ecnh tr\u1ea3 l\u1eddi b\u1eb1ng n\u00fat kh\u00f4ng nh\u00ecn th\u1ea5y.",
        "opt_cursor": "Con tr\u1ecf chu\u1ed9t khi \u0111\u1ee9ng y\u00ean trong:",
        "opt_cursor_tip": "Hi\u1ec7n l\u1ea1i ngay khi b\u1ea1n di chuy\u1ec3n chu\u1ed9t.",
        "opt_cursor_suffix": " gi\u00e2y",
        "opt_auto_start": "T\u1ef1 \u0111\u1ed9ng b\u1eaft \u0111\u1ea7u \u00f4n t\u1eadp khi m\u1edf b\u1ed9 th\u1ebb",
        "opt_auto_start_tip": "Ch\u1ec9 khi c\u00f3 th\u1ebb \u0111\u1ebfn h\u1ea1n. N\u1ebfu ch\u00ednh b\u1ea1n r\u1eddi \u00f4n t\u1eadp, "
        "Hider s\u1ebd kh\u00f4ng \u0111\u01b0a b\u1ea1n quay l\u1ea1i.",
        "btn_save": "Chấp nhận",
        "btn_cancel": "H\u1ee7y",
        "btn_defaults": "Khôi phục giá trị mặc định",
        "saved": "\u0110\u00e3 l\u01b0u c\u1ea5u h\u00ecnh Hider.",
        "save_failed": "Kh\u00f4ng th\u1ec3 l\u01b0u c\u1ea5u h\u00ecnh Hider.",
    },
    "id": {
        "button_hidden": "Tombol itu tersembunyi. Kamu hanya bisa menjawab \u00abLagi\u00bb atau \u00abBagus\u00bb.",
        "hook_error": "Hider mengalami masalah dan menonaktifkan bagian itu demi keamanan. "
        "Periksa konfigurasi add-on.",
        "dialog_title": "Hider",
        "group_review": "Selama meninjau, sembunyikan:",
        "group_behaviour": "Perilaku",
        "opt_menu_bar": "Bilah menu (Berkas, Edit, Alat...)",
        "opt_menu_bar_tip": "Muncul kembali segera setelah kamu keluar dari peninjauan.",
        "opt_toolbar": "Bilah alat atas (Dek, Tambah, Jelajahi, Statistik)",
        "opt_toolbar_tip": "Muncul kembali segera setelah kamu keluar dari peninjauan.",
        "opt_bottom_bar": "Bilah bawah jendela",
        "opt_bottom_bar_tip": "Muncul kembali segera setelah kamu keluar dari peninjauan.",
        "opt_scrollbar": "Bilah gulir kartu",
        "opt_scrollbar_tip": "Hanya visual: kamu masih bisa menggulir dengan roda mouse. "
        "Perubahan terlihat pada kartu berikutnya.",
        "opt_hard_easy": "Tombol \u00abSulit\u00bb dan \u00abMudah\u00bb",
        "opt_hard_easy_tip": "Hanya menyisakan \u00abLagi\u00bb dan \u00abBagus\u00bb. Pintasan keyboardnya juga "
        "diblokir, agar kamu tidak salah menjawab dengan tombol yang tidak terlihat.",
        "opt_cursor": "Kursor mouse ketika diam selama:",
        "opt_cursor_tip": "Muncul kembali segera setelah kamu menggerakkan mouse.",
        "opt_cursor_suffix": " dtk",
        "opt_auto_start": "Mulai peninjauan otomatis saat membuka dek",
        "opt_auto_start_tip": "Hanya jika ada kartu yang jatuh tempo. Jika kamu sendiri keluar dari "
        "peninjauan, Hider tidak akan memasukkanmu kembali.",
        "btn_save": "Terima",
        "btn_cancel": "Batal",
        "btn_defaults": "Pulihkan nilai bawaan",
        "saved": "Konfigurasi Hider disimpan.",
        "save_failed": "Konfigurasi Hider tidak dapat disimpan.",
    },
    "ms": {
        "button_hidden": "Butang itu tersembunyi. Anda hanya boleh menjawab \u00abSekali lagi\u00bb atau \u00abBaik\u00bb.",
        "hook_error": "Hider menghadapi masalah dan melumpuhkan bahagian itu demi keselamatan. "
        "Semak konfigurasi tambahan.",
        "dialog_title": "Hider",
        "group_review": "Semasa ulang kaji, sembunyikan:",
        "group_behaviour": "Kelakuan",
        "opt_menu_bar": "Bar menu (Fail, Edit, Alatan...)",
        "opt_menu_bar_tip": "Muncul semula sebaik sahaja anda keluar dari ulang kaji.",
        "opt_toolbar": "Bar alat atas (Dek, Tambah, Semak Imbas, Statistik)",
        "opt_toolbar_tip": "Muncul semula sebaik sahaja anda keluar dari ulang kaji.",
        "opt_bottom_bar": "Bar bawah tetingkap",
        "opt_bottom_bar_tip": "Muncul semula sebaik sahaja anda keluar dari ulang kaji.",
        "opt_scrollbar": "Bar tatal kad",
        "opt_scrollbar_tip": "Hanya visual: anda masih boleh tatal dengan roda tetikus. "
        "Perubahan kelihatan pada kad seterusnya.",
        "opt_hard_easy": "Butang \u00abSukar\u00bb dan \u00abMudah\u00bb",
        "opt_hard_easy_tip": "Hanya menyisakan \u00abSekali lagi\u00bb dan \u00abBaik\u00bb. Pintasan papan kekunci mereka juga "
        "disekat, supaya anda tidak menjawab secara tidak sengaja dengan butang yang tidak kelihatan.",
        "opt_cursor": "Kursor tetikus apabila diam selama:",
        "opt_cursor_tip": "Muncul semula sebaik sahaja anda menggerakkan tetikus.",
        "opt_cursor_suffix": " s",
        "opt_auto_start": "Mulakan ulang kaji secara automatik apabila membuka dek",
        "opt_auto_start_tip": "Hanya jika terdapat kad yang perlu diulang kaji. Jika anda sendiri keluar "
        "dari ulang kaji, Hider tidak akan memasukkan anda semula.",
        "btn_save": "Terima",
        "btn_cancel": "Batal",
        "btn_defaults": "Pulihkan nilai lalai",
        "saved": "Konfigurasi Hider disimpan.",
        "save_failed": "Konfigurasi Hider tidak dapat disimpan.",
    },
    "fil": {
        "button_hidden": "Nakatago ang button na iyon. Puwede ka lang sumagot ng \u00abUlitin\u00bb o \u00abMabuti\u00bb.",
        "hook_error": "May naranasan si Hider na problema at in-disable ang bahaging iyon para sa kaligtasan. "
        "Suriin ang configuration ng add-on.",
        "dialog_title": "Hider",
        "group_review": "Habang nagre-review, itago:",
        "group_behaviour": "Asal",
        "opt_menu_bar": "Ang menu bar (File, Edit, Tools...)",
        "opt_menu_bar_tip": "Lalabas ulit ito sa sandaling umalis ka sa review.",
        "opt_toolbar": "Ang itaas na toolbar (Decks, Add, Browse, Stats)",
        "opt_toolbar_tip": "Lalabas ulit ito sa sandaling umalis ka sa review.",
        "opt_bottom_bar": "Ang ibabang bar ng window",
        "opt_bottom_bar_tip": "Lalabas ulit ito sa sandaling umalis ka sa review.",
        "opt_scrollbar": "Ang scrollbar ng card",
        "opt_scrollbar_tip": "Visual lang ito: puwede ka pa ring mag-scroll gamit ang mouse wheel. "
        "Makikita ang pagbabago sa susunod na card.",
        "opt_hard_easy": "Ang mga button na \u00abMahirap\u00bb at \u00abMadali\u00bb",
        "opt_hard_easy_tip": "Iiwan lang ang \u00abUlitin\u00bb at \u00abMabuti\u00bb. Naka-block din ang kanilang "
        "keyboard shortcuts, para hindi ka aksidenteng makasagot gamit ang button na hindi mo nakikita.",
        "opt_cursor": "Ang mouse pointer kapag hindi gumagalaw sa loob ng:",
        "opt_cursor_tip": "Lalabas ulit sa sandaling gumalaw ang mouse.",
        "opt_cursor_suffix": " s",
        "opt_auto_start": "Awtomatikong simulan ang review pagbukas ng deck",
        "opt_auto_start_tip": "Kung may mga due card lamang. Kung ikaw mismo ang aalis sa review, "
        "hindi ka na ibabalik ni Hider.",
        "btn_save": "Tanggapin",
        "btn_cancel": "Kanselahin",
        "btn_defaults": "Ibalik ang mga default na halaga",
        "saved": "Na-save na ang configuration ng Hider.",
        "save_failed": "Hindi na-save ang configuration ng Hider.",
    },
}


def _resolve(code: str) -> str:
    code = code.replace("-", "_")
    parts = code.split("_")
    primary = parts[0].lower()
    region = parts[1].upper() if len(parts) > 1 else ""
    if primary == "zh":
        return "zh_TW" if region in ("TW", "HK", "MO") or "HANT" in code.upper() else "zh_CN"
    if primary == "pt":
        return "pt_PT" if region == "PT" else "pt_BR"
    if primary in ("fil", "tl"):
        return "fil"
    return primary if primary in TRANSLATIONS else FALLBACK


@lru_cache(maxsize=1)
def current_lang() -> str:
    try:
        import anki.lang

        raw = (
            getattr(anki.lang, "current_lang", None)
            or getattr(anki.lang, "currentLang", None)
            or ""
        )
        code = raw if isinstance(raw, str) else ""
        return _resolve(code)
    except Exception as exc:
        print(f"[hider] {exc!r}")
        return FALLBACK


def t(key: str, **values: str) -> str:
    table = TRANSLATIONS.get(current_lang(), TRANSLATIONS[FALLBACK])
    text = table.get(key)
    if text is None:
        text = TRANSLATIONS[FALLBACK].get(key, key)
    if not values:
        return text
    try:
        return text.format(**values)
    except (KeyError, IndexError):
        return text