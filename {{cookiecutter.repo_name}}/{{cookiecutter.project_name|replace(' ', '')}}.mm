<map version="freeplane 1.7.0">
<!--To view this file, download free mind mapping software Freeplane from http://freeplane.sourceforge.net -->
<node FOLDED="false" ID="ID_822712631" CREATED="1564511595253" MODIFIED="1618554709585"><richcontent TYPE="NODE">

<html>
  <head>

  </head>
  <body>
    <h1>
      {{cookiecutter.project_name }}
    </h1>
  </body>
</html>
</richcontent>
<attribute_layout NAME_WIDTH="55.49999834597116 pt" VALUE_WIDTH="110.99999669194231 pt"/>
<attribute NAME="cc_template" VALUE="cc-py-setup"/>
<attribute NAME="version" VALUE="{{cookiecutter.version}}"/>
<attribute NAME="$id" VALUE="{{cookiecutter.domain}}#"/>
<attribute NAME="ns_name" VALUE="{{cookiecutter.ns_name}}"/>
<attribute NAME="domain" VALUE="{{cookiecutter.domain}}"/>
<attribute NAME="repo_name" VALUE="{{cookiecutter.repo_name}}"/>
<attribute NAME="languages" VALUE="{{cookiecutter.languages}}"/>
<attribute NAME="timezone" VALUE="{{cookiecutter.timezone}}"/>
<attribute NAME="keywords" VALUE="{{cookiecutter.keywords}}"/>
<attribute NAME="license" VALUE="NUMENGO"/>
<hook NAME="MapStyle">
    <properties show_icon_for_attributes="true" fit_to_viewport="false" show_note_icons="true"/>

<map_styles>
<stylenode LOCALIZED_TEXT="styles.root_node" STYLE="oval" UNIFORM_SHAPE="true" VGAP_QUANTITY="24.0 pt">
<font SIZE="24"/>
<stylenode LOCALIZED_TEXT="styles.predefined" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="default" COLOR="#000000" STYLE="fork" MAX_WIDTH="600.0 px">
<font NAME="SansSerif" SIZE="12" BOLD="false" ITALIC="false"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.details"/>
<stylenode LOCALIZED_TEXT="defaultstyle.attributes">
<font SIZE="9"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.note"/>
<stylenode LOCALIZED_TEXT="defaultstyle.floating">
<edge STYLE="hide_edge"/>
<cloud COLOR="#f0f0f0" SHAPE="ROUND_RECT"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.ok">
<icon BUILTIN="button_ok"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.needs_action">
<icon BUILTIN="messagebox_warning"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.floating_node">
<cloud COLOR="#ffffff" SHAPE="ARC"/>
<edge STYLE="hide_edge"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.topic" COLOR="#18898b" STYLE="fork">
<font NAME="Liberation Sans" SIZE="12" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subtopic" COLOR="#cc3300" STYLE="fork">
<font NAME="Liberation Sans" SIZE="12" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subsubtopic" COLOR="#669900">
<font NAME="Liberation Sans" SIZE="12" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.connection" COLOR="#606060" STYLE="fork">
<font NAME="Arial" SIZE="10" BOLD="false"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.important" COLOR="#ff0000">
<font NAME="Liberation Sans" SIZE="12"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.question">
<icon BUILTIN="help"/>
<font NAME="Aharoni" SIZE="12"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.key" COLOR="#996600">
<icon BUILTIN="password"/>
<font NAME="Liberation Sans" SIZE="12" BOLD="false"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.idea">
<icon BUILTIN="idea"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.note" COLOR="#990000">
<font NAME="Liberation Sans" SIZE="12"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.date" COLOR="#0033ff">
<icon BUILTIN="calendar"/>
<font NAME="Liberation Sans" SIZE="12"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.website" COLOR="#006633">
<font NAME="Liberation Sans" SIZE="12"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.list" COLOR="#cc6600">
<icon BUILTIN="list"/>
<font NAME="Liberation Sans" SIZE="12" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.quotation" COLOR="#338800" STYLE="fork">
<font NAME="Liberation Sans" SIZE="12" BOLD="false" ITALIC="false"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.definition" COLOR="#666600">
<font NAME="Liberation Sans" SIZE="12" BOLD="false"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.description" COLOR="#996600">
<font NAME="Liberation Sans" SIZE="12" BOLD="false"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.pending" COLOR="#b3b95c">
<font NAME="Liberation Sans" SIZE="12"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.AutomaticLayout" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="AutomaticLayout.level.root" COLOR="#000000">
<font SIZE="20"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,1" COLOR="#0033ff">
<font SIZE="18"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,2" COLOR="#00b439">
<font SIZE="16"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,3" COLOR="#990000">
<font SIZE="14"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,4" COLOR="#111111">
<font SIZE="12"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.user-defined" POSITION="right" STYLE="bubble">
<stylenode TEXT="red" COLOR="#ff0300"/>
<stylenode TEXT="green" COLOR="#00cd00"/>
</stylenode>
</stylenode>
</map_styles>
</hook>
<node TEXT="{{ cookiecutter.short_description }}" POSITION="right" ID="ID_439081159" CREATED="1564513063544" MODIFIED="1574097100051">
<icon BUILTIN="idea"/>
<edge COLOR="#7c007c"/>
</node>
<node TEXT="authors" POSITION="right" ID="ID_1099217662" CREATED="1564512586456" MODIFIED="1564562190310" LINK="%7B%7Bcookiecutter.repo_name%7D%7D/AUTHORS.rst">
<icon BUILTIN="group"/>
<edge COLOR="#0000ff"/>
<node TEXT="{{cookiecutter.full_name}}" ID="ID_1625049955" CREATED="1564512868837" MODIFIED="1564513399553" LINK="mailto:%7B%7Bcookiecutter.email%7D%7D"/>
</node>
<node TEXT="documentation" POSITION="right" ID="ID_10359407" CREATED="1564512049272" MODIFIED="1564562378591" LINK="%7B%7Bcookiecutter.repo_name%7D%7D/README.rst">
<icon BUILTIN="help"/>
<edge COLOR="#7c7c00"/>
</node>
<node TEXT="definitions" POSITION="right" ID="ID_1877134666" CREATED="1574097045957" MODIFIED="1574097066413">
<icon BUILTIN="executable"/>
</node>
<node TEXT="config" POSITION="left" ID="ID_1792180576" CREATED="1564560707351" MODIFIED="1648798438178">
<icon BUILTIN="folder"/>
<edge COLOR="#0000ff"/>
<node TEXT="environment" ID="ID_611638581" CREATED="1564525004691" MODIFIED="1574097675444">
<icon BUILTIN="gohome"/>
<node TEXT="requirements" ID="ID_805509740" CREATED="1564511844874" MODIFIED="1564525025465">
<node TEXT="base" ID="ID_1193327370" CREATED="1564514737493" MODIFIED="1564514739592"/>
<node TEXT="dev" ID="ID_1881762815" CREATED="1564511877888" MODIFIED="1564511881057"/>
<node TEXT="prod" ID="ID_1918746364" CREATED="1564511881910" MODIFIED="1564511883569"/>
</node>
</node>
<node TEXT="settings" ID="ID_1022287218" CREATED="1564511772728" MODIFIED="1564562270224">
<icon BUILTIN="executable"/>
<node TEXT="#" ID="ID_768606279" CREATED="1648797936355" MODIFIED="1648797941930">
<node TEXT="config settings" ID="ID_136580391" CREATED="1648797942443" MODIFIED="1648798478191"/>
</node>
</node>
<node TEXT="deployment" ID="ID_303797780" CREATED="1564511853175" MODIFIED="1564562290063">
<icon BUILTIN="internet"/>
<node TEXT="settings" ID="ID_1478975464" CREATED="1564511908841" MODIFIED="1564511911548">
<node TEXT="dev" ID="ID_1077769042" CREATED="1564511911792" MODIFIED="1564511912876"/>
<node TEXT="prod" ID="ID_1838239997" CREATED="1564511913187" MODIFIED="1564511915332"/>
</node>
</node>
<node TEXT="urls" ID="ID_46120739" CREATED="1564524510165" MODIFIED="1564562297599">
<icon BUILTIN="mindmap"/>
</node>
<node TEXT="entry points" ID="ID_740169143" CREATED="1564524510165" MODIFIED="1586855445185">
<icon BUILTIN="mindmap"/>
</node>
<node TEXT="static" ID="ID_1821767778" CREATED="1574847273070" MODIFIED="1574847274807"/>
</node>
<node TEXT="changes" POSITION="left" ID="ID_8536831" CREATED="1564561854135" MODIFIED="1564562336122">
<icon BUILTIN="clock2"/>
</node>
</node>
</map>
