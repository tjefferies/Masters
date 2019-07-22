
# Bayesian Reliability Chapter 2

Last updated: 07/21/2019<br>
Author: Travis Jefferies

This notebook walks through the beta-binomial Bayesian modeling paradigm presented in Bayesian Reliability Chapter 2.

Source:
“Bayesian Inference.” Bayesian Reliability, by Michael Hamada, Springer, 2008, pp. 21–39.

Table 2.1 shows first time spacecraft vehicle launches post 1980.


```sas
/*Source: https://www4.stat.ncsu.edu/~wilson/BR/table21.txt*/
Title "Chapter 2 Table 2.1";
data table2_1;
    input Vehicle $ Outcome;
    cards;
Pegasus 1
Percheron 0
AMROC 0
Conestoga 0
Ariane 1
IndiaSLV3 0
IndiaASLV 0
IndiaPSLV 0
Shavit 1
Taepodong 0
BrazilVLS 0
proc print; run;
```

    SAS Connection established. Subprocess id is 20340
    





<!DOCTYPE html>
<html lang="en" xml:lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta charset="utf-8"/>
<meta content="SAS 9.4" name="generator"/>
<title>SAS Output</title>
<style>
/*<![CDATA[*/
.body.c > table, .body.c > pre, .body.c div > table,
.body.c div > pre, .body.c > table, .body.c > pre,
.body.j > table, .body.j > pre, .body.j div > table,
.body.j div > pre, .body.j > table, .body.j > pre,
.body.c p.note, .body.c p.warning, .body.c p.error, .body.c p.fatal,
.body.j p.note, .body.j p.warning, .body.j p.error, .body.j p.fatal,
.body.c > table.layoutcontainer, .body.j > table.layoutcontainer { margin-left: auto; margin-right: auto }
.layoutregion.l table, .layoutregion.l pre, .layoutregion.l p.note,
.layoutregion.l p.warning, .layoutregion.l p.error, .layoutregion.l p.fatal { margin-left: 0 }
.layoutregion.c table, .layoutregion.c pre, .layoutregion.c p.note,
.layoutregion.c p.warning, .layoutregion.c p.error, .layoutregion.c p.fatal { margin-left: auto; margin-right: auto }
.layoutregion.r table, .layoutregion.r pre, .layoutregion.r p.note,
.layoutregion.r table, .layoutregion.r pre, .layoutregion.r p.note,
.layoutregion.r p.warning, .layoutregion.r p.error, .layoutregion.r p.fatal { margin-right: 0 }
article, aside, details, figcaption, figure, footer, header, hgroup, nav, section { display: block }
html{ font-size: 100% }
.body { margin: 1em; font-size: 13px; line-height: 1.231 }
sup { position: relative; vertical-align: baseline; bottom: 0.25em; font-size: 0.8em }
sub { position: relative; vertical-align: baseline; top: 0.25em; font-size: 0.8em }
ul, ol { margin: 1em 0; padding: 0 0 0 40px }
dd { margin: 0 0 0 40px }
nav ul, nav ol { list-style: none; list-style-image: none; margin: 0; padding: 0 }
img { border: 0; vertical-align: middle }
svg:not(:root) { overflow: hidden }
figure { margin: 0 }
table { border-collapse: collapse; border-spacing: 0 }
.layoutcontainer { border-collapse: separate; border-spacing: 0 }
p { margin-top: 0; text-align: left }
h1.heading1 { text-align: left }
h2.heading2 { text-align: left }
h3.heading3 { text-align: left }
h4.heading4 { text-align: left }
h5.heading5 { text-align: left }
h6.heading6 { text-align: left }
span { text-align: left }
table { margin-bottom: 1em }
td, th { text-align: left; padding: 3px 6px; vertical-align: top }
td[class$="fixed"], th[class$="fixed"] { white-space: pre }
section, article { padding-top: 1px; padding-bottom: 8px }
hr.pagebreak { height: 0px; border: 0; border-bottom: 1px solid #c0c0c0; margin: 1em 0 }
.stacked-value { text-align: left; display: block }
.stacked-cell > .stacked-value, td.data > td.data, th.data > td.data, th.data > th.data, td.data > th.data, th.header > th.header { border: 0 }
.stacked-cell > div.data { border-width: 0 }
.systitleandfootercontainer { white-space: nowrap; margin-bottom: 1em }
.systitleandfootercontainer > p { margin: 0 }
.systitleandfootercontainer > p > span { display: inline-block; width: 100%; white-space: normal }
.batch { display: table }
.toc { display: none }
.proc_note_group, .proc_title_group { margin-bottom: 1em }
p.proctitle { margin: 0 }
p.note, p.warning, p.error, p.fatal { display: table }
.notebanner, .warnbanner, .errorbanner, .fatalbanner,
.notecontent, .warncontent, .errorcontent, .fatalcontent { display: table-cell; padding: 0.5em }
.notebanner, .warnbanner, .errorbanner, .fatalbanner { padding-right: 0 }
.body > div > ol li { text-align: left }
.beforecaption > h4 { margin-top: 0; margin-bottom: 0 }
.c { text-align: center }
.r { text-align: right }
.l { text-align: left }
.j { text-align: justify }
.d { text-align: right }
.b { vertical-align: bottom }
.m { vertical-align: middle }
.t { vertical-align: top }
.accessiblecaption {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
a:active { color: #800080 }
.aftercaption {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
    padding-top: 4pt;
}
.batch > colgroup {
    border-left: 1px solid #c1c1c1;
    border-right: 1px solid #c1c1c1;
}
.batch > tbody, .batch > thead, .batch > tfoot {
    border-top: 1px solid #c1c1c1;
    border-bottom: 1px solid #c1c1c1;
}
.batch { border: hidden; }
.batch {
    background-color: #fafbfe;
    border: 1px solid #c1c1c1;
    border-collapse: separate;
    border-spacing: 1px;
    color: #000000;
    font-family: 'SAS Monospace', 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    padding: 7px;
    }
.beforecaption {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.body {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    margin-left: 8px;
    margin-right: 8px;
}
.bodydate {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    text-align: right;
    vertical-align: top;
    width: 100%;
}
.bycontentfolder {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.byline {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.bylinecontainer > col, .bylinecontainer > colgroup > col, .bylinecontainer > colgroup, .bylinecontainer > tr, .bylinecontainer > * > tr, .bylinecontainer > thead, .bylinecontainer > tbody, .bylinecontainer > tfoot { border: none; }
.bylinecontainer {
    background-color: #fafbfe;
    border: none;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.caption {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.cell, .container {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.contentfolder, .contentitem {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.contentproclabel, .contentprocname {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.contents {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: decimal;
    margin-left: 8px;
    margin-right: 8px;
}
.contentsdate {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.contenttitle {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: bold;
}
.continued {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
    width: 100%;
}
.data, .dataemphasis {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.dataemphasisfixed {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.dataempty {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.datafixed {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.datastrong {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.datastrongfixed {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.date {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.document {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.errorbanner {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.errorcontent {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.errorcontentfixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.extendedpage {
    background-color: #fafbfe;
    border-style: solid;
    border-width: 1pt;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
    text-align: center;
}
.fatalbanner {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.fatalcontent {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.fatalcontentfixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.folderaction {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.footer {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.footeremphasis {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.footeremphasisfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.footerempty {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.footerfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.footerstrong {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.footerstrongfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.frame {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.graph > colgroup {
    border-left: 1px solid #c1c1c1;
    border-right: 1px solid #c1c1c1;
}
.graph > tbody, .graph > thead, .graph > tfoot {
    border-top: 1px solid #c1c1c1;
    border-bottom: 1px solid #c1c1c1;
}
.graph { border: hidden; }
.graph {
    background-color: #fafbfe;
    border: 1px solid #c1c1c1;
    border-collapse: separate;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    }
.header {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.headeremphasis {
    background-color: #d8dbd3;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.headeremphasisfixed {
    background-color: #d8dbd3;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.headerempty {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.headerfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.headersandfooters {
    background-color: #edf2f9;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.headerstrong {
    background-color: #d8dbd3;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.headerstrongfixed {
    background-color: #d8dbd3;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.heading1, .heading2, .heading3, .heading4, .heading5, .heading6 { font-family: Arial, Helvetica, sans-serif }
.index {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.indexaction, .indexitem {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.indexprocname {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.indextitle {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: bold;
}
.layoutcontainer, .layoutregion {
    border-width: 0;
    border-spacing: 30px;
}
.linecontent {
    background-color: #fafbfe;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
a:link { color: #0000ff }
.list {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: disc;
}
.list10 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: square;
}
.list2 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: circle;
}
.list3, .list4, .list5, .list6, .list7, .list8, .list9 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: square;
}
.listitem {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: disc;
}
.listitem10 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: square;
}
.listitem2 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: circle;
}
.listitem3, .listitem4, .listitem5, .listitem6, .listitem7, .listitem8, .listitem9 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: square;
}
.note {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.notebanner {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.notecontent {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.notecontentfixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.output > colgroup {
    border-left: 1px solid #c1c1c1;
    border-right: 1px solid #c1c1c1;
}
.output > tbody, .output > thead, .output > tfoot {
    border-top: 1px solid #c1c1c1;
    border-bottom: 1px solid #c1c1c1;
}
.output { border: hidden; }
.output {
    background-color: #fafbfe;
    border: 1px solid #c1c1c1;
    border-collapse: separate;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    }
.pageno {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
    text-align: right;
    vertical-align: top;
}
.pages {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: decimal;
    margin-left: 8px;
    margin-right: 8px;
}
.pagesdate {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.pagesitem {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.pagesproclabel, .pagesprocname {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.pagestitle {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: bold;
}
.paragraph {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.parskip > col, .parskip > colgroup > col, .parskip > colgroup, .parskip > tr, .parskip > * > tr, .parskip > thead, .parskip > tbody, .parskip > tfoot { border: none; }
.parskip {
    border: none;
    border-spacing: 0;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
    }
.prepage {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    text-align: left;
}
.proctitle {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.proctitlefixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowfooter {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowfooteremphasis {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.rowfooteremphasisfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.rowfooterempty {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowfooterfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.rowfooterstrong {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowfooterstrongfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowheader {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowheaderemphasis {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.rowheaderemphasisfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.rowheaderempty {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowheaderfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.rowheaderstrong {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowheaderstrongfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.systemfooter, .systemfooter10, .systemfooter2, .systemfooter3, .systemfooter4, .systemfooter5, .systemfooter6, .systemfooter7, .systemfooter8, .systemfooter9 {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.systemtitle, .systemtitle10, .systemtitle2, .systemtitle3, .systemtitle4, .systemtitle5, .systemtitle6, .systemtitle7, .systemtitle8, .systemtitle9 {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size: small;
    font-style: normal;
    font-weight: bold;
}
.systitleandfootercontainer > col, .systitleandfootercontainer > colgroup > col, .systitleandfootercontainer > colgroup, .systitleandfootercontainer > tr, .systitleandfootercontainer > * > tr, .systitleandfootercontainer > thead, .systitleandfootercontainer > tbody, .systitleandfootercontainer > tfoot { border: none; }
.systitleandfootercontainer {
    background-color: #fafbfe;
    border: none;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.table > col, .table > colgroup > col {
    border-left: 1px solid #c1c1c1;
    border-right: 0 solid #c1c1c1;
}
.table > tr, .table > * > tr {
    border-top: 1px solid #c1c1c1;
    border-bottom: 0 solid #c1c1c1;
}
.table { border: hidden; }
.table {
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 1px 0 0 1px;
    border-collapse: collapse;
    border-spacing: 0;
    }
.titleandnotecontainer > col, .titleandnotecontainer > colgroup > col, .titleandnotecontainer > colgroup, .titleandnotecontainer > tr, .titleandnotecontainer > * > tr, .titleandnotecontainer > thead, .titleandnotecontainer > tbody, .titleandnotecontainer > tfoot { border: none; }
.titleandnotecontainer {
    background-color: #fafbfe;
    border: none;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.titlesandfooters {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.usertext {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
a:visited { color: #800080 }
.warnbanner {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.warncontent {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.warncontentfixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
/*]]>*/
</style>
</head>
<body class="l body">
<div style="padding-bottom: 8px; padding-top: 1px">
<div id="IDX" class="systitleandfootercontainer" style="border-spacing: 1px">
<p><span class="c systemtitle">Chapter 2 Table 2.1</span> </p>
</div>
<div style="padding-bottom: 8px; padding-top: 1px">
<table class="table" style="border-spacing: 0" aria-label="Data Set WORK.TABLE2_1">
<caption aria-label="Data Set WORK.TABLE2_1"></caption>
<colgroup><col/></colgroup><colgroup><col/><col/></colgroup>
<thead>
<tr>
<th class="r header" scope="col">Obs</th>
<th class="header" scope="col">Vehicle</th>
<th class="r header" scope="col">Outcome</th>
</tr>
</thead>
<tbody>
<tr>
<th class="r rowheader" scope="row">1</th>
<td class="data">Pegasus</td>
<td class="r data">1</td>
</tr>
<tr>
<th class="r rowheader" scope="row">2</th>
<td class="data">Perchero</td>
<td class="r data">0</td>
</tr>
<tr>
<th class="r rowheader" scope="row">3</th>
<td class="data">AMROC</td>
<td class="r data">0</td>
</tr>
<tr>
<th class="r rowheader" scope="row">4</th>
<td class="data">Conestog</td>
<td class="r data">0</td>
</tr>
<tr>
<th class="r rowheader" scope="row">5</th>
<td class="data">Ariane</td>
<td class="r data">1</td>
</tr>
<tr>
<th class="r rowheader" scope="row">6</th>
<td class="data">IndiaSLV</td>
<td class="r data">0</td>
</tr>
<tr>
<th class="r rowheader" scope="row">7</th>
<td class="data">IndiaASL</td>
<td class="r data">0</td>
</tr>
<tr>
<th class="r rowheader" scope="row">8</th>
<td class="data">IndiaPSL</td>
<td class="r data">0</td>
</tr>
<tr>
<th class="r rowheader" scope="row">9</th>
<td class="data">Shavit</td>
<td class="r data">1</td>
</tr>
<tr>
<th class="r rowheader" scope="row">10</th>
<td class="data">Taepodon</td>
<td class="r data">0</td>
</tr>
<tr>
<th class="r rowheader" scope="row">11</th>
<td class="data">BrazilVL</td>
<td class="r data">0</td>
</tr>
</tbody>
</table>
</div>
</div>
</body>
</html>




To model using a Bernoulli distribution, we must assume each event is independent from one another.

For two events *A and B*, this is formulated as:

$$
\textbf{P}\left(A\cap B \right) = \textbf{P}\left(A \right)\textbf{P}\left(B \right)
$$

Two events *A and B* are ***conditionally independent*** given an event *C* if:

$$
\textbf{P}\left(A\cap B \, | \, C\right) = \textbf{P}\left(A \, | \, C\right)\textbf{P}\left(B \, | \, C\right)
$$

Once we determine that the binary outcome of two events are conditionally independent from one another, we can multiply their individual probabilities together to obtain the probability of observing a given sequence of successes and failures.

Let $\pi$ denote the probability that a new launch vehicle selected at random from the population succeeds, then we can express the probability of obtaining the sequence of successes and failures in Table 2.1 as:

$$
\pi \left(1 - \pi \right)\left(1 - \pi \right)\left(1 - \pi \right)\pi \left(1 - \pi \right)\left(1 - \pi \right)\left(1 - \pi \right)\pi \left(1 - \pi \right)\left(1 - \pi \right) = \pi^{3}\left(1 - \pi \right)^{8}
$$

We can generalize this result to the situation where we observe $\textit{y}$ successes in $\textit{n}$ trials and arrive at the Binomial probability density function:

$$
f\left(y \, | \, n, \pi \right) = \binom{n}{y} \pi^{y}\left(1-\pi\right)^{n-y}
$$

In Table 2.1 above $\textit{y}=$ 3 and $\textit{n}=$ 11.<br>

Once an experiment has been conducted or data has been collected, the value of the random variable $\textit{y}$ is known. It then makes more sense to regard the sampling distribution as a function of the unknown model parameter, $\pi$.

When we model this unknown model parameter, the sampling distribution (or any function proportional to it) is called the ***likelihood function***.

The simplest way to use a likelihood function is to find the value of the unknown parameters that maximizes the value of the likelihood function. These estimates are referred to as ***maximum likelihood estimates*** (MLEs). An MLE makes the observed data as "likely" as possible.

For computational purposes, it is much easier to model the logarithm of the likelihood function or the *log-likelihood* function.
* When observations are conditionally independent of one another, we can sum the individual probabilities of successes instead of multiplying in the log-likelihood function

The log-likelihood function for the Binomial distribution is proportional to:

$$
\log\left[ f\left( y \, | \, n, \pi \right)\right] \propto y \, \log(\pi) + \left(n-y\right)\log\left( 1-\pi\right)
$$

If we take the first derivative with respect to $\pi$ and set the result equal to zero, we find that the MLE must satisfy:

$$
0 = \frac{d\log f\left( y \, | \, n, \pi \right)}{d\pi} = \frac{y}{\pi} - \frac{n-y}{1-\pi}
$$

We can now solve for $\pi$:

$$
\begin{align*}
0 &= \frac{y}{\pi} - \frac{n-y}{1-\pi}\\ 
\frac{n-y}{1-\pi} &= \frac{y}{\pi}\\ 
\frac{1-\pi}{n-y} &= \frac{\pi}{y} \\
\frac{y\left(1-\pi\right)}{n-y} &= \pi \\
\frac{y}{n} &= \pi
\end{align*}
$$

With $\textit{y}=$ 3 and $\textit{n}=$ 11...

$$
\frac{3}{11} = \pi
$$

The corresponding Binomial distribution looks like:


```sas
%let y = 3;
%let n = 11;
%let pi = &y./&n.;

ods graphics on;
proc mcmc seed=23 nmc=2000 maxtune=0 statistics=none diagnostics=none PLOTS=DENSITY;
   ods exclude nobs parameters;
   parm pi 0;
   prior pi ~ binomial(n=&n., &pi.);
   model general(0);
run;
```




<!DOCTYPE html>
<html lang="en" xml:lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta charset="utf-8"/>
<meta content="SAS 9.4" name="generator"/>
<title>SAS Output</title>
<style>
/*<![CDATA[*/
.body.c > table, .body.c > pre, .body.c div > table,
.body.c div > pre, .body.c > table, .body.c > pre,
.body.j > table, .body.j > pre, .body.j div > table,
.body.j div > pre, .body.j > table, .body.j > pre,
.body.c p.note, .body.c p.warning, .body.c p.error, .body.c p.fatal,
.body.j p.note, .body.j p.warning, .body.j p.error, .body.j p.fatal,
.body.c > table.layoutcontainer, .body.j > table.layoutcontainer { margin-left: auto; margin-right: auto }
.layoutregion.l table, .layoutregion.l pre, .layoutregion.l p.note,
.layoutregion.l p.warning, .layoutregion.l p.error, .layoutregion.l p.fatal { margin-left: 0 }
.layoutregion.c table, .layoutregion.c pre, .layoutregion.c p.note,
.layoutregion.c p.warning, .layoutregion.c p.error, .layoutregion.c p.fatal { margin-left: auto; margin-right: auto }
.layoutregion.r table, .layoutregion.r pre, .layoutregion.r p.note,
.layoutregion.r table, .layoutregion.r pre, .layoutregion.r p.note,
.layoutregion.r p.warning, .layoutregion.r p.error, .layoutregion.r p.fatal { margin-right: 0 }
article, aside, details, figcaption, figure, footer, header, hgroup, nav, section { display: block }
html{ font-size: 100% }
.body { margin: 1em; font-size: 13px; line-height: 1.231 }
sup { position: relative; vertical-align: baseline; bottom: 0.25em; font-size: 0.8em }
sub { position: relative; vertical-align: baseline; top: 0.25em; font-size: 0.8em }
ul, ol { margin: 1em 0; padding: 0 0 0 40px }
dd { margin: 0 0 0 40px }
nav ul, nav ol { list-style: none; list-style-image: none; margin: 0; padding: 0 }
img { border: 0; vertical-align: middle }
svg:not(:root) { overflow: hidden }
figure { margin: 0 }
table { border-collapse: collapse; border-spacing: 0 }
.layoutcontainer { border-collapse: separate; border-spacing: 0 }
p { margin-top: 0; text-align: left }
h1.heading1 { text-align: left }
h2.heading2 { text-align: left }
h3.heading3 { text-align: left }
h4.heading4 { text-align: left }
h5.heading5 { text-align: left }
h6.heading6 { text-align: left }
span { text-align: left }
table { margin-bottom: 1em }
td, th { text-align: left; padding: 3px 6px; vertical-align: top }
td[class$="fixed"], th[class$="fixed"] { white-space: pre }
section, article { padding-top: 1px; padding-bottom: 8px }
hr.pagebreak { height: 0px; border: 0; border-bottom: 1px solid #c0c0c0; margin: 1em 0 }
.stacked-value { text-align: left; display: block }
.stacked-cell > .stacked-value, td.data > td.data, th.data > td.data, th.data > th.data, td.data > th.data, th.header > th.header { border: 0 }
.stacked-cell > div.data { border-width: 0 }
.systitleandfootercontainer { white-space: nowrap; margin-bottom: 1em }
.systitleandfootercontainer > p { margin: 0 }
.systitleandfootercontainer > p > span { display: inline-block; width: 100%; white-space: normal }
.batch { display: table }
.toc { display: none }
.proc_note_group, .proc_title_group { margin-bottom: 1em }
p.proctitle { margin: 0 }
p.note, p.warning, p.error, p.fatal { display: table }
.notebanner, .warnbanner, .errorbanner, .fatalbanner,
.notecontent, .warncontent, .errorcontent, .fatalcontent { display: table-cell; padding: 0.5em }
.notebanner, .warnbanner, .errorbanner, .fatalbanner { padding-right: 0 }
.body > div > ol li { text-align: left }
.beforecaption > h4 { margin-top: 0; margin-bottom: 0 }
.c { text-align: center }
.r { text-align: right }
.l { text-align: left }
.j { text-align: justify }
.d { text-align: right }
.b { vertical-align: bottom }
.m { vertical-align: middle }
.t { vertical-align: top }
.accessiblecaption {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
a:active { color: #800080 }
.aftercaption {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
    padding-top: 4pt;
}
.batch > colgroup {
    border-left: 1px solid #c1c1c1;
    border-right: 1px solid #c1c1c1;
}
.batch > tbody, .batch > thead, .batch > tfoot {
    border-top: 1px solid #c1c1c1;
    border-bottom: 1px solid #c1c1c1;
}
.batch { border: hidden; }
.batch {
    background-color: #fafbfe;
    border: 1px solid #c1c1c1;
    border-collapse: separate;
    border-spacing: 1px;
    color: #000000;
    font-family: 'SAS Monospace', 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    padding: 7px;
    }
.beforecaption {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.body {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    margin-left: 8px;
    margin-right: 8px;
}
.bodydate {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    text-align: right;
    vertical-align: top;
    width: 100%;
}
.bycontentfolder {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.byline {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.bylinecontainer > col, .bylinecontainer > colgroup > col, .bylinecontainer > colgroup, .bylinecontainer > tr, .bylinecontainer > * > tr, .bylinecontainer > thead, .bylinecontainer > tbody, .bylinecontainer > tfoot { border: none; }
.bylinecontainer {
    background-color: #fafbfe;
    border: none;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.caption {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.cell, .container {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.contentfolder, .contentitem {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.contentproclabel, .contentprocname {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.contents {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: decimal;
    margin-left: 8px;
    margin-right: 8px;
}
.contentsdate {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.contenttitle {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: bold;
}
.continued {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
    width: 100%;
}
.data, .dataemphasis {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.dataemphasisfixed {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.dataempty {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.datafixed {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.datastrong {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.datastrongfixed {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.date {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.document {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.errorbanner {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.errorcontent {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.errorcontentfixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.extendedpage {
    background-color: #fafbfe;
    border-style: solid;
    border-width: 1pt;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
    text-align: center;
}
.fatalbanner {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.fatalcontent {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.fatalcontentfixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.folderaction {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.footer {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.footeremphasis {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.footeremphasisfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.footerempty {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.footerfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.footerstrong {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.footerstrongfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.frame {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.graph > colgroup {
    border-left: 1px solid #c1c1c1;
    border-right: 1px solid #c1c1c1;
}
.graph > tbody, .graph > thead, .graph > tfoot {
    border-top: 1px solid #c1c1c1;
    border-bottom: 1px solid #c1c1c1;
}
.graph { border: hidden; }
.graph {
    background-color: #fafbfe;
    border: 1px solid #c1c1c1;
    border-collapse: separate;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    }
.header {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.headeremphasis {
    background-color: #d8dbd3;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.headeremphasisfixed {
    background-color: #d8dbd3;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.headerempty {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.headerfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.headersandfooters {
    background-color: #edf2f9;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.headerstrong {
    background-color: #d8dbd3;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.headerstrongfixed {
    background-color: #d8dbd3;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.heading1, .heading2, .heading3, .heading4, .heading5, .heading6 { font-family: Arial, Helvetica, sans-serif }
.index {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.indexaction, .indexitem {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.indexprocname {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.indextitle {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: bold;
}
.layoutcontainer, .layoutregion {
    border-width: 0;
    border-spacing: 30px;
}
.linecontent {
    background-color: #fafbfe;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
a:link { color: #0000ff }
.list {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: disc;
}
.list10 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: square;
}
.list2 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: circle;
}
.list3, .list4, .list5, .list6, .list7, .list8, .list9 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: square;
}
.listitem {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: disc;
}
.listitem10 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: square;
}
.listitem2 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: circle;
}
.listitem3, .listitem4, .listitem5, .listitem6, .listitem7, .listitem8, .listitem9 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: square;
}
.note {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.notebanner {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.notecontent {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.notecontentfixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.output > colgroup {
    border-left: 1px solid #c1c1c1;
    border-right: 1px solid #c1c1c1;
}
.output > tbody, .output > thead, .output > tfoot {
    border-top: 1px solid #c1c1c1;
    border-bottom: 1px solid #c1c1c1;
}
.output { border: hidden; }
.output {
    background-color: #fafbfe;
    border: 1px solid #c1c1c1;
    border-collapse: separate;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    }
.pageno {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
    text-align: right;
    vertical-align: top;
}
.pages {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: decimal;
    margin-left: 8px;
    margin-right: 8px;
}
.pagesdate {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.pagesitem {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.pagesproclabel, .pagesprocname {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.pagestitle {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: bold;
}
.paragraph {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.parskip > col, .parskip > colgroup > col, .parskip > colgroup, .parskip > tr, .parskip > * > tr, .parskip > thead, .parskip > tbody, .parskip > tfoot { border: none; }
.parskip {
    border: none;
    border-spacing: 0;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
    }
.prepage {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    text-align: left;
}
.proctitle {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.proctitlefixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowfooter {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowfooteremphasis {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.rowfooteremphasisfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.rowfooterempty {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowfooterfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.rowfooterstrong {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowfooterstrongfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowheader {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowheaderemphasis {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.rowheaderemphasisfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.rowheaderempty {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowheaderfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.rowheaderstrong {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowheaderstrongfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.systemfooter, .systemfooter10, .systemfooter2, .systemfooter3, .systemfooter4, .systemfooter5, .systemfooter6, .systemfooter7, .systemfooter8, .systemfooter9 {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.systemtitle, .systemtitle10, .systemtitle2, .systemtitle3, .systemtitle4, .systemtitle5, .systemtitle6, .systemtitle7, .systemtitle8, .systemtitle9 {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size: small;
    font-style: normal;
    font-weight: bold;
}
.systitleandfootercontainer > col, .systitleandfootercontainer > colgroup > col, .systitleandfootercontainer > colgroup, .systitleandfootercontainer > tr, .systitleandfootercontainer > * > tr, .systitleandfootercontainer > thead, .systitleandfootercontainer > tbody, .systitleandfootercontainer > tfoot { border: none; }
.systitleandfootercontainer {
    background-color: #fafbfe;
    border: none;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.table > col, .table > colgroup > col {
    border-left: 1px solid #c1c1c1;
    border-right: 0 solid #c1c1c1;
}
.table > tr, .table > * > tr {
    border-top: 1px solid #c1c1c1;
    border-bottom: 0 solid #c1c1c1;
}
.table { border: hidden; }
.table {
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 1px 0 0 1px;
    border-collapse: collapse;
    border-spacing: 0;
    }
.titleandnotecontainer > col, .titleandnotecontainer > colgroup > col, .titleandnotecontainer > colgroup, .titleandnotecontainer > tr, .titleandnotecontainer > * > tr, .titleandnotecontainer > thead, .titleandnotecontainer > tbody, .titleandnotecontainer > tfoot { border: none; }
.titleandnotecontainer {
    background-color: #fafbfe;
    border: none;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.titlesandfooters {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.usertext {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
a:visited { color: #800080 }
.warnbanner {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.warncontent {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.warncontentfixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
/*]]>*/
</style>
</head>
<body class="l body">
<div style="padding-bottom: 8px; padding-top: 1px">
<div id="IDX" class="systitleandfootercontainer" style="border-spacing: 1px">
<p><span class="c systemtitle">Chapter 2 Table 2.1</span> </p>
</div>
<div class="proc_title_group">
<p class="c proctitle">The MCMC Procedure</p>
</div>
<div style="padding-bottom: 8px; padding-top: 1px">
<div style="padding-bottom: 8px; padding-top: 1px">
<div class="c">
<img style="height: 480px; width: 640px" alt="Posterior Density Plots: Panel 1" src="data:image/png;base64,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//M//zPvigSWVgE8a9aswcFB9udQKBQKhWbNSrfrq1KT3++/6667vva1ry1ZsoR3LZLwyiuvZGZmbtmyhXchEqLRaJYtW/aZz3xGq9U+/vjjvb29586d411UmmtsbPza1772wQcf+Hy+L3/5y7fddlua/dKTVgF83XXXtbS0sD+3t7cXFBREB8QgnoGBgdtuu+3BBx985JFHeNciFX/4wx927dolk8lkMtno6Ghubu7u3bt5F5Xm5s2bd+7cuVAoREQymYyIlEol76LS3Pvvv79p06Y1a9bMmjXriSeeOHv27IULF3gXJaS0CuCVK1eGQqFnn322p6fnP/7jP+6++27eFaW/np6eW2+99bHHHnv00Ud51yIhu3btiozJyMjo6+vbuhVXxItr8eLFRqPx6aef9nq9//3f/20ymcrKyngXleZWrVr1zjvvHDt2zO/3/+hHPzKZTEVFRbyLElJaBbBSqfz973//zDPPFBUV+Xy+b3/727wrSn/PPPPM4cOHH3roITYaUyjS8H4tACKSyWSvvfbavn37CgoKfve73+3cuVMuT6u/P1PQmjVrvv3tbz/wwAOzZ89+88033377bTb3kDbS6hgSAADAjJBux5AAAABmCgQwAAAABwhgAAAADhDAAAAAHCCAAQAAOEAAAwAAcIAABgAA4AABDAAAwAECGAAAgAMEMAAAAAcIYAAAAA4QwAAAABwggAHSgdvtXrBgQTAY5F0IAEwXLo8DSAdGo/HUqVO8qwCAGGAEDDDD2O12hUKxf//+0tLSkpKS5557jogcDkeaXZUKkPYwAgaYecLh8K9//evjx4+3trbecccdCxcuLCsr410UAMQGI2CAmUcmk/30pz+dPXv2jTfeuH379ldffZV3RQAQMwQwwMwjk8lyc3PZn0tLSy9evMi3HgCIAwIYYOaJRCIej4f9+fz586WlpXzrAYA4IIABZp5IJPLVr361t7f3wIEDr7zyyic/+UneFQFAzLAJC2DmkcvlDz744KJFixQKxU9+8pPFixc7HA7eRQFAbBDAADPS5s2bu7u7o/9YXFwciUQ41gMAscIUNAAAAAcIYAAAAA4QwAAzTHl5eSgU4l0FACQKAQwAAMABAhgAAIADBDAAAAAHCGAAAAAOEMAAAAAcIIABAAA4QAADAABwgAAGAADgAAEMAADAAQIYAACAAwQwAAAABwhgAAAADhRE1NzczLsMAAAAafn/AWYg/hRkEtQpAAAAAElFTkSuQmCC"/>
</div>
</div>
</div>
</div>
</body>
</html>




## 2.2 Fundamentals of Bayesian Inference

*Bayesian inference is based on the subjective view of probability. Rather than specifying a rule for constructing an interval that will contain the true value, of a parameter a specified proportion of the time in an infinite sequence of repetitions of the same experiment, Bayesians combine knowledge of a parameter available before data are analyzed with information collected during an experiment to update their belief about the value of the parameter after the experiment has been completed. Bayesians summarize knowledge of the parameter after seeing the results of an experiment using a probability density function. The use of a probability density function to summarize uncertainty about the value of a parameter does not mean that we believe that values of unknown parameters are random; it only means that our knowledge of a parameter’s value is uncertain, and that our uncertainty about this value can be represented using an appropriate probability density function.* (Hamada, et. al 2008)

We use Baye's Theorem to update the probability density function representing our uncertainty about a given parameter:

$$
p\left(\theta \, | \, y\right) = \frac{f\left(\textbf{y} \, | \, \theta \right) p \left( \theta \right)}{m\left(\textbf{y}\right)} \: \: \: \: \: \: \: \: \: \: (2.6)
$$

where

$$
m\left(\textbf{y}\right) = \int f\left(\textbf{y} \, | \, \theta\right)p \left( \theta \right)d \theta
$$

The function $p\left(\theta \, | \, y\right)$ is called the *posterior density*.<br>
$p \left( \theta \right)$ is called the *prior density*.<br>
$m\left(\textbf{y}\right)$ is the *marginal density*.<br>
$f\left(\textbf{y} \, | \, \theta\right)$ is the *sampling density*.

### 2.2.1 The Prior Distribution

Our parameter of interest in the value of the success probability $\pi$; could be any value in the unit interval $\left( 0,1\right)$.

From the Bayesian perspective, we specify prior information using a probability density function on the unit interval.
* Prior information could come from previous experiments, expert judgement, or published results
    * The probability density function is usually more concentrated in a particular region
        * Informative prior

* Alternatively, if we have very little information about the experiment at hand, we can use the probability density function to robustly express our uncertainty
    * The probability density function is flat
        * Diffuse prior
        
Prior distribution for $\pi$ is uniform (that is all values are equally likely) on the unit interval:

$$
p\left( \pi \right) = 1, \: \: \: 0 < \pi < 1
$$
        
Example of informative prior and diffuse priors:


```sas
%let a = 2.4;
%let b = 2;

data priors;
    do i =1 to 1000000;
        uniform_ = rand('uniform');
        beta_ = rand('beta',&a., &b.);
        output;
    end;
run;

ods graphics on;
Title "Informative and Diffuse Priors";
proc sgplot data=priors;
density uniform_ / type=kernel lineattrs=(pattern=1) scale=density legendlabel='Uniform';
density beta_ / type=kernel lineattrs=(pattern=2) scale=density legendlabel='Beta(2.4,2)';
keylegend / location=inside position=topright across=1 noborder linelength=20;
xaxis min=0.0000001 max=0.99999 label='pi'; 
run;
```




<!DOCTYPE html>
<html lang="en" xml:lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta charset="utf-8"/>
<meta content="SAS 9.4" name="generator"/>
<title>SAS Output</title>
<style>
/*<![CDATA[*/
.body.c > table, .body.c > pre, .body.c div > table,
.body.c div > pre, .body.c > table, .body.c > pre,
.body.j > table, .body.j > pre, .body.j div > table,
.body.j div > pre, .body.j > table, .body.j > pre,
.body.c p.note, .body.c p.warning, .body.c p.error, .body.c p.fatal,
.body.j p.note, .body.j p.warning, .body.j p.error, .body.j p.fatal,
.body.c > table.layoutcontainer, .body.j > table.layoutcontainer { margin-left: auto; margin-right: auto }
.layoutregion.l table, .layoutregion.l pre, .layoutregion.l p.note,
.layoutregion.l p.warning, .layoutregion.l p.error, .layoutregion.l p.fatal { margin-left: 0 }
.layoutregion.c table, .layoutregion.c pre, .layoutregion.c p.note,
.layoutregion.c p.warning, .layoutregion.c p.error, .layoutregion.c p.fatal { margin-left: auto; margin-right: auto }
.layoutregion.r table, .layoutregion.r pre, .layoutregion.r p.note,
.layoutregion.r table, .layoutregion.r pre, .layoutregion.r p.note,
.layoutregion.r p.warning, .layoutregion.r p.error, .layoutregion.r p.fatal { margin-right: 0 }
article, aside, details, figcaption, figure, footer, header, hgroup, nav, section { display: block }
html{ font-size: 100% }
.body { margin: 1em; font-size: 13px; line-height: 1.231 }
sup { position: relative; vertical-align: baseline; bottom: 0.25em; font-size: 0.8em }
sub { position: relative; vertical-align: baseline; top: 0.25em; font-size: 0.8em }
ul, ol { margin: 1em 0; padding: 0 0 0 40px }
dd { margin: 0 0 0 40px }
nav ul, nav ol { list-style: none; list-style-image: none; margin: 0; padding: 0 }
img { border: 0; vertical-align: middle }
svg:not(:root) { overflow: hidden }
figure { margin: 0 }
table { border-collapse: collapse; border-spacing: 0 }
.layoutcontainer { border-collapse: separate; border-spacing: 0 }
p { margin-top: 0; text-align: left }
h1.heading1 { text-align: left }
h2.heading2 { text-align: left }
h3.heading3 { text-align: left }
h4.heading4 { text-align: left }
h5.heading5 { text-align: left }
h6.heading6 { text-align: left }
span { text-align: left }
table { margin-bottom: 1em }
td, th { text-align: left; padding: 3px 6px; vertical-align: top }
td[class$="fixed"], th[class$="fixed"] { white-space: pre }
section, article { padding-top: 1px; padding-bottom: 8px }
hr.pagebreak { height: 0px; border: 0; border-bottom: 1px solid #c0c0c0; margin: 1em 0 }
.stacked-value { text-align: left; display: block }
.stacked-cell > .stacked-value, td.data > td.data, th.data > td.data, th.data > th.data, td.data > th.data, th.header > th.header { border: 0 }
.stacked-cell > div.data { border-width: 0 }
.systitleandfootercontainer { white-space: nowrap; margin-bottom: 1em }
.systitleandfootercontainer > p { margin: 0 }
.systitleandfootercontainer > p > span { display: inline-block; width: 100%; white-space: normal }
.batch { display: table }
.toc { display: none }
.proc_note_group, .proc_title_group { margin-bottom: 1em }
p.proctitle { margin: 0 }
p.note, p.warning, p.error, p.fatal { display: table }
.notebanner, .warnbanner, .errorbanner, .fatalbanner,
.notecontent, .warncontent, .errorcontent, .fatalcontent { display: table-cell; padding: 0.5em }
.notebanner, .warnbanner, .errorbanner, .fatalbanner { padding-right: 0 }
.body > div > ol li { text-align: left }
.beforecaption > h4 { margin-top: 0; margin-bottom: 0 }
.c { text-align: center }
.r { text-align: right }
.l { text-align: left }
.j { text-align: justify }
.d { text-align: right }
.b { vertical-align: bottom }
.m { vertical-align: middle }
.t { vertical-align: top }
.accessiblecaption {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
a:active { color: #800080 }
.aftercaption {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
    padding-top: 4pt;
}
.batch > colgroup {
    border-left: 1px solid #c1c1c1;
    border-right: 1px solid #c1c1c1;
}
.batch > tbody, .batch > thead, .batch > tfoot {
    border-top: 1px solid #c1c1c1;
    border-bottom: 1px solid #c1c1c1;
}
.batch { border: hidden; }
.batch {
    background-color: #fafbfe;
    border: 1px solid #c1c1c1;
    border-collapse: separate;
    border-spacing: 1px;
    color: #000000;
    font-family: 'SAS Monospace', 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    padding: 7px;
    }
.beforecaption {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.body {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    margin-left: 8px;
    margin-right: 8px;
}
.bodydate {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    text-align: right;
    vertical-align: top;
    width: 100%;
}
.bycontentfolder {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.byline {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.bylinecontainer > col, .bylinecontainer > colgroup > col, .bylinecontainer > colgroup, .bylinecontainer > tr, .bylinecontainer > * > tr, .bylinecontainer > thead, .bylinecontainer > tbody, .bylinecontainer > tfoot { border: none; }
.bylinecontainer {
    background-color: #fafbfe;
    border: none;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.caption {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.cell, .container {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.contentfolder, .contentitem {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.contentproclabel, .contentprocname {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.contents {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: decimal;
    margin-left: 8px;
    margin-right: 8px;
}
.contentsdate {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.contenttitle {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: bold;
}
.continued {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
    width: 100%;
}
.data, .dataemphasis {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.dataemphasisfixed {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.dataempty {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.datafixed {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.datastrong {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.datastrongfixed {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.date {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.document {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.errorbanner {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.errorcontent {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.errorcontentfixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.extendedpage {
    background-color: #fafbfe;
    border-style: solid;
    border-width: 1pt;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
    text-align: center;
}
.fatalbanner {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.fatalcontent {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.fatalcontentfixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.folderaction {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.footer {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.footeremphasis {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.footeremphasisfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.footerempty {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.footerfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.footerstrong {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.footerstrongfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.frame {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.graph > colgroup {
    border-left: 1px solid #c1c1c1;
    border-right: 1px solid #c1c1c1;
}
.graph > tbody, .graph > thead, .graph > tfoot {
    border-top: 1px solid #c1c1c1;
    border-bottom: 1px solid #c1c1c1;
}
.graph { border: hidden; }
.graph {
    background-color: #fafbfe;
    border: 1px solid #c1c1c1;
    border-collapse: separate;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    }
.header {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.headeremphasis {
    background-color: #d8dbd3;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.headeremphasisfixed {
    background-color: #d8dbd3;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.headerempty {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.headerfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.headersandfooters {
    background-color: #edf2f9;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.headerstrong {
    background-color: #d8dbd3;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.headerstrongfixed {
    background-color: #d8dbd3;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.heading1, .heading2, .heading3, .heading4, .heading5, .heading6 { font-family: Arial, Helvetica, sans-serif }
.index {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.indexaction, .indexitem {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.indexprocname {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.indextitle {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: bold;
}
.layoutcontainer, .layoutregion {
    border-width: 0;
    border-spacing: 30px;
}
.linecontent {
    background-color: #fafbfe;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
a:link { color: #0000ff }
.list {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: disc;
}
.list10 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: square;
}
.list2 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: circle;
}
.list3, .list4, .list5, .list6, .list7, .list8, .list9 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: square;
}
.listitem {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: disc;
}
.listitem10 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: square;
}
.listitem2 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: circle;
}
.listitem3, .listitem4, .listitem5, .listitem6, .listitem7, .listitem8, .listitem9 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: square;
}
.note {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.notebanner {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.notecontent {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.notecontentfixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.output > colgroup {
    border-left: 1px solid #c1c1c1;
    border-right: 1px solid #c1c1c1;
}
.output > tbody, .output > thead, .output > tfoot {
    border-top: 1px solid #c1c1c1;
    border-bottom: 1px solid #c1c1c1;
}
.output { border: hidden; }
.output {
    background-color: #fafbfe;
    border: 1px solid #c1c1c1;
    border-collapse: separate;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    }
.pageno {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
    text-align: right;
    vertical-align: top;
}
.pages {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: decimal;
    margin-left: 8px;
    margin-right: 8px;
}
.pagesdate {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.pagesitem {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.pagesproclabel, .pagesprocname {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.pagestitle {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: bold;
}
.paragraph {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.parskip > col, .parskip > colgroup > col, .parskip > colgroup, .parskip > tr, .parskip > * > tr, .parskip > thead, .parskip > tbody, .parskip > tfoot { border: none; }
.parskip {
    border: none;
    border-spacing: 0;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
    }
.prepage {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    text-align: left;
}
.proctitle {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.proctitlefixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowfooter {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowfooteremphasis {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.rowfooteremphasisfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.rowfooterempty {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowfooterfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.rowfooterstrong {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowfooterstrongfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowheader {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowheaderemphasis {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.rowheaderemphasisfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.rowheaderempty {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowheaderfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.rowheaderstrong {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowheaderstrongfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.systemfooter, .systemfooter10, .systemfooter2, .systemfooter3, .systemfooter4, .systemfooter5, .systemfooter6, .systemfooter7, .systemfooter8, .systemfooter9 {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.systemtitle, .systemtitle10, .systemtitle2, .systemtitle3, .systemtitle4, .systemtitle5, .systemtitle6, .systemtitle7, .systemtitle8, .systemtitle9 {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size: small;
    font-style: normal;
    font-weight: bold;
}
.systitleandfootercontainer > col, .systitleandfootercontainer > colgroup > col, .systitleandfootercontainer > colgroup, .systitleandfootercontainer > tr, .systitleandfootercontainer > * > tr, .systitleandfootercontainer > thead, .systitleandfootercontainer > tbody, .systitleandfootercontainer > tfoot { border: none; }
.systitleandfootercontainer {
    background-color: #fafbfe;
    border: none;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.table > col, .table > colgroup > col {
    border-left: 1px solid #c1c1c1;
    border-right: 0 solid #c1c1c1;
}
.table > tr, .table > * > tr {
    border-top: 1px solid #c1c1c1;
    border-bottom: 0 solid #c1c1c1;
}
.table { border: hidden; }
.table {
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 1px 0 0 1px;
    border-collapse: collapse;
    border-spacing: 0;
    }
.titleandnotecontainer > col, .titleandnotecontainer > colgroup > col, .titleandnotecontainer > colgroup, .titleandnotecontainer > tr, .titleandnotecontainer > * > tr, .titleandnotecontainer > thead, .titleandnotecontainer > tbody, .titleandnotecontainer > tfoot { border: none; }
.titleandnotecontainer {
    background-color: #fafbfe;
    border: none;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.titlesandfooters {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.usertext {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
a:visited { color: #800080 }
.warnbanner {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.warncontent {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.warncontentfixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
/*]]>*/
</style>
</head>
<body class="l body">
<div style="padding-bottom: 8px; padding-top: 1px">
<div id="IDX" style="padding-bottom: 8px; padding-top: 1px">
<div class="c">
<img style="height: 480px; width: 640px" alt="The SGPlot Procedure" src="data:image/png;base64,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"/>
</div>
</div>
</div>
</body>
</html>




The `Beta(2.4,2)` pdf above corresponds to data collected prior to 1980 which were conducted prior to the experiements who generated the data in Table 2.1.

Beta probability distribution function:

$$
p\left( \pi \, | \, \alpha, \beta \right) = \frac{\Gamma \left( \alpha + \beta \right)}{\Gamma \left( \alpha \right) \Gamma \left( \beta \right)} \pi ^{\alpha - 1} \left( 1 - \pi \right)^{\beta-1}, \: \: \: \: \: \: 0 \leq \pi \leq 1, \: \: \: \alpha,\beta  > 0
$$

Note that the `Beta(2.4,2)` pdf lies mainly between 0.2 and 0.8 and the prior distribution has
* Mean: $\frac{\alpha}{\left( \alpha + \beta \right)}$ = 0.545
* Mode: $\frac{\alpha - 1}{\alpha + \beta - 2}$ = 0.583
* 70% Confidence Interval: $\left( 0.25 - 0.75 \right)$
    * Compare this to the uniform generation where $\left( 0.25 - 0.75 \right)$ is only 50% confidence
    * Note: a uniform distribution is just a `Beta(1,1)`
    
### 2.2.2 Combining Data with Prior Information

The prior distribution $p\left( \theta \right)$ reflects knowledge of a parameter before an experiment is conducted and new data is generated. We update our prior belief about the parameter using this new information to come up with a $\textit{posterior distribution}$. We use Bayes' Theorem:

$$
p\left(\theta \, | \, y\right) = \frac{f\left(\textbf{y} \, | \, \theta \right) p \left( \theta \right)}{m\left(\textbf{y}\right)} \: \: \: \: \: \: \: \: \: \: (2.6)
$$

Or in plain english:

$$
\text{posterior} \: \propto \: \text{likelihood} \times \text{prior}
$$

When we reexpress Bayes' Theorem this way, the proportionality constant absorbs the term $m(\textbf{y})$ as it does not depend on the model parameter $\theta$:

$$
p\left( \theta \, | \, \textbf{y} \right) \: \propto \: f\left( \textbf{y} \, | \, \theta  \right)p(\theta) \: \: \: \: \: \: \: \: \: \: (2.7)
$$

***Example 2.2: Calculating posterior distributions for Table 2.1***

In the graph above we discussed two prior distributions, a diffuse prior `Beta(1,1)` and an informative prior `Beta(2.4,2)`. Substituting the diffuse prior distribution `Beta(1,1)` $p(\pi)$ for $p(\theta)$ in Eq. 2.7 leads to a posterior distribution for the launch vehicle success probability that is proportional to:

$$
\begin{align*}
p\left(\pi \, | \, y\right) \: &\propto \: \pi^{3}\left( 1 - \pi \right)^{8} \times \pi^{1-1}\left( 1 - \pi \right)^{1-1}\\ 
 &\propto \pi^{4-1} \left( 1 - \pi \right)^{9-1}
\end{align*}
$$

If you look closely at the equation above, you'll notice that the posterior distribution is proportional to yet another beta distribution. Because the posterior distribution is a beta distribution, we can analytically determine the constant of proportionality (aka normalizing constant), which in this case is equal to $\frac{\Gamma(13)}{\left[ \Gamma(4) \Gamma(9) \right]}$

Similarly, we can substitute the informative prior distribution `Beta(2.4,2)` $p(\pi)$ for $p(\theta)$ in Eq. 2.7 leads to a posterior distribution for the launch vehicle success probability that is proportional to:

$$
\begin{align*}
p\left(\pi \, | \, y\right) \: &\propto \: \pi^{3}\left( 1 - \pi \right)^{8} \times \pi^{2.4-1}\left( 1 - \pi \right)^{2-1}\\ 
 &\propto \pi^{5.4-1} \left( 1 - \pi \right)^{10-1}
\end{align*}
$$

Once again, the posterior distribution is proportional to a beta distribution, so we can determine it's normalizing constant, which in this case is equal to $\frac{\Gamma(15.4)}{\left[ \Gamma(5.4) \Gamma(10) \right]}$.

Ok - so by now it should become readily apparent that our choice in prior is very important in determining our posterior distribution. Let's visualize the difference in our choice of prior using our results from Example 2.2:


```sas
%let a_prior_diffuse = 1;
%let b_prior_diffuse = 1;
%let a_prior_informative = 2.4;
%let b_prior_informative = 2;

proc sql noprint;
    create table tbl as
        select count(*) as n, sum(outcome) as y, sum(outcome)/count(*) as pi
        from table2_1;
quit; 

proc mcmc data=tbl outpost=ex2_2_diffuse seed=23 nmc=10000 maxtune=0 statistics=none diagnostics=none plots=none;
   ods exclude nobs parameters;
   parm diffuse;
   prior diffuse ~ beta(&a_prior_diffuse., &b_prior_diffuse.);
   model y ~ binomial(n,diffuse);
run;

proc mcmc data=tbl outpost=ex2_2_info seed=23 nmc=10000 maxtune=0 statistics=none diagnostics=none plots=none;
   ods exclude nobs parameters;
   parm info;
   prior info ~ beta(&a_prior_informative., &b_prior_informative.);
   model y ~ binomial(n,info);
run;

data plots;
    set ex2_2_diffuse ex2_2_info;
run;
```




<!DOCTYPE html>
<html lang="en" xml:lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta charset="utf-8"/>
<meta content="SAS 9.4" name="generator"/>
<title>SAS Output</title>
<style>
/*<![CDATA[*/
.body.c > table, .body.c > pre, .body.c div > table,
.body.c div > pre, .body.c > table, .body.c > pre,
.body.j > table, .body.j > pre, .body.j div > table,
.body.j div > pre, .body.j > table, .body.j > pre,
.body.c p.note, .body.c p.warning, .body.c p.error, .body.c p.fatal,
.body.j p.note, .body.j p.warning, .body.j p.error, .body.j p.fatal,
.body.c > table.layoutcontainer, .body.j > table.layoutcontainer { margin-left: auto; margin-right: auto }
.layoutregion.l table, .layoutregion.l pre, .layoutregion.l p.note,
.layoutregion.l p.warning, .layoutregion.l p.error, .layoutregion.l p.fatal { margin-left: 0 }
.layoutregion.c table, .layoutregion.c pre, .layoutregion.c p.note,
.layoutregion.c p.warning, .layoutregion.c p.error, .layoutregion.c p.fatal { margin-left: auto; margin-right: auto }
.layoutregion.r table, .layoutregion.r pre, .layoutregion.r p.note,
.layoutregion.r table, .layoutregion.r pre, .layoutregion.r p.note,
.layoutregion.r p.warning, .layoutregion.r p.error, .layoutregion.r p.fatal { margin-right: 0 }
article, aside, details, figcaption, figure, footer, header, hgroup, nav, section { display: block }
html{ font-size: 100% }
.body { margin: 1em; font-size: 13px; line-height: 1.231 }
sup { position: relative; vertical-align: baseline; bottom: 0.25em; font-size: 0.8em }
sub { position: relative; vertical-align: baseline; top: 0.25em; font-size: 0.8em }
ul, ol { margin: 1em 0; padding: 0 0 0 40px }
dd { margin: 0 0 0 40px }
nav ul, nav ol { list-style: none; list-style-image: none; margin: 0; padding: 0 }
img { border: 0; vertical-align: middle }
svg:not(:root) { overflow: hidden }
figure { margin: 0 }
table { border-collapse: collapse; border-spacing: 0 }
.layoutcontainer { border-collapse: separate; border-spacing: 0 }
p { margin-top: 0; text-align: left }
h1.heading1 { text-align: left }
h2.heading2 { text-align: left }
h3.heading3 { text-align: left }
h4.heading4 { text-align: left }
h5.heading5 { text-align: left }
h6.heading6 { text-align: left }
span { text-align: left }
table { margin-bottom: 1em }
td, th { text-align: left; padding: 3px 6px; vertical-align: top }
td[class$="fixed"], th[class$="fixed"] { white-space: pre }
section, article { padding-top: 1px; padding-bottom: 8px }
hr.pagebreak { height: 0px; border: 0; border-bottom: 1px solid #c0c0c0; margin: 1em 0 }
.stacked-value { text-align: left; display: block }
.stacked-cell > .stacked-value, td.data > td.data, th.data > td.data, th.data > th.data, td.data > th.data, th.header > th.header { border: 0 }
.stacked-cell > div.data { border-width: 0 }
.systitleandfootercontainer { white-space: nowrap; margin-bottom: 1em }
.systitleandfootercontainer > p { margin: 0 }
.systitleandfootercontainer > p > span { display: inline-block; width: 100%; white-space: normal }
.batch { display: table }
.toc { display: none }
.proc_note_group, .proc_title_group { margin-bottom: 1em }
p.proctitle { margin: 0 }
p.note, p.warning, p.error, p.fatal { display: table }
.notebanner, .warnbanner, .errorbanner, .fatalbanner,
.notecontent, .warncontent, .errorcontent, .fatalcontent { display: table-cell; padding: 0.5em }
.notebanner, .warnbanner, .errorbanner, .fatalbanner { padding-right: 0 }
.body > div > ol li { text-align: left }
.beforecaption > h4 { margin-top: 0; margin-bottom: 0 }
.c { text-align: center }
.r { text-align: right }
.l { text-align: left }
.j { text-align: justify }
.d { text-align: right }
.b { vertical-align: bottom }
.m { vertical-align: middle }
.t { vertical-align: top }
.accessiblecaption {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
a:active { color: #800080 }
.aftercaption {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
    padding-top: 4pt;
}
.batch > colgroup {
    border-left: 1px solid #c1c1c1;
    border-right: 1px solid #c1c1c1;
}
.batch > tbody, .batch > thead, .batch > tfoot {
    border-top: 1px solid #c1c1c1;
    border-bottom: 1px solid #c1c1c1;
}
.batch { border: hidden; }
.batch {
    background-color: #fafbfe;
    border: 1px solid #c1c1c1;
    border-collapse: separate;
    border-spacing: 1px;
    color: #000000;
    font-family: 'SAS Monospace', 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    padding: 7px;
    }
.beforecaption {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.body {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    margin-left: 8px;
    margin-right: 8px;
}
.bodydate {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    text-align: right;
    vertical-align: top;
    width: 100%;
}
.bycontentfolder {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.byline {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.bylinecontainer > col, .bylinecontainer > colgroup > col, .bylinecontainer > colgroup, .bylinecontainer > tr, .bylinecontainer > * > tr, .bylinecontainer > thead, .bylinecontainer > tbody, .bylinecontainer > tfoot { border: none; }
.bylinecontainer {
    background-color: #fafbfe;
    border: none;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.caption {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.cell, .container {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.contentfolder, .contentitem {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.contentproclabel, .contentprocname {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.contents {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: decimal;
    margin-left: 8px;
    margin-right: 8px;
}
.contentsdate {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.contenttitle {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: bold;
}
.continued {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
    width: 100%;
}
.data, .dataemphasis {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.dataemphasisfixed {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.dataempty {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.datafixed {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.datastrong {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.datastrongfixed {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.date {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.document {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.errorbanner {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.errorcontent {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.errorcontentfixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.extendedpage {
    background-color: #fafbfe;
    border-style: solid;
    border-width: 1pt;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
    text-align: center;
}
.fatalbanner {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.fatalcontent {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.fatalcontentfixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.folderaction {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.footer {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.footeremphasis {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.footeremphasisfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.footerempty {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.footerfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.footerstrong {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.footerstrongfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.frame {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.graph > colgroup {
    border-left: 1px solid #c1c1c1;
    border-right: 1px solid #c1c1c1;
}
.graph > tbody, .graph > thead, .graph > tfoot {
    border-top: 1px solid #c1c1c1;
    border-bottom: 1px solid #c1c1c1;
}
.graph { border: hidden; }
.graph {
    background-color: #fafbfe;
    border: 1px solid #c1c1c1;
    border-collapse: separate;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    }
.header {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.headeremphasis {
    background-color: #d8dbd3;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.headeremphasisfixed {
    background-color: #d8dbd3;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.headerempty {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.headerfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.headersandfooters {
    background-color: #edf2f9;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.headerstrong {
    background-color: #d8dbd3;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.headerstrongfixed {
    background-color: #d8dbd3;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.heading1, .heading2, .heading3, .heading4, .heading5, .heading6 { font-family: Arial, Helvetica, sans-serif }
.index {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.indexaction, .indexitem {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.indexprocname {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.indextitle {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: bold;
}
.layoutcontainer, .layoutregion {
    border-width: 0;
    border-spacing: 30px;
}
.linecontent {
    background-color: #fafbfe;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
a:link { color: #0000ff }
.list {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: disc;
}
.list10 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: square;
}
.list2 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: circle;
}
.list3, .list4, .list5, .list6, .list7, .list8, .list9 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: square;
}
.listitem {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: disc;
}
.listitem10 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: square;
}
.listitem2 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: circle;
}
.listitem3, .listitem4, .listitem5, .listitem6, .listitem7, .listitem8, .listitem9 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: square;
}
.note {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.notebanner {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.notecontent {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.notecontentfixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.output > colgroup {
    border-left: 1px solid #c1c1c1;
    border-right: 1px solid #c1c1c1;
}
.output > tbody, .output > thead, .output > tfoot {
    border-top: 1px solid #c1c1c1;
    border-bottom: 1px solid #c1c1c1;
}
.output { border: hidden; }
.output {
    background-color: #fafbfe;
    border: 1px solid #c1c1c1;
    border-collapse: separate;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    }
.pageno {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
    text-align: right;
    vertical-align: top;
}
.pages {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: decimal;
    margin-left: 8px;
    margin-right: 8px;
}
.pagesdate {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.pagesitem {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.pagesproclabel, .pagesprocname {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.pagestitle {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: bold;
}
.paragraph {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.parskip > col, .parskip > colgroup > col, .parskip > colgroup, .parskip > tr, .parskip > * > tr, .parskip > thead, .parskip > tbody, .parskip > tfoot { border: none; }
.parskip {
    border: none;
    border-spacing: 0;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
    }
.prepage {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    text-align: left;
}
.proctitle {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.proctitlefixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowfooter {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowfooteremphasis {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.rowfooteremphasisfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.rowfooterempty {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowfooterfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.rowfooterstrong {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowfooterstrongfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowheader {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowheaderemphasis {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.rowheaderemphasisfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.rowheaderempty {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowheaderfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.rowheaderstrong {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowheaderstrongfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.systemfooter, .systemfooter10, .systemfooter2, .systemfooter3, .systemfooter4, .systemfooter5, .systemfooter6, .systemfooter7, .systemfooter8, .systemfooter9 {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.systemtitle, .systemtitle10, .systemtitle2, .systemtitle3, .systemtitle4, .systemtitle5, .systemtitle6, .systemtitle7, .systemtitle8, .systemtitle9 {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size: small;
    font-style: normal;
    font-weight: bold;
}
.systitleandfootercontainer > col, .systitleandfootercontainer > colgroup > col, .systitleandfootercontainer > colgroup, .systitleandfootercontainer > tr, .systitleandfootercontainer > * > tr, .systitleandfootercontainer > thead, .systitleandfootercontainer > tbody, .systitleandfootercontainer > tfoot { border: none; }
.systitleandfootercontainer {
    background-color: #fafbfe;
    border: none;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.table > col, .table > colgroup > col {
    border-left: 1px solid #c1c1c1;
    border-right: 0 solid #c1c1c1;
}
.table > tr, .table > * > tr {
    border-top: 1px solid #c1c1c1;
    border-bottom: 0 solid #c1c1c1;
}
.table { border: hidden; }
.table {
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 1px 0 0 1px;
    border-collapse: collapse;
    border-spacing: 0;
    }
.titleandnotecontainer > col, .titleandnotecontainer > colgroup > col, .titleandnotecontainer > colgroup, .titleandnotecontainer > tr, .titleandnotecontainer > * > tr, .titleandnotecontainer > thead, .titleandnotecontainer > tbody, .titleandnotecontainer > tfoot { border: none; }
.titleandnotecontainer {
    background-color: #fafbfe;
    border: none;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.titlesandfooters {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.usertext {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
a:visited { color: #800080 }
.warnbanner {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.warncontent {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.warncontentfixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
/*]]>*/
</style>
</head>
<body class="l body">
<div style="padding-bottom: 8px; padding-top: 1px">
</div>
<div style="padding-bottom: 8px; padding-top: 1px">
</div>
</body>
</html>





```sas
ods graphics on;
Title "Posterior distributions for launch vehicle success probabilities";
proc sgplot data=plots;
density info / type=kernel lineattrs=(pattern=2) scale=density legendlabel='Posterior [Prior: Beta(2.4,2)]';
density diffuse / type=kernel lineattrs=(pattern=1) scale=density legendlabel='Posterior [Prior: Beta(1,1)]';
keylegend / location=inside position=topright across=1 noborder linelength=20;
xaxis min=0 max=1 label='pi'; 
run;
```




<!DOCTYPE html>
<html lang="en" xml:lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta charset="utf-8"/>
<meta content="SAS 9.4" name="generator"/>
<title>SAS Output</title>
<style>
/*<![CDATA[*/
.body.c > table, .body.c > pre, .body.c div > table,
.body.c div > pre, .body.c > table, .body.c > pre,
.body.j > table, .body.j > pre, .body.j div > table,
.body.j div > pre, .body.j > table, .body.j > pre,
.body.c p.note, .body.c p.warning, .body.c p.error, .body.c p.fatal,
.body.j p.note, .body.j p.warning, .body.j p.error, .body.j p.fatal,
.body.c > table.layoutcontainer, .body.j > table.layoutcontainer { margin-left: auto; margin-right: auto }
.layoutregion.l table, .layoutregion.l pre, .layoutregion.l p.note,
.layoutregion.l p.warning, .layoutregion.l p.error, .layoutregion.l p.fatal { margin-left: 0 }
.layoutregion.c table, .layoutregion.c pre, .layoutregion.c p.note,
.layoutregion.c p.warning, .layoutregion.c p.error, .layoutregion.c p.fatal { margin-left: auto; margin-right: auto }
.layoutregion.r table, .layoutregion.r pre, .layoutregion.r p.note,
.layoutregion.r table, .layoutregion.r pre, .layoutregion.r p.note,
.layoutregion.r p.warning, .layoutregion.r p.error, .layoutregion.r p.fatal { margin-right: 0 }
article, aside, details, figcaption, figure, footer, header, hgroup, nav, section { display: block }
html{ font-size: 100% }
.body { margin: 1em; font-size: 13px; line-height: 1.231 }
sup { position: relative; vertical-align: baseline; bottom: 0.25em; font-size: 0.8em }
sub { position: relative; vertical-align: baseline; top: 0.25em; font-size: 0.8em }
ul, ol { margin: 1em 0; padding: 0 0 0 40px }
dd { margin: 0 0 0 40px }
nav ul, nav ol { list-style: none; list-style-image: none; margin: 0; padding: 0 }
img { border: 0; vertical-align: middle }
svg:not(:root) { overflow: hidden }
figure { margin: 0 }
table { border-collapse: collapse; border-spacing: 0 }
.layoutcontainer { border-collapse: separate; border-spacing: 0 }
p { margin-top: 0; text-align: left }
h1.heading1 { text-align: left }
h2.heading2 { text-align: left }
h3.heading3 { text-align: left }
h4.heading4 { text-align: left }
h5.heading5 { text-align: left }
h6.heading6 { text-align: left }
span { text-align: left }
table { margin-bottom: 1em }
td, th { text-align: left; padding: 3px 6px; vertical-align: top }
td[class$="fixed"], th[class$="fixed"] { white-space: pre }
section, article { padding-top: 1px; padding-bottom: 8px }
hr.pagebreak { height: 0px; border: 0; border-bottom: 1px solid #c0c0c0; margin: 1em 0 }
.stacked-value { text-align: left; display: block }
.stacked-cell > .stacked-value, td.data > td.data, th.data > td.data, th.data > th.data, td.data > th.data, th.header > th.header { border: 0 }
.stacked-cell > div.data { border-width: 0 }
.systitleandfootercontainer { white-space: nowrap; margin-bottom: 1em }
.systitleandfootercontainer > p { margin: 0 }
.systitleandfootercontainer > p > span { display: inline-block; width: 100%; white-space: normal }
.batch { display: table }
.toc { display: none }
.proc_note_group, .proc_title_group { margin-bottom: 1em }
p.proctitle { margin: 0 }
p.note, p.warning, p.error, p.fatal { display: table }
.notebanner, .warnbanner, .errorbanner, .fatalbanner,
.notecontent, .warncontent, .errorcontent, .fatalcontent { display: table-cell; padding: 0.5em }
.notebanner, .warnbanner, .errorbanner, .fatalbanner { padding-right: 0 }
.body > div > ol li { text-align: left }
.beforecaption > h4 { margin-top: 0; margin-bottom: 0 }
.c { text-align: center }
.r { text-align: right }
.l { text-align: left }
.j { text-align: justify }
.d { text-align: right }
.b { vertical-align: bottom }
.m { vertical-align: middle }
.t { vertical-align: top }
.accessiblecaption {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
a:active { color: #800080 }
.aftercaption {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
    padding-top: 4pt;
}
.batch > colgroup {
    border-left: 1px solid #c1c1c1;
    border-right: 1px solid #c1c1c1;
}
.batch > tbody, .batch > thead, .batch > tfoot {
    border-top: 1px solid #c1c1c1;
    border-bottom: 1px solid #c1c1c1;
}
.batch { border: hidden; }
.batch {
    background-color: #fafbfe;
    border: 1px solid #c1c1c1;
    border-collapse: separate;
    border-spacing: 1px;
    color: #000000;
    font-family: 'SAS Monospace', 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    padding: 7px;
    }
.beforecaption {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.body {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    margin-left: 8px;
    margin-right: 8px;
}
.bodydate {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    text-align: right;
    vertical-align: top;
    width: 100%;
}
.bycontentfolder {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.byline {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.bylinecontainer > col, .bylinecontainer > colgroup > col, .bylinecontainer > colgroup, .bylinecontainer > tr, .bylinecontainer > * > tr, .bylinecontainer > thead, .bylinecontainer > tbody, .bylinecontainer > tfoot { border: none; }
.bylinecontainer {
    background-color: #fafbfe;
    border: none;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.caption {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.cell, .container {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.contentfolder, .contentitem {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.contentproclabel, .contentprocname {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.contents {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: decimal;
    margin-left: 8px;
    margin-right: 8px;
}
.contentsdate {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.contenttitle {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: bold;
}
.continued {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
    width: 100%;
}
.data, .dataemphasis {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.dataemphasisfixed {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.dataempty {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.datafixed {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.datastrong {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.datastrongfixed {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.date {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.document {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.errorbanner {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.errorcontent {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.errorcontentfixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.extendedpage {
    background-color: #fafbfe;
    border-style: solid;
    border-width: 1pt;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
    text-align: center;
}
.fatalbanner {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.fatalcontent {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.fatalcontentfixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.folderaction {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.footer {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.footeremphasis {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.footeremphasisfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.footerempty {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.footerfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.footerstrong {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.footerstrongfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.frame {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.graph > colgroup {
    border-left: 1px solid #c1c1c1;
    border-right: 1px solid #c1c1c1;
}
.graph > tbody, .graph > thead, .graph > tfoot {
    border-top: 1px solid #c1c1c1;
    border-bottom: 1px solid #c1c1c1;
}
.graph { border: hidden; }
.graph {
    background-color: #fafbfe;
    border: 1px solid #c1c1c1;
    border-collapse: separate;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    }
.header {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.headeremphasis {
    background-color: #d8dbd3;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.headeremphasisfixed {
    background-color: #d8dbd3;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.headerempty {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.headerfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.headersandfooters {
    background-color: #edf2f9;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.headerstrong {
    background-color: #d8dbd3;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.headerstrongfixed {
    background-color: #d8dbd3;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.heading1, .heading2, .heading3, .heading4, .heading5, .heading6 { font-family: Arial, Helvetica, sans-serif }
.index {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.indexaction, .indexitem {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.indexprocname {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.indextitle {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: bold;
}
.layoutcontainer, .layoutregion {
    border-width: 0;
    border-spacing: 30px;
}
.linecontent {
    background-color: #fafbfe;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
a:link { color: #0000ff }
.list {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: disc;
}
.list10 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: square;
}
.list2 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: circle;
}
.list3, .list4, .list5, .list6, .list7, .list8, .list9 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: square;
}
.listitem {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: disc;
}
.listitem10 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: square;
}
.listitem2 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: circle;
}
.listitem3, .listitem4, .listitem5, .listitem6, .listitem7, .listitem8, .listitem9 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: square;
}
.note {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.notebanner {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.notecontent {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.notecontentfixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.output > colgroup {
    border-left: 1px solid #c1c1c1;
    border-right: 1px solid #c1c1c1;
}
.output > tbody, .output > thead, .output > tfoot {
    border-top: 1px solid #c1c1c1;
    border-bottom: 1px solid #c1c1c1;
}
.output { border: hidden; }
.output {
    background-color: #fafbfe;
    border: 1px solid #c1c1c1;
    border-collapse: separate;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    }
.pageno {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
    text-align: right;
    vertical-align: top;
}
.pages {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: decimal;
    margin-left: 8px;
    margin-right: 8px;
}
.pagesdate {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.pagesitem {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.pagesproclabel, .pagesprocname {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.pagestitle {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: bold;
}
.paragraph {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.parskip > col, .parskip > colgroup > col, .parskip > colgroup, .parskip > tr, .parskip > * > tr, .parskip > thead, .parskip > tbody, .parskip > tfoot { border: none; }
.parskip {
    border: none;
    border-spacing: 0;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
    }
.prepage {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    text-align: left;
}
.proctitle {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.proctitlefixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowfooter {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowfooteremphasis {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.rowfooteremphasisfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.rowfooterempty {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowfooterfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.rowfooterstrong {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowfooterstrongfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowheader {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowheaderemphasis {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.rowheaderemphasisfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.rowheaderempty {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowheaderfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.rowheaderstrong {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowheaderstrongfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.systemfooter, .systemfooter10, .systemfooter2, .systemfooter3, .systemfooter4, .systemfooter5, .systemfooter6, .systemfooter7, .systemfooter8, .systemfooter9 {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.systemtitle, .systemtitle10, .systemtitle2, .systemtitle3, .systemtitle4, .systemtitle5, .systemtitle6, .systemtitle7, .systemtitle8, .systemtitle9 {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size: small;
    font-style: normal;
    font-weight: bold;
}
.systitleandfootercontainer > col, .systitleandfootercontainer > colgroup > col, .systitleandfootercontainer > colgroup, .systitleandfootercontainer > tr, .systitleandfootercontainer > * > tr, .systitleandfootercontainer > thead, .systitleandfootercontainer > tbody, .systitleandfootercontainer > tfoot { border: none; }
.systitleandfootercontainer {
    background-color: #fafbfe;
    border: none;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.table > col, .table > colgroup > col {
    border-left: 1px solid #c1c1c1;
    border-right: 0 solid #c1c1c1;
}
.table > tr, .table > * > tr {
    border-top: 1px solid #c1c1c1;
    border-bottom: 0 solid #c1c1c1;
}
.table { border: hidden; }
.table {
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 1px 0 0 1px;
    border-collapse: collapse;
    border-spacing: 0;
    }
.titleandnotecontainer > col, .titleandnotecontainer > colgroup > col, .titleandnotecontainer > colgroup, .titleandnotecontainer > tr, .titleandnotecontainer > * > tr, .titleandnotecontainer > thead, .titleandnotecontainer > tbody, .titleandnotecontainer > tfoot { border: none; }
.titleandnotecontainer {
    background-color: #fafbfe;
    border: none;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.titlesandfooters {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.usertext {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
a:visited { color: #800080 }
.warnbanner {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.warncontent {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.warncontentfixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
/*]]>*/
</style>
</head>
<body class="l body">
<div style="padding-bottom: 8px; padding-top: 1px">
<div id="IDX" style="padding-bottom: 8px; padding-top: 1px">
<div class="c">
<img style="height: 480px; width: 640px" alt="The SGPlot Procedure" src="data:image/png;base64,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"/>
</div>
</div>
</div>
</body>
</html>




Part of the Bayesian value proposition is the ability to assign probabilities to certain outcomes using our posterior density. For example, let's find the probability that $\pi$ falls in the interval $\left( 0.2,0.5 \right)$.


```sas
proc rank data=plots out=ranked groups=100;
   ranks weightrank;
   var diffuse;
run;

proc rank data=plots out=ranked2 groups=100;
   ranks weightrank;
   var info;
run;

Title "Posterior probability that pi falls in interval (0.2,0.5) [Prior: Beta(1,1)]";
proc sql;
        select (max(weightrank) - min(weightrank))/100.0
        from ranked
        where abs(diffuse - 0.2) < 0.001 or abs(diffuse - 0.5) < 0.001;
quit;

Title "Posterior probability that pi falls in interval (0.2,0.5) [Prior: Beta(2.4,2)]";
proc sql;
        select (max(weightrank) - min(weightrank))/100.0
        from ranked2
        where abs(info - 0.2) < 0.001 or abs(info - 0.5) < 0.001;
quit;
```




<!DOCTYPE html>
<html lang="en" xml:lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta charset="utf-8"/>
<meta content="SAS 9.4" name="generator"/>
<title>SAS Output</title>
<style>
/*<![CDATA[*/
.body.c > table, .body.c > pre, .body.c div > table,
.body.c div > pre, .body.c > table, .body.c > pre,
.body.j > table, .body.j > pre, .body.j div > table,
.body.j div > pre, .body.j > table, .body.j > pre,
.body.c p.note, .body.c p.warning, .body.c p.error, .body.c p.fatal,
.body.j p.note, .body.j p.warning, .body.j p.error, .body.j p.fatal,
.body.c > table.layoutcontainer, .body.j > table.layoutcontainer { margin-left: auto; margin-right: auto }
.layoutregion.l table, .layoutregion.l pre, .layoutregion.l p.note,
.layoutregion.l p.warning, .layoutregion.l p.error, .layoutregion.l p.fatal { margin-left: 0 }
.layoutregion.c table, .layoutregion.c pre, .layoutregion.c p.note,
.layoutregion.c p.warning, .layoutregion.c p.error, .layoutregion.c p.fatal { margin-left: auto; margin-right: auto }
.layoutregion.r table, .layoutregion.r pre, .layoutregion.r p.note,
.layoutregion.r table, .layoutregion.r pre, .layoutregion.r p.note,
.layoutregion.r p.warning, .layoutregion.r p.error, .layoutregion.r p.fatal { margin-right: 0 }
article, aside, details, figcaption, figure, footer, header, hgroup, nav, section { display: block }
html{ font-size: 100% }
.body { margin: 1em; font-size: 13px; line-height: 1.231 }
sup { position: relative; vertical-align: baseline; bottom: 0.25em; font-size: 0.8em }
sub { position: relative; vertical-align: baseline; top: 0.25em; font-size: 0.8em }
ul, ol { margin: 1em 0; padding: 0 0 0 40px }
dd { margin: 0 0 0 40px }
nav ul, nav ol { list-style: none; list-style-image: none; margin: 0; padding: 0 }
img { border: 0; vertical-align: middle }
svg:not(:root) { overflow: hidden }
figure { margin: 0 }
table { border-collapse: collapse; border-spacing: 0 }
.layoutcontainer { border-collapse: separate; border-spacing: 0 }
p { margin-top: 0; text-align: left }
h1.heading1 { text-align: left }
h2.heading2 { text-align: left }
h3.heading3 { text-align: left }
h4.heading4 { text-align: left }
h5.heading5 { text-align: left }
h6.heading6 { text-align: left }
span { text-align: left }
table { margin-bottom: 1em }
td, th { text-align: left; padding: 3px 6px; vertical-align: top }
td[class$="fixed"], th[class$="fixed"] { white-space: pre }
section, article { padding-top: 1px; padding-bottom: 8px }
hr.pagebreak { height: 0px; border: 0; border-bottom: 1px solid #c0c0c0; margin: 1em 0 }
.stacked-value { text-align: left; display: block }
.stacked-cell > .stacked-value, td.data > td.data, th.data > td.data, th.data > th.data, td.data > th.data, th.header > th.header { border: 0 }
.stacked-cell > div.data { border-width: 0 }
.systitleandfootercontainer { white-space: nowrap; margin-bottom: 1em }
.systitleandfootercontainer > p { margin: 0 }
.systitleandfootercontainer > p > span { display: inline-block; width: 100%; white-space: normal }
.batch { display: table }
.toc { display: none }
.proc_note_group, .proc_title_group { margin-bottom: 1em }
p.proctitle { margin: 0 }
p.note, p.warning, p.error, p.fatal { display: table }
.notebanner, .warnbanner, .errorbanner, .fatalbanner,
.notecontent, .warncontent, .errorcontent, .fatalcontent { display: table-cell; padding: 0.5em }
.notebanner, .warnbanner, .errorbanner, .fatalbanner { padding-right: 0 }
.body > div > ol li { text-align: left }
.beforecaption > h4 { margin-top: 0; margin-bottom: 0 }
.c { text-align: center }
.r { text-align: right }
.l { text-align: left }
.j { text-align: justify }
.d { text-align: right }
.b { vertical-align: bottom }
.m { vertical-align: middle }
.t { vertical-align: top }
.accessiblecaption {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
a:active { color: #800080 }
.aftercaption {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
    padding-top: 4pt;
}
.batch > colgroup {
    border-left: 1px solid #c1c1c1;
    border-right: 1px solid #c1c1c1;
}
.batch > tbody, .batch > thead, .batch > tfoot {
    border-top: 1px solid #c1c1c1;
    border-bottom: 1px solid #c1c1c1;
}
.batch { border: hidden; }
.batch {
    background-color: #fafbfe;
    border: 1px solid #c1c1c1;
    border-collapse: separate;
    border-spacing: 1px;
    color: #000000;
    font-family: 'SAS Monospace', 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    padding: 7px;
    }
.beforecaption {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.body {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    margin-left: 8px;
    margin-right: 8px;
}
.bodydate {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    text-align: right;
    vertical-align: top;
    width: 100%;
}
.bycontentfolder {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.byline {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.bylinecontainer > col, .bylinecontainer > colgroup > col, .bylinecontainer > colgroup, .bylinecontainer > tr, .bylinecontainer > * > tr, .bylinecontainer > thead, .bylinecontainer > tbody, .bylinecontainer > tfoot { border: none; }
.bylinecontainer {
    background-color: #fafbfe;
    border: none;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.caption {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.cell, .container {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.contentfolder, .contentitem {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.contentproclabel, .contentprocname {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.contents {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: decimal;
    margin-left: 8px;
    margin-right: 8px;
}
.contentsdate {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.contenttitle {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: bold;
}
.continued {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
    width: 100%;
}
.data, .dataemphasis {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.dataemphasisfixed {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.dataempty {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.datafixed {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.datastrong {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.datastrongfixed {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.date {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.document {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.errorbanner {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.errorcontent {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.errorcontentfixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.extendedpage {
    background-color: #fafbfe;
    border-style: solid;
    border-width: 1pt;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
    text-align: center;
}
.fatalbanner {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.fatalcontent {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.fatalcontentfixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.folderaction {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.footer {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.footeremphasis {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.footeremphasisfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.footerempty {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.footerfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.footerstrong {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.footerstrongfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.frame {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.graph > colgroup {
    border-left: 1px solid #c1c1c1;
    border-right: 1px solid #c1c1c1;
}
.graph > tbody, .graph > thead, .graph > tfoot {
    border-top: 1px solid #c1c1c1;
    border-bottom: 1px solid #c1c1c1;
}
.graph { border: hidden; }
.graph {
    background-color: #fafbfe;
    border: 1px solid #c1c1c1;
    border-collapse: separate;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    }
.header {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.headeremphasis {
    background-color: #d8dbd3;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.headeremphasisfixed {
    background-color: #d8dbd3;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.headerempty {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.headerfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.headersandfooters {
    background-color: #edf2f9;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.headerstrong {
    background-color: #d8dbd3;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.headerstrongfixed {
    background-color: #d8dbd3;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.heading1, .heading2, .heading3, .heading4, .heading5, .heading6 { font-family: Arial, Helvetica, sans-serif }
.index {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.indexaction, .indexitem {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.indexprocname {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.indextitle {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: bold;
}
.layoutcontainer, .layoutregion {
    border-width: 0;
    border-spacing: 30px;
}
.linecontent {
    background-color: #fafbfe;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
a:link { color: #0000ff }
.list {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: disc;
}
.list10 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: square;
}
.list2 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: circle;
}
.list3, .list4, .list5, .list6, .list7, .list8, .list9 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: square;
}
.listitem {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: disc;
}
.listitem10 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: square;
}
.listitem2 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: circle;
}
.listitem3, .listitem4, .listitem5, .listitem6, .listitem7, .listitem8, .listitem9 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: square;
}
.note {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.notebanner {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.notecontent {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.notecontentfixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.output > colgroup {
    border-left: 1px solid #c1c1c1;
    border-right: 1px solid #c1c1c1;
}
.output > tbody, .output > thead, .output > tfoot {
    border-top: 1px solid #c1c1c1;
    border-bottom: 1px solid #c1c1c1;
}
.output { border: hidden; }
.output {
    background-color: #fafbfe;
    border: 1px solid #c1c1c1;
    border-collapse: separate;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    }
.pageno {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
    text-align: right;
    vertical-align: top;
}
.pages {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: decimal;
    margin-left: 8px;
    margin-right: 8px;
}
.pagesdate {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.pagesitem {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.pagesproclabel, .pagesprocname {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.pagestitle {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: bold;
}
.paragraph {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.parskip > col, .parskip > colgroup > col, .parskip > colgroup, .parskip > tr, .parskip > * > tr, .parskip > thead, .parskip > tbody, .parskip > tfoot { border: none; }
.parskip {
    border: none;
    border-spacing: 0;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
    }
.prepage {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    text-align: left;
}
.proctitle {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.proctitlefixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowfooter {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowfooteremphasis {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.rowfooteremphasisfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.rowfooterempty {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowfooterfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.rowfooterstrong {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowfooterstrongfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowheader {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowheaderemphasis {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.rowheaderemphasisfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.rowheaderempty {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowheaderfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.rowheaderstrong {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowheaderstrongfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.systemfooter, .systemfooter10, .systemfooter2, .systemfooter3, .systemfooter4, .systemfooter5, .systemfooter6, .systemfooter7, .systemfooter8, .systemfooter9 {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.systemtitle, .systemtitle10, .systemtitle2, .systemtitle3, .systemtitle4, .systemtitle5, .systemtitle6, .systemtitle7, .systemtitle8, .systemtitle9 {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size: small;
    font-style: normal;
    font-weight: bold;
}
.systitleandfootercontainer > col, .systitleandfootercontainer > colgroup > col, .systitleandfootercontainer > colgroup, .systitleandfootercontainer > tr, .systitleandfootercontainer > * > tr, .systitleandfootercontainer > thead, .systitleandfootercontainer > tbody, .systitleandfootercontainer > tfoot { border: none; }
.systitleandfootercontainer {
    background-color: #fafbfe;
    border: none;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.table > col, .table > colgroup > col {
    border-left: 1px solid #c1c1c1;
    border-right: 0 solid #c1c1c1;
}
.table > tr, .table > * > tr {
    border-top: 1px solid #c1c1c1;
    border-bottom: 0 solid #c1c1c1;
}
.table { border: hidden; }
.table {
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 1px 0 0 1px;
    border-collapse: collapse;
    border-spacing: 0;
    }
.titleandnotecontainer > col, .titleandnotecontainer > colgroup > col, .titleandnotecontainer > colgroup, .titleandnotecontainer > tr, .titleandnotecontainer > * > tr, .titleandnotecontainer > thead, .titleandnotecontainer > tbody, .titleandnotecontainer > tfoot { border: none; }
.titleandnotecontainer {
    background-color: #fafbfe;
    border: none;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.titlesandfooters {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.usertext {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
a:visited { color: #800080 }
.warnbanner {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.warncontent {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.warncontentfixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
/*]]>*/
</style>
</head>
<body class="l body">
<div style="padding-bottom: 8px; padding-top: 1px">
<div id="IDX" class="systitleandfootercontainer" style="border-spacing: 1px">
<p><span class="c systemtitle">Posterior probability that pi falls in interval (0.2,0.5) [Prior: Beta(1,1)]</span> </p>
</div>
<div style="padding-bottom: 8px; padding-top: 1px">
<table class="table" style="border-spacing: 0" aria-label="Query Results">
<caption aria-label="Query Results"></caption>
<colgroup><col/></colgroup>
<thead>
<tr>
<th class="r b header" scope="col"> &#160;</th>
</tr>
</thead>
<tbody>
<tr>
<td class="r data">0.72</td>
</tr>
</tbody>
</table>
</div>
</div>
<div style="padding-bottom: 8px; padding-top: 1px">
<hr class="pagebreak"/>
<div id="IDX1" class="systitleandfootercontainer" style="border-spacing: 1px">
<p><span class="c systemtitle">Posterior probability that pi falls in interval (0.2,0.5) [Prior: Beta(2.4,2)]</span> </p>
</div>
<div style="padding-bottom: 8px; padding-top: 1px">
<table class="table" style="border-spacing: 0" aria-label="Query Results">
<caption aria-label="Query Results"></caption>
<colgroup><col/></colgroup>
<thead>
<tr>
<th class="r b header" scope="col"> &#160;</th>
</tr>
</thead>
<tbody>
<tr>
<td class="r data">0.79</td>
</tr>
</tbody>
</table>
</div>
</div>
</body>
</html>




*Posterior probability intervals* or *posterior credible intervals* are the Bayesian equivalent to confidence intervals. We frequently summarize the posterior distribution using a central $\left( 1 - \alpha \right) \times 100$% interval, which is a range of values having $\frac{\alpha}{2} \times 100$% of the posterior probability above and below the endpoints.

Let's calculate the 95% posterior probability intervals on the posterior distributions above.


```sas
%let alpha = 0.025;
%let ci_low = %sysevalf(&alpha*100);
%let ci_high = %sysevalf((1-&alpha)*100);
%let ct = %sysevalf(&ci_high - &ci_low);

ods graphics off;
proc univariate data=ranked noprint;
   var diffuse;
   output out=pctl pctlpts=&ci_low. &ci_high. pctlpre=p;
run;

ods graphics on;
title "Diffuse prior &ct% posterior probability interval";
proc print data=pctl;
run;

ods graphics off;
proc univariate data=ranked2 noprint;
   var info;
   output out=pctl pctlpts=&ci_low. &ci_high. pctlpre=p;
run;

ods graphics on;
title "Informative prior &ct% posterior probability interval";
proc print data=pctl;
run;
```




<!DOCTYPE html>
<html lang="en" xml:lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta charset="utf-8"/>
<meta content="SAS 9.4" name="generator"/>
<title>SAS Output</title>
<style>
/*<![CDATA[*/
.body.c > table, .body.c > pre, .body.c div > table,
.body.c div > pre, .body.c > table, .body.c > pre,
.body.j > table, .body.j > pre, .body.j div > table,
.body.j div > pre, .body.j > table, .body.j > pre,
.body.c p.note, .body.c p.warning, .body.c p.error, .body.c p.fatal,
.body.j p.note, .body.j p.warning, .body.j p.error, .body.j p.fatal,
.body.c > table.layoutcontainer, .body.j > table.layoutcontainer { margin-left: auto; margin-right: auto }
.layoutregion.l table, .layoutregion.l pre, .layoutregion.l p.note,
.layoutregion.l p.warning, .layoutregion.l p.error, .layoutregion.l p.fatal { margin-left: 0 }
.layoutregion.c table, .layoutregion.c pre, .layoutregion.c p.note,
.layoutregion.c p.warning, .layoutregion.c p.error, .layoutregion.c p.fatal { margin-left: auto; margin-right: auto }
.layoutregion.r table, .layoutregion.r pre, .layoutregion.r p.note,
.layoutregion.r table, .layoutregion.r pre, .layoutregion.r p.note,
.layoutregion.r p.warning, .layoutregion.r p.error, .layoutregion.r p.fatal { margin-right: 0 }
article, aside, details, figcaption, figure, footer, header, hgroup, nav, section { display: block }
html{ font-size: 100% }
.body { margin: 1em; font-size: 13px; line-height: 1.231 }
sup { position: relative; vertical-align: baseline; bottom: 0.25em; font-size: 0.8em }
sub { position: relative; vertical-align: baseline; top: 0.25em; font-size: 0.8em }
ul, ol { margin: 1em 0; padding: 0 0 0 40px }
dd { margin: 0 0 0 40px }
nav ul, nav ol { list-style: none; list-style-image: none; margin: 0; padding: 0 }
img { border: 0; vertical-align: middle }
svg:not(:root) { overflow: hidden }
figure { margin: 0 }
table { border-collapse: collapse; border-spacing: 0 }
.layoutcontainer { border-collapse: separate; border-spacing: 0 }
p { margin-top: 0; text-align: left }
h1.heading1 { text-align: left }
h2.heading2 { text-align: left }
h3.heading3 { text-align: left }
h4.heading4 { text-align: left }
h5.heading5 { text-align: left }
h6.heading6 { text-align: left }
span { text-align: left }
table { margin-bottom: 1em }
td, th { text-align: left; padding: 3px 6px; vertical-align: top }
td[class$="fixed"], th[class$="fixed"] { white-space: pre }
section, article { padding-top: 1px; padding-bottom: 8px }
hr.pagebreak { height: 0px; border: 0; border-bottom: 1px solid #c0c0c0; margin: 1em 0 }
.stacked-value { text-align: left; display: block }
.stacked-cell > .stacked-value, td.data > td.data, th.data > td.data, th.data > th.data, td.data > th.data, th.header > th.header { border: 0 }
.stacked-cell > div.data { border-width: 0 }
.systitleandfootercontainer { white-space: nowrap; margin-bottom: 1em }
.systitleandfootercontainer > p { margin: 0 }
.systitleandfootercontainer > p > span { display: inline-block; width: 100%; white-space: normal }
.batch { display: table }
.toc { display: none }
.proc_note_group, .proc_title_group { margin-bottom: 1em }
p.proctitle { margin: 0 }
p.note, p.warning, p.error, p.fatal { display: table }
.notebanner, .warnbanner, .errorbanner, .fatalbanner,
.notecontent, .warncontent, .errorcontent, .fatalcontent { display: table-cell; padding: 0.5em }
.notebanner, .warnbanner, .errorbanner, .fatalbanner { padding-right: 0 }
.body > div > ol li { text-align: left }
.beforecaption > h4 { margin-top: 0; margin-bottom: 0 }
.c { text-align: center }
.r { text-align: right }
.l { text-align: left }
.j { text-align: justify }
.d { text-align: right }
.b { vertical-align: bottom }
.m { vertical-align: middle }
.t { vertical-align: top }
.accessiblecaption {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
a:active { color: #800080 }
.aftercaption {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
    padding-top: 4pt;
}
.batch > colgroup {
    border-left: 1px solid #c1c1c1;
    border-right: 1px solid #c1c1c1;
}
.batch > tbody, .batch > thead, .batch > tfoot {
    border-top: 1px solid #c1c1c1;
    border-bottom: 1px solid #c1c1c1;
}
.batch { border: hidden; }
.batch {
    background-color: #fafbfe;
    border: 1px solid #c1c1c1;
    border-collapse: separate;
    border-spacing: 1px;
    color: #000000;
    font-family: 'SAS Monospace', 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    padding: 7px;
    }
.beforecaption {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.body {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    margin-left: 8px;
    margin-right: 8px;
}
.bodydate {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    text-align: right;
    vertical-align: top;
    width: 100%;
}
.bycontentfolder {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.byline {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.bylinecontainer > col, .bylinecontainer > colgroup > col, .bylinecontainer > colgroup, .bylinecontainer > tr, .bylinecontainer > * > tr, .bylinecontainer > thead, .bylinecontainer > tbody, .bylinecontainer > tfoot { border: none; }
.bylinecontainer {
    background-color: #fafbfe;
    border: none;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.caption {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.cell, .container {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.contentfolder, .contentitem {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.contentproclabel, .contentprocname {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.contents {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: decimal;
    margin-left: 8px;
    margin-right: 8px;
}
.contentsdate {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.contenttitle {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: bold;
}
.continued {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
    width: 100%;
}
.data, .dataemphasis {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.dataemphasisfixed {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.dataempty {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.datafixed {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.datastrong {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.datastrongfixed {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.date {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.document {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.errorbanner {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.errorcontent {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.errorcontentfixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.extendedpage {
    background-color: #fafbfe;
    border-style: solid;
    border-width: 1pt;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
    text-align: center;
}
.fatalbanner {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.fatalcontent {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.fatalcontentfixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.folderaction {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.footer {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.footeremphasis {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.footeremphasisfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.footerempty {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.footerfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.footerstrong {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.footerstrongfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.frame {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.graph > colgroup {
    border-left: 1px solid #c1c1c1;
    border-right: 1px solid #c1c1c1;
}
.graph > tbody, .graph > thead, .graph > tfoot {
    border-top: 1px solid #c1c1c1;
    border-bottom: 1px solid #c1c1c1;
}
.graph { border: hidden; }
.graph {
    background-color: #fafbfe;
    border: 1px solid #c1c1c1;
    border-collapse: separate;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    }
.header {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.headeremphasis {
    background-color: #d8dbd3;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.headeremphasisfixed {
    background-color: #d8dbd3;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.headerempty {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.headerfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.headersandfooters {
    background-color: #edf2f9;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.headerstrong {
    background-color: #d8dbd3;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.headerstrongfixed {
    background-color: #d8dbd3;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.heading1, .heading2, .heading3, .heading4, .heading5, .heading6 { font-family: Arial, Helvetica, sans-serif }
.index {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.indexaction, .indexitem {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.indexprocname {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.indextitle {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: bold;
}
.layoutcontainer, .layoutregion {
    border-width: 0;
    border-spacing: 30px;
}
.linecontent {
    background-color: #fafbfe;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
a:link { color: #0000ff }
.list {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: disc;
}
.list10 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: square;
}
.list2 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: circle;
}
.list3, .list4, .list5, .list6, .list7, .list8, .list9 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: square;
}
.listitem {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: disc;
}
.listitem10 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: square;
}
.listitem2 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: circle;
}
.listitem3, .listitem4, .listitem5, .listitem6, .listitem7, .listitem8, .listitem9 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: square;
}
.note {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.notebanner {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.notecontent {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.notecontentfixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.output > colgroup {
    border-left: 1px solid #c1c1c1;
    border-right: 1px solid #c1c1c1;
}
.output > tbody, .output > thead, .output > tfoot {
    border-top: 1px solid #c1c1c1;
    border-bottom: 1px solid #c1c1c1;
}
.output { border: hidden; }
.output {
    background-color: #fafbfe;
    border: 1px solid #c1c1c1;
    border-collapse: separate;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    }
.pageno {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
    text-align: right;
    vertical-align: top;
}
.pages {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: decimal;
    margin-left: 8px;
    margin-right: 8px;
}
.pagesdate {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.pagesitem {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.pagesproclabel, .pagesprocname {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.pagestitle {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: bold;
}
.paragraph {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.parskip > col, .parskip > colgroup > col, .parskip > colgroup, .parskip > tr, .parskip > * > tr, .parskip > thead, .parskip > tbody, .parskip > tfoot { border: none; }
.parskip {
    border: none;
    border-spacing: 0;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
    }
.prepage {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    text-align: left;
}
.proctitle {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.proctitlefixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowfooter {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowfooteremphasis {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.rowfooteremphasisfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.rowfooterempty {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowfooterfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.rowfooterstrong {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowfooterstrongfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowheader {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowheaderemphasis {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.rowheaderemphasisfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.rowheaderempty {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowheaderfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.rowheaderstrong {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowheaderstrongfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.systemfooter, .systemfooter10, .systemfooter2, .systemfooter3, .systemfooter4, .systemfooter5, .systemfooter6, .systemfooter7, .systemfooter8, .systemfooter9 {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.systemtitle, .systemtitle10, .systemtitle2, .systemtitle3, .systemtitle4, .systemtitle5, .systemtitle6, .systemtitle7, .systemtitle8, .systemtitle9 {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size: small;
    font-style: normal;
    font-weight: bold;
}
.systitleandfootercontainer > col, .systitleandfootercontainer > colgroup > col, .systitleandfootercontainer > colgroup, .systitleandfootercontainer > tr, .systitleandfootercontainer > * > tr, .systitleandfootercontainer > thead, .systitleandfootercontainer > tbody, .systitleandfootercontainer > tfoot { border: none; }
.systitleandfootercontainer {
    background-color: #fafbfe;
    border: none;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.table > col, .table > colgroup > col {
    border-left: 1px solid #c1c1c1;
    border-right: 0 solid #c1c1c1;
}
.table > tr, .table > * > tr {
    border-top: 1px solid #c1c1c1;
    border-bottom: 0 solid #c1c1c1;
}
.table { border: hidden; }
.table {
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 1px 0 0 1px;
    border-collapse: collapse;
    border-spacing: 0;
    }
.titleandnotecontainer > col, .titleandnotecontainer > colgroup > col, .titleandnotecontainer > colgroup, .titleandnotecontainer > tr, .titleandnotecontainer > * > tr, .titleandnotecontainer > thead, .titleandnotecontainer > tbody, .titleandnotecontainer > tfoot { border: none; }
.titleandnotecontainer {
    background-color: #fafbfe;
    border: none;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.titlesandfooters {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.usertext {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
a:visited { color: #800080 }
.warnbanner {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.warncontent {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.warncontentfixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
/*]]>*/
</style>
</head>
<body class="l body">
<div style="padding-bottom: 8px; padding-top: 1px">
<div id="IDX" class="systitleandfootercontainer" style="border-spacing: 1px">
<p><span class="c systemtitle">Diffuse prior 95% posterior probability interval</span> </p>
</div>
<div style="padding-bottom: 8px; padding-top: 1px">
<table class="table" style="border-spacing: 0" aria-label="Data Set WORK.PCTL">
<caption aria-label="Data Set WORK.PCTL"></caption>
<colgroup><col/></colgroup><colgroup><col/><col/></colgroup>
<thead>
<tr>
<th class="r header" scope="col">Obs</th>
<th class="r header" scope="col">p2_5</th>
<th class="r header" scope="col">p97_5</th>
</tr>
</thead>
<tbody>
<tr>
<th class="r rowheader" scope="row">1</th>
<td class="r data">0.096976</td>
<td class="r data">0.57557</td>
</tr>
</tbody>
</table>
</div>
</div>
<div style="padding-bottom: 8px; padding-top: 1px">
<hr class="pagebreak"/>
<div id="IDX1" class="systitleandfootercontainer" style="border-spacing: 1px">
<p><span class="c systemtitle">Informative prior 95% posterior probability interval</span> </p>
</div>
<div style="padding-bottom: 8px; padding-top: 1px">
<table class="table" style="border-spacing: 0" aria-label="Data Set WORK.PCTL">
<caption aria-label="Data Set WORK.PCTL"></caption>
<colgroup><col/></colgroup><colgroup><col/><col/></colgroup>
<thead>
<tr>
<th class="r header" scope="col">Obs</th>
<th class="r header" scope="col">p2_5</th>
<th class="r header" scope="col">p97_5</th>
</tr>
</thead>
<tbody>
<tr>
<th class="r rowheader" scope="row">1</th>
<td class="r data">0.13838</td>
<td class="r data">0.59868</td>
</tr>
</tbody>
</table>
</div>
</div>
</body>
</html>




There are three Bayesian analogues of the MLE:
* Maximum a posteriori (MAP)
    * MAP is the point on the x axis having the highest posterior density on the y axis
    
* Posterior mean
    * First moment of the posterior distribution

Posterior mean of the binomial success probability:

$$
E \left( \pi \, | \, y \right) = \int^{1}_{0} \pi p \left( \pi \, | \, y \right) d\pi
$$

* Posterior median

$$
\int^{\tilde{\pi}}_{0} p \left( \pi \, | \, y \right) d\pi = 0.5
$$

Let's calculate these now.


```sas
ods graphics off;
proc univariate data=ranked noprint round=0.001;
    var diffuse;
    output out=sdescr mode=mode mean=mean median=p50;
run;

ods graphics on;
Title "Posterior probability MAP, mean, median [Prior: Beta(1,1)]";
proc print data=sdescr;
run;

ods graphics off;
proc univariate data=ranked2 noprint round=0.001;
    var info;
    output out=sdescr mode=mode mean=mean median=p50;
run;

ods graphics on;
Title "Posterior probability MAP, mean, median [Prior: Beta(2.4,2)]";
proc print data=sdescr;
run;
```




<!DOCTYPE html>
<html lang="en" xml:lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta charset="utf-8"/>
<meta content="SAS 9.4" name="generator"/>
<title>SAS Output</title>
<style>
/*<![CDATA[*/
.body.c > table, .body.c > pre, .body.c div > table,
.body.c div > pre, .body.c > table, .body.c > pre,
.body.j > table, .body.j > pre, .body.j div > table,
.body.j div > pre, .body.j > table, .body.j > pre,
.body.c p.note, .body.c p.warning, .body.c p.error, .body.c p.fatal,
.body.j p.note, .body.j p.warning, .body.j p.error, .body.j p.fatal,
.body.c > table.layoutcontainer, .body.j > table.layoutcontainer { margin-left: auto; margin-right: auto }
.layoutregion.l table, .layoutregion.l pre, .layoutregion.l p.note,
.layoutregion.l p.warning, .layoutregion.l p.error, .layoutregion.l p.fatal { margin-left: 0 }
.layoutregion.c table, .layoutregion.c pre, .layoutregion.c p.note,
.layoutregion.c p.warning, .layoutregion.c p.error, .layoutregion.c p.fatal { margin-left: auto; margin-right: auto }
.layoutregion.r table, .layoutregion.r pre, .layoutregion.r p.note,
.layoutregion.r table, .layoutregion.r pre, .layoutregion.r p.note,
.layoutregion.r p.warning, .layoutregion.r p.error, .layoutregion.r p.fatal { margin-right: 0 }
article, aside, details, figcaption, figure, footer, header, hgroup, nav, section { display: block }
html{ font-size: 100% }
.body { margin: 1em; font-size: 13px; line-height: 1.231 }
sup { position: relative; vertical-align: baseline; bottom: 0.25em; font-size: 0.8em }
sub { position: relative; vertical-align: baseline; top: 0.25em; font-size: 0.8em }
ul, ol { margin: 1em 0; padding: 0 0 0 40px }
dd { margin: 0 0 0 40px }
nav ul, nav ol { list-style: none; list-style-image: none; margin: 0; padding: 0 }
img { border: 0; vertical-align: middle }
svg:not(:root) { overflow: hidden }
figure { margin: 0 }
table { border-collapse: collapse; border-spacing: 0 }
.layoutcontainer { border-collapse: separate; border-spacing: 0 }
p { margin-top: 0; text-align: left }
h1.heading1 { text-align: left }
h2.heading2 { text-align: left }
h3.heading3 { text-align: left }
h4.heading4 { text-align: left }
h5.heading5 { text-align: left }
h6.heading6 { text-align: left }
span { text-align: left }
table { margin-bottom: 1em }
td, th { text-align: left; padding: 3px 6px; vertical-align: top }
td[class$="fixed"], th[class$="fixed"] { white-space: pre }
section, article { padding-top: 1px; padding-bottom: 8px }
hr.pagebreak { height: 0px; border: 0; border-bottom: 1px solid #c0c0c0; margin: 1em 0 }
.stacked-value { text-align: left; display: block }
.stacked-cell > .stacked-value, td.data > td.data, th.data > td.data, th.data > th.data, td.data > th.data, th.header > th.header { border: 0 }
.stacked-cell > div.data { border-width: 0 }
.systitleandfootercontainer { white-space: nowrap; margin-bottom: 1em }
.systitleandfootercontainer > p { margin: 0 }
.systitleandfootercontainer > p > span { display: inline-block; width: 100%; white-space: normal }
.batch { display: table }
.toc { display: none }
.proc_note_group, .proc_title_group { margin-bottom: 1em }
p.proctitle { margin: 0 }
p.note, p.warning, p.error, p.fatal { display: table }
.notebanner, .warnbanner, .errorbanner, .fatalbanner,
.notecontent, .warncontent, .errorcontent, .fatalcontent { display: table-cell; padding: 0.5em }
.notebanner, .warnbanner, .errorbanner, .fatalbanner { padding-right: 0 }
.body > div > ol li { text-align: left }
.beforecaption > h4 { margin-top: 0; margin-bottom: 0 }
.c { text-align: center }
.r { text-align: right }
.l { text-align: left }
.j { text-align: justify }
.d { text-align: right }
.b { vertical-align: bottom }
.m { vertical-align: middle }
.t { vertical-align: top }
.accessiblecaption {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
a:active { color: #800080 }
.aftercaption {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
    padding-top: 4pt;
}
.batch > colgroup {
    border-left: 1px solid #c1c1c1;
    border-right: 1px solid #c1c1c1;
}
.batch > tbody, .batch > thead, .batch > tfoot {
    border-top: 1px solid #c1c1c1;
    border-bottom: 1px solid #c1c1c1;
}
.batch { border: hidden; }
.batch {
    background-color: #fafbfe;
    border: 1px solid #c1c1c1;
    border-collapse: separate;
    border-spacing: 1px;
    color: #000000;
    font-family: 'SAS Monospace', 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    padding: 7px;
    }
.beforecaption {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.body {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    margin-left: 8px;
    margin-right: 8px;
}
.bodydate {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    text-align: right;
    vertical-align: top;
    width: 100%;
}
.bycontentfolder {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.byline {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.bylinecontainer > col, .bylinecontainer > colgroup > col, .bylinecontainer > colgroup, .bylinecontainer > tr, .bylinecontainer > * > tr, .bylinecontainer > thead, .bylinecontainer > tbody, .bylinecontainer > tfoot { border: none; }
.bylinecontainer {
    background-color: #fafbfe;
    border: none;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.caption {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.cell, .container {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.contentfolder, .contentitem {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.contentproclabel, .contentprocname {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.contents {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: decimal;
    margin-left: 8px;
    margin-right: 8px;
}
.contentsdate {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.contenttitle {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: bold;
}
.continued {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
    width: 100%;
}
.data, .dataemphasis {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.dataemphasisfixed {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.dataempty {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.datafixed {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.datastrong {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.datastrongfixed {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.date {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.document {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.errorbanner {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.errorcontent {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.errorcontentfixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.extendedpage {
    background-color: #fafbfe;
    border-style: solid;
    border-width: 1pt;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
    text-align: center;
}
.fatalbanner {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.fatalcontent {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.fatalcontentfixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.folderaction {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.footer {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.footeremphasis {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.footeremphasisfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.footerempty {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.footerfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.footerstrong {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.footerstrongfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.frame {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.graph > colgroup {
    border-left: 1px solid #c1c1c1;
    border-right: 1px solid #c1c1c1;
}
.graph > tbody, .graph > thead, .graph > tfoot {
    border-top: 1px solid #c1c1c1;
    border-bottom: 1px solid #c1c1c1;
}
.graph { border: hidden; }
.graph {
    background-color: #fafbfe;
    border: 1px solid #c1c1c1;
    border-collapse: separate;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    }
.header {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.headeremphasis {
    background-color: #d8dbd3;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.headeremphasisfixed {
    background-color: #d8dbd3;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.headerempty {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.headerfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.headersandfooters {
    background-color: #edf2f9;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.headerstrong {
    background-color: #d8dbd3;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.headerstrongfixed {
    background-color: #d8dbd3;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.heading1, .heading2, .heading3, .heading4, .heading5, .heading6 { font-family: Arial, Helvetica, sans-serif }
.index {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.indexaction, .indexitem {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.indexprocname {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.indextitle {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: bold;
}
.layoutcontainer, .layoutregion {
    border-width: 0;
    border-spacing: 30px;
}
.linecontent {
    background-color: #fafbfe;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
a:link { color: #0000ff }
.list {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: disc;
}
.list10 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: square;
}
.list2 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: circle;
}
.list3, .list4, .list5, .list6, .list7, .list8, .list9 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: square;
}
.listitem {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: disc;
}
.listitem10 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: square;
}
.listitem2 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: circle;
}
.listitem3, .listitem4, .listitem5, .listitem6, .listitem7, .listitem8, .listitem9 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: square;
}
.note {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.notebanner {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.notecontent {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.notecontentfixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.output > colgroup {
    border-left: 1px solid #c1c1c1;
    border-right: 1px solid #c1c1c1;
}
.output > tbody, .output > thead, .output > tfoot {
    border-top: 1px solid #c1c1c1;
    border-bottom: 1px solid #c1c1c1;
}
.output { border: hidden; }
.output {
    background-color: #fafbfe;
    border: 1px solid #c1c1c1;
    border-collapse: separate;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    }
.pageno {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
    text-align: right;
    vertical-align: top;
}
.pages {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: decimal;
    margin-left: 8px;
    margin-right: 8px;
}
.pagesdate {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.pagesitem {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.pagesproclabel, .pagesprocname {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.pagestitle {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: bold;
}
.paragraph {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.parskip > col, .parskip > colgroup > col, .parskip > colgroup, .parskip > tr, .parskip > * > tr, .parskip > thead, .parskip > tbody, .parskip > tfoot { border: none; }
.parskip {
    border: none;
    border-spacing: 0;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
    }
.prepage {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    text-align: left;
}
.proctitle {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.proctitlefixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowfooter {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowfooteremphasis {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.rowfooteremphasisfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.rowfooterempty {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowfooterfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.rowfooterstrong {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowfooterstrongfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowheader {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowheaderemphasis {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.rowheaderemphasisfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.rowheaderempty {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowheaderfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.rowheaderstrong {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowheaderstrongfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.systemfooter, .systemfooter10, .systemfooter2, .systemfooter3, .systemfooter4, .systemfooter5, .systemfooter6, .systemfooter7, .systemfooter8, .systemfooter9 {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.systemtitle, .systemtitle10, .systemtitle2, .systemtitle3, .systemtitle4, .systemtitle5, .systemtitle6, .systemtitle7, .systemtitle8, .systemtitle9 {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size: small;
    font-style: normal;
    font-weight: bold;
}
.systitleandfootercontainer > col, .systitleandfootercontainer > colgroup > col, .systitleandfootercontainer > colgroup, .systitleandfootercontainer > tr, .systitleandfootercontainer > * > tr, .systitleandfootercontainer > thead, .systitleandfootercontainer > tbody, .systitleandfootercontainer > tfoot { border: none; }
.systitleandfootercontainer {
    background-color: #fafbfe;
    border: none;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.table > col, .table > colgroup > col {
    border-left: 1px solid #c1c1c1;
    border-right: 0 solid #c1c1c1;
}
.table > tr, .table > * > tr {
    border-top: 1px solid #c1c1c1;
    border-bottom: 0 solid #c1c1c1;
}
.table { border: hidden; }
.table {
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 1px 0 0 1px;
    border-collapse: collapse;
    border-spacing: 0;
    }
.titleandnotecontainer > col, .titleandnotecontainer > colgroup > col, .titleandnotecontainer > colgroup, .titleandnotecontainer > tr, .titleandnotecontainer > * > tr, .titleandnotecontainer > thead, .titleandnotecontainer > tbody, .titleandnotecontainer > tfoot { border: none; }
.titleandnotecontainer {
    background-color: #fafbfe;
    border: none;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.titlesandfooters {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.usertext {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
a:visited { color: #800080 }
.warnbanner {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.warncontent {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.warncontentfixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
/*]]>*/
</style>
</head>
<body class="l body">
<div style="padding-bottom: 8px; padding-top: 1px">
<div id="IDX" class="systitleandfootercontainer" style="border-spacing: 1px">
<p><span class="c systemtitle">Posterior probability MAP, mean, median [Prior: Beta(1,1)]</span> </p>
</div>
<div style="padding-bottom: 8px; padding-top: 1px">
<table class="table" style="border-spacing: 0" aria-label="Data Set WORK.SDESCR">
<caption aria-label="Data Set WORK.SDESCR"></caption>
<colgroup><col/></colgroup><colgroup><col/><col/><col/></colgroup>
<thead>
<tr>
<th class="r header" scope="col">Obs</th>
<th class="r header" scope="col">mean</th>
<th class="r header" scope="col">p50</th>
<th class="r header" scope="col">mode</th>
</tr>
</thead>
<tbody>
<tr>
<th class="r rowheader" scope="row">1</th>
<td class="r data">0.30799</td>
<td class="r data">0.297</td>
<td class="r data">0.231</td>
</tr>
</tbody>
</table>
</div>
</div>
<div style="padding-bottom: 8px; padding-top: 1px">
<hr class="pagebreak"/>
<div id="IDX1" class="systitleandfootercontainer" style="border-spacing: 1px">
<p><span class="c systemtitle">Posterior probability MAP, mean, median [Prior: Beta(2.4,2)]</span> </p>
</div>
<div style="padding-bottom: 8px; padding-top: 1px">
<table class="table" style="border-spacing: 0" aria-label="Data Set WORK.SDESCR">
<caption aria-label="Data Set WORK.SDESCR"></caption>
<colgroup><col/></colgroup><colgroup><col/><col/><col/></colgroup>
<thead>
<tr>
<th class="r header" scope="col">Obs</th>
<th class="r header" scope="col">mean</th>
<th class="r header" scope="col">p50</th>
<th class="r header" scope="col">mode</th>
</tr>
</thead>
<tbody>
<tr>
<th class="r rowheader" scope="row">1</th>
<td class="r data">0.35080</td>
<td class="r data">0.344</td>
<td class="r data">0.276</td>
</tr>
</tbody>
</table>
</div>
</div>
</body>
</html>




One way to understand the combination of information from the prior distribution and the data is through the notion of shrinkage. Recall that a beta distribution with parameters $\alpha$ and $\beta$ has mean = $\frac{\alpha}{\alpha + \beta}$.

Based on $\textit{y}$ successes and $\textit{n-y}$ failures, the posterior mean becomes:

$$
E \left( \pi \, | \, y \right) = \frac{\alpha + y}{\alpha + \beta + n}
$$

which we can reexpress as:

$$
E \left( \pi \, | \, y \right) = w\frac{\alpha}{\alpha + \beta} + (1-w)\frac{y}{n}
$$

where $\frac{\alpha}{\alpha + \beta}$ is the prior mean for the proportion of successes.<br>
$\frac{y}{n}$ is the proportion of successes in the sample.<br>
And...
$
w = \frac{\alpha + \beta}{\alpha + \beta + n}
$
is a fraction between 0 and 1.

Our posterior mean can be thought of as a $\textit{shrinkage estimate}$ because it moves the observed proportion of successes $\frac{y}{n}$ toward the prior mean $\frac{\alpha}{\alpha + \beta}$.
* The degree of shrinkage is controlled by $w$
    * The value of $w$ depends on the relative size of $(\alpha + \beta)$ to the sample size $n$
    * $\alpha + \beta$ can be thought of as a $\textit{prior sample size}$ or the number of observations afforded to the prior distribution in determining the posterior mean
    * Notice that as $n$ gets bigger, the weight given to the prior mean decreases to 0 - that is the prior mean loses its impact on the posterior mean as more and more samples $n$ are collected
    
## 2.3 Predictions

Now let's turn our attention to predict values of a future sample! FAA must predict the number of new launches that will succeed in say $m$ future launches scheduled.

Probability of observing $m-z$ failures in $m$ future launches of new vehicles would be equal to the probability of observing $z$ successes:

$$
f\left( z \, | \, \pi \right) = \binom{m}{z} \pi^{z} (1-\pi)^{m-z}
$$

In practice we do not know the value of $\pi$, we only have it's posterior distribution. In this case, the $\textit{predictive probability}$ of $z$ (for a future sample size of $m$), given a posterior distribution on $\pi$ based on past data $y$, is given by the integral

$$
p \left( z \, | \, y \right) = \int^{1}_{0} f\left( z \, | \, \pi \right) p\left( \pi \, | \, y \right)d\pi, \: \: \: \: \: \: \: \: z=0,\ldots,m \: \: \: \: \: \: \: \: \: \: \: \: \: \: \: \: \: \: \: \: \: \: \: \: (2.9)
$$

By integrating the sampling distribution $f\left( z \, | \, \pi \right)$ over the posterior distribution on the parameter $\pi$, we average over the uncertainty in this parameter. The predictive distribution provides a full account for the uncertainty in the unknown parameter $\pi$.

We can generalize Equation 2.9:

$$
p \left( \textbf{z} \, | \, \textbf{y} \right) = \int_{\Theta} f \left( \textbf{z} \, | \, \theta \right) p \left( \theta \, | \, \textbf{y} \right)d\theta
$$

We use MCMC methods to do this integration.

***Example 2.3: Calculating the predictive distribution for the number of successes of a new launch vehicle***

Assume we used a diffuse prior in Example 2.2.<br>
In this case, we found that the posterior distribution is equal to `Beta(4,9)`.<br>
Now suppose we want to calculate the probabilities of success associated with 5 additional launches of new vehicles, given this posterior distribution.


```sas
%let a_prior_diffuse = 1;
%let b_prior_diffuse = 1;


proc mcmc data=tbl outpost=ex2_3 seed=23 nmc=10000 maxtune=0 statistics=none diagnostics=none monitor=(xpred p0-p5) plots=none;
    ods exclude nobs parameters;
    parm diffuse;
    beginprior;
        xpred = rand("binomial", diffuse, 5);
        p0 = (xpred le 0);
        p1 = (xpred le 1);
        p2 = (xpred le 2);
        p3 = (xpred le 3);
        p4 = (xpred le 4);
        p5 = (xpred le 5);
    endprior;
    prior diffuse ~ beta(&a_prior_diffuse., &b_prior_diffuse.);
    model y ~ binomial(n,diffuse);
run;

proc univariate data=ex2_3 outtable=ex2_3_means noprint;
    var p0 p1 p2 p3 p4 p5;
run;            /* omit VAR statement to analyze all numerical variables */

data ex2_3_means2(keep=n probability_of_success _mean_ rename=(_mean_=cumulative));
    set ex2_3_means(keep=_var_ _mean_);
    m = lag(_mean_);
    n = _n_ - 1;
    if _n_ = 1 then probability_of_success = _mean_;
    else
        probability_of_success = _mean_ - m;
        drop m;
run;

Title "Probability of n number of successful launches given diffuse prior";
proc print data=ex2_3_means2; run;

proc sgplot data=ex2_3_means2;
series x=n y=cumulative;
title "Cumulative Distribution Function vs. n Number of Successful Launches";
yaxis label='Probability' min=0;
xaxis label='Number of Successes';
run;
```




<!DOCTYPE html>
<html lang="en" xml:lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta charset="utf-8"/>
<meta content="SAS 9.4" name="generator"/>
<title>SAS Output</title>
<style>
/*<![CDATA[*/
.body.c > table, .body.c > pre, .body.c div > table,
.body.c div > pre, .body.c > table, .body.c > pre,
.body.j > table, .body.j > pre, .body.j div > table,
.body.j div > pre, .body.j > table, .body.j > pre,
.body.c p.note, .body.c p.warning, .body.c p.error, .body.c p.fatal,
.body.j p.note, .body.j p.warning, .body.j p.error, .body.j p.fatal,
.body.c > table.layoutcontainer, .body.j > table.layoutcontainer { margin-left: auto; margin-right: auto }
.layoutregion.l table, .layoutregion.l pre, .layoutregion.l p.note,
.layoutregion.l p.warning, .layoutregion.l p.error, .layoutregion.l p.fatal { margin-left: 0 }
.layoutregion.c table, .layoutregion.c pre, .layoutregion.c p.note,
.layoutregion.c p.warning, .layoutregion.c p.error, .layoutregion.c p.fatal { margin-left: auto; margin-right: auto }
.layoutregion.r table, .layoutregion.r pre, .layoutregion.r p.note,
.layoutregion.r table, .layoutregion.r pre, .layoutregion.r p.note,
.layoutregion.r p.warning, .layoutregion.r p.error, .layoutregion.r p.fatal { margin-right: 0 }
article, aside, details, figcaption, figure, footer, header, hgroup, nav, section { display: block }
html{ font-size: 100% }
.body { margin: 1em; font-size: 13px; line-height: 1.231 }
sup { position: relative; vertical-align: baseline; bottom: 0.25em; font-size: 0.8em }
sub { position: relative; vertical-align: baseline; top: 0.25em; font-size: 0.8em }
ul, ol { margin: 1em 0; padding: 0 0 0 40px }
dd { margin: 0 0 0 40px }
nav ul, nav ol { list-style: none; list-style-image: none; margin: 0; padding: 0 }
img { border: 0; vertical-align: middle }
svg:not(:root) { overflow: hidden }
figure { margin: 0 }
table { border-collapse: collapse; border-spacing: 0 }
.layoutcontainer { border-collapse: separate; border-spacing: 0 }
p { margin-top: 0; text-align: left }
h1.heading1 { text-align: left }
h2.heading2 { text-align: left }
h3.heading3 { text-align: left }
h4.heading4 { text-align: left }
h5.heading5 { text-align: left }
h6.heading6 { text-align: left }
span { text-align: left }
table { margin-bottom: 1em }
td, th { text-align: left; padding: 3px 6px; vertical-align: top }
td[class$="fixed"], th[class$="fixed"] { white-space: pre }
section, article { padding-top: 1px; padding-bottom: 8px }
hr.pagebreak { height: 0px; border: 0; border-bottom: 1px solid #c0c0c0; margin: 1em 0 }
.stacked-value { text-align: left; display: block }
.stacked-cell > .stacked-value, td.data > td.data, th.data > td.data, th.data > th.data, td.data > th.data, th.header > th.header { border: 0 }
.stacked-cell > div.data { border-width: 0 }
.systitleandfootercontainer { white-space: nowrap; margin-bottom: 1em }
.systitleandfootercontainer > p { margin: 0 }
.systitleandfootercontainer > p > span { display: inline-block; width: 100%; white-space: normal }
.batch { display: table }
.toc { display: none }
.proc_note_group, .proc_title_group { margin-bottom: 1em }
p.proctitle { margin: 0 }
p.note, p.warning, p.error, p.fatal { display: table }
.notebanner, .warnbanner, .errorbanner, .fatalbanner,
.notecontent, .warncontent, .errorcontent, .fatalcontent { display: table-cell; padding: 0.5em }
.notebanner, .warnbanner, .errorbanner, .fatalbanner { padding-right: 0 }
.body > div > ol li { text-align: left }
.beforecaption > h4 { margin-top: 0; margin-bottom: 0 }
.c { text-align: center }
.r { text-align: right }
.l { text-align: left }
.j { text-align: justify }
.d { text-align: right }
.b { vertical-align: bottom }
.m { vertical-align: middle }
.t { vertical-align: top }
.accessiblecaption {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
a:active { color: #800080 }
.aftercaption {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
    padding-top: 4pt;
}
.batch > colgroup {
    border-left: 1px solid #c1c1c1;
    border-right: 1px solid #c1c1c1;
}
.batch > tbody, .batch > thead, .batch > tfoot {
    border-top: 1px solid #c1c1c1;
    border-bottom: 1px solid #c1c1c1;
}
.batch { border: hidden; }
.batch {
    background-color: #fafbfe;
    border: 1px solid #c1c1c1;
    border-collapse: separate;
    border-spacing: 1px;
    color: #000000;
    font-family: 'SAS Monospace', 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    padding: 7px;
    }
.beforecaption {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.body {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    margin-left: 8px;
    margin-right: 8px;
}
.bodydate {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    text-align: right;
    vertical-align: top;
    width: 100%;
}
.bycontentfolder {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.byline {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.bylinecontainer > col, .bylinecontainer > colgroup > col, .bylinecontainer > colgroup, .bylinecontainer > tr, .bylinecontainer > * > tr, .bylinecontainer > thead, .bylinecontainer > tbody, .bylinecontainer > tfoot { border: none; }
.bylinecontainer {
    background-color: #fafbfe;
    border: none;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.caption {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.cell, .container {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.contentfolder, .contentitem {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.contentproclabel, .contentprocname {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.contents {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: decimal;
    margin-left: 8px;
    margin-right: 8px;
}
.contentsdate {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.contenttitle {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: bold;
}
.continued {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
    width: 100%;
}
.data, .dataemphasis {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.dataemphasisfixed {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.dataempty {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.datafixed {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.datastrong {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.datastrongfixed {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.date {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.document {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.errorbanner {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.errorcontent {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.errorcontentfixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.extendedpage {
    background-color: #fafbfe;
    border-style: solid;
    border-width: 1pt;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
    text-align: center;
}
.fatalbanner {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.fatalcontent {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.fatalcontentfixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.folderaction {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.footer {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.footeremphasis {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.footeremphasisfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.footerempty {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.footerfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.footerstrong {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.footerstrongfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.frame {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.graph > colgroup {
    border-left: 1px solid #c1c1c1;
    border-right: 1px solid #c1c1c1;
}
.graph > tbody, .graph > thead, .graph > tfoot {
    border-top: 1px solid #c1c1c1;
    border-bottom: 1px solid #c1c1c1;
}
.graph { border: hidden; }
.graph {
    background-color: #fafbfe;
    border: 1px solid #c1c1c1;
    border-collapse: separate;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    }
.header {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.headeremphasis {
    background-color: #d8dbd3;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.headeremphasisfixed {
    background-color: #d8dbd3;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.headerempty {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.headerfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.headersandfooters {
    background-color: #edf2f9;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.headerstrong {
    background-color: #d8dbd3;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.headerstrongfixed {
    background-color: #d8dbd3;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.heading1, .heading2, .heading3, .heading4, .heading5, .heading6 { font-family: Arial, Helvetica, sans-serif }
.index {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.indexaction, .indexitem {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.indexprocname {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.indextitle {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: bold;
}
.layoutcontainer, .layoutregion {
    border-width: 0;
    border-spacing: 30px;
}
.linecontent {
    background-color: #fafbfe;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
a:link { color: #0000ff }
.list {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: disc;
}
.list10 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: square;
}
.list2 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: circle;
}
.list3, .list4, .list5, .list6, .list7, .list8, .list9 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: square;
}
.listitem {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: disc;
}
.listitem10 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: square;
}
.listitem2 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: circle;
}
.listitem3, .listitem4, .listitem5, .listitem6, .listitem7, .listitem8, .listitem9 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: square;
}
.note {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.notebanner {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.notecontent {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.notecontentfixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.output > colgroup {
    border-left: 1px solid #c1c1c1;
    border-right: 1px solid #c1c1c1;
}
.output > tbody, .output > thead, .output > tfoot {
    border-top: 1px solid #c1c1c1;
    border-bottom: 1px solid #c1c1c1;
}
.output { border: hidden; }
.output {
    background-color: #fafbfe;
    border: 1px solid #c1c1c1;
    border-collapse: separate;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    }
.pageno {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
    text-align: right;
    vertical-align: top;
}
.pages {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: decimal;
    margin-left: 8px;
    margin-right: 8px;
}
.pagesdate {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.pagesitem {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.pagesproclabel, .pagesprocname {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.pagestitle {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: bold;
}
.paragraph {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.parskip > col, .parskip > colgroup > col, .parskip > colgroup, .parskip > tr, .parskip > * > tr, .parskip > thead, .parskip > tbody, .parskip > tfoot { border: none; }
.parskip {
    border: none;
    border-spacing: 0;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
    }
.prepage {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    text-align: left;
}
.proctitle {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.proctitlefixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowfooter {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowfooteremphasis {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.rowfooteremphasisfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.rowfooterempty {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowfooterfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.rowfooterstrong {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowfooterstrongfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowheader {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowheaderemphasis {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.rowheaderemphasisfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.rowheaderempty {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowheaderfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.rowheaderstrong {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowheaderstrongfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.systemfooter, .systemfooter10, .systemfooter2, .systemfooter3, .systemfooter4, .systemfooter5, .systemfooter6, .systemfooter7, .systemfooter8, .systemfooter9 {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.systemtitle, .systemtitle10, .systemtitle2, .systemtitle3, .systemtitle4, .systemtitle5, .systemtitle6, .systemtitle7, .systemtitle8, .systemtitle9 {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size: small;
    font-style: normal;
    font-weight: bold;
}
.systitleandfootercontainer > col, .systitleandfootercontainer > colgroup > col, .systitleandfootercontainer > colgroup, .systitleandfootercontainer > tr, .systitleandfootercontainer > * > tr, .systitleandfootercontainer > thead, .systitleandfootercontainer > tbody, .systitleandfootercontainer > tfoot { border: none; }
.systitleandfootercontainer {
    background-color: #fafbfe;
    border: none;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.table > col, .table > colgroup > col {
    border-left: 1px solid #c1c1c1;
    border-right: 0 solid #c1c1c1;
}
.table > tr, .table > * > tr {
    border-top: 1px solid #c1c1c1;
    border-bottom: 0 solid #c1c1c1;
}
.table { border: hidden; }
.table {
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 1px 0 0 1px;
    border-collapse: collapse;
    border-spacing: 0;
    }
.titleandnotecontainer > col, .titleandnotecontainer > colgroup > col, .titleandnotecontainer > colgroup, .titleandnotecontainer > tr, .titleandnotecontainer > * > tr, .titleandnotecontainer > thead, .titleandnotecontainer > tbody, .titleandnotecontainer > tfoot { border: none; }
.titleandnotecontainer {
    background-color: #fafbfe;
    border: none;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.titlesandfooters {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.usertext {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
a:visited { color: #800080 }
.warnbanner {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.warncontent {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.warncontentfixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
/*]]>*/
</style>
</head>
<body class="l body">
<div style="padding-bottom: 8px; padding-top: 1px">
</div>
<div style="padding-bottom: 8px; padding-top: 1px">
<div id="IDX" class="systitleandfootercontainer" style="border-spacing: 1px">
<p><span class="c systemtitle">Probability of n number of successful launches given diffuse prior</span> </p>
</div>
<div style="padding-bottom: 8px; padding-top: 1px">
<table class="table" style="border-spacing: 0" aria-label="Data Set WORK.EX2_3_MEANS2">
<caption aria-label="Data Set WORK.EX2_3_MEANS2"></caption>
<colgroup><col/></colgroup><colgroup><col/><col/><col/></colgroup>
<thead>
<tr>
<th class="r header" scope="col">Obs</th>
<th class="r header" scope="col">cumulative</th>
<th class="r header" scope="col">n</th>
<th class="r header" scope="col">probability_of_success</th>
</tr>
</thead>
<tbody>
<tr>
<th class="r rowheader" scope="row">1</th>
<td class="r data">0.2096</td>
<td class="r data">0</td>
<td class="r data">0.2096</td>
</tr>
<tr>
<th class="r rowheader" scope="row">2</th>
<td class="r data">0.5268</td>
<td class="r data">1</td>
<td class="r data">0.3172</td>
</tr>
<tr>
<th class="r rowheader" scope="row">3</th>
<td class="r data">0.7893</td>
<td class="r data">2</td>
<td class="r data">0.2625</td>
</tr>
<tr>
<th class="r rowheader" scope="row">4</th>
<td class="r data">0.9385</td>
<td class="r data">3</td>
<td class="r data">0.1492</td>
</tr>
<tr>
<th class="r rowheader" scope="row">5</th>
<td class="r data">0.9905</td>
<td class="r data">4</td>
<td class="r data">0.0520</td>
</tr>
<tr>
<th class="r rowheader" scope="row">6</th>
<td class="r data">1.0000</td>
<td class="r data">5</td>
<td class="r data">0.0095</td>
</tr>
</tbody>
</table>
</div>
</div>
<div style="padding-bottom: 8px; padding-top: 1px">
<hr class="pagebreak"/>
<div id="IDX1" style="padding-bottom: 8px; padding-top: 1px">
<div class="c">
<img style="height: 480px; width: 640px" alt="The SGPlot Procedure" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAoAAAAHgCAIAAAC6s0uzAAAACXBIWXMAAA7DAAAOwwHHb6hkAAAgAElEQVR4nO3deVxU9f7H8cO+CaLgiguuoJLikrnmvqC4kOFV07R+dhXTlLLcTW+laS5xNZGyq2mGC+Y1LdyXJHFBBMUkBMVExGV0WBwQBub3x7GJy+aAA19meD3/4HHmbPM5Z86cN+fMOedrEh0dLQEAgIplLklS27ZtRZcBAEAVcvnyZVPRNQAAUBURwAAACEAAAwAgAAEMAIAABDAAAAIQwAAACEAAAwAgAAEMAIAABDAAAAIQwAAACEAAAwAgAAEMAIAABHAp5OXlbdq0qVu3bg4ODra2tu3bt//ss8+USmUFvLWjo6OJiUlKSoqO4+fl5b3yyitNmzZVKBQv+NbW1tYmf7G1te3YsWNgYGBeXp4e36jATEq7sM+d4YvLvxK05s6dq5eZF0fvS1HB5JU2ffp0bZ+kpCQTE5NOnTrp6y1efFPRXVpamq+vb/Xq1U1MTAICAvIPevLkyapVq9q3b1+jRg07O7uOHTuuXLkyIyOjAqoqmxKWpYDi1rD84cbHx5dnmSWpyI++/BDAulKr1SNHjnznnXfCw8PT09MzMzOjoqIWLlzYunXrR48eia5OkiSpd+/eJiYmR48elV/m5uZKkqTRaPT4FpmZmZGRkdOmTRszZox2zrq8UYHaCnvxaitg8SuAcSxFfkFBQb///rvoKvRg9erVISEhaWlpkiR5enpq++fl5Q0cOPDDDz+MiopSKpUqlSoyMnLOnDlt27Z9+vSpuHpLUtyyoIIRwLr69NNP9+/fb2FhsWbNmocPH6ampkZERMyfP79NmzY1a9YUXV1BpqamERERN27ccHZ21ssMr1+/rtFobt26NXfuXFNT0927d3/99df6eiO9V6v3GcrklaD1+eef63HmhZXTUlQwtVr9/vvvi65CD2JjYyVJ+vjjjzUaTa9evbT9L1y4cObMGXNz8x07dqSlpT1+/PjcuXOzZs3q3LmzlZWVuHpLUtyyoKJFR0dr8DzZ2dnVq1eXJOmzzz4rbhwzMzNJktLT0+WXTk5OkiTdvXtXo9HI03799ddt27a1t7fv3bv3xYsXJ0yYULt27bp16wYFBek4B7n75MmTr7/+urOzc7Vq1bp163b27FmNRtOxY0ftZ9qvX7/8kwwbNkySpHnz5smzffjwoYWFhbm5+f3791Uq1axZs+rWrWtlZdW9e/eLFy8WXi55J5I/e6ZNmyZJUqtWreSX+Ws7d+5c//79a9asWb169R49enz//fdqtbq42n799demTZt6eHgUmIncvXv37nbt2smFXb58ueRVVMLiazSap0+fLl68uEmTJhYWFvXq1Zs2bdrjx4/zF7958+aOHTvKJw8jIiJ0WQm6f+5Fzjw3N3f16tVt2rSxsrJq0KDB+PHj4+LiynUpStgMivzUCi+plu4rrXr16n369JEk6eeff9ZoNLdv35YkqWPHjjquuud+ZUrYVIrbtgtve/kVt5LlqWTVq1fPP0lERIQkSba2tqdOnSpydZWwmEVuBiX0L26hivsEi+xfeFl03PMU+HCL+0YUuYPS5V10/6aUPElp15Io0dHRBLBOLly4IEmSiYmJdusp7LmbV3EsLCzu3Lmjyxzu3r2bm5tbYG61a9dOS0srYd+9a9cuSZKaNm0qz3b9+vWSJHl7e2v+2ilrOTo6KhSKAstV+JsWFRUlj5+ampr/jbKyshwdHQss3fXr14urrUuXLpIkjR8/XlNUAFtYWGincnFxefLkSQmrqOToev311wtU1b59++zs7CI/Gu2KKrwSCti8eXNpP3ftzCdNmlRg0Ouvv16uS1HcZlDcp1bcdl6qlVa9evWoqChTU1N3d/ecnJzSBnBxtF+ZEjaV4rbtwttefsWt5BICODc3V56bJEn16tUbN27cli1b8n+PSljMIjeDEvoXuVDFfYLF9S/XAC5uB1Xaj7vkb0rJk5RqLRXebisMAayrgwcPSpJUq1atEsZ57uY1YcKElJSUDz/8UJIkW1vbHTt2PHz4sFGjRpIkHTp0SJc5yN1vv/32hg0bHj16lJyc3LJlS0mSTp8+rfnrVNKRI0fkyfPnotx94cIFjUYj7yx27tx56dIlSZKcnZ0vXLigUqk++eQTSZIWL15cYLkKf9O01wTdunUr/xslJydLkuTg4PDtt98mJycfOHCgd+/eeXl5xdVWv379P/74o0C12m4/P7+UlJSLFy/WqlVLkqRvvvmm5FVU3OLL/y6Ympru2rUrIyPj+PHjDg4OkiT98MMP2tF8fX1TUlLOnj1rampawu6mAB0DuPDMr169Ks9h5cqVSqXy1q1bM2fOlNd8+S1FcZtBCZ9acXRfafL+ffLkyZIkBQQElDaAn/uVKW5TKWHbLrztaZW8kkeNGiVJ0rZt2wqvkPT09AULFjRp0kS7bdja2q5du7bkxSxuMyiuf3ELVdwnWMInW2BZ9HsEXNwOSr/fFHmScePG/fnnn/knKe1aKnILrxgEsK7OnTsnSZKJiYn8r1yRdNyId+zYIUnS0KFD5dEGDx4sSdLevXt1n8OtW7dmzJjRtm1b7f+A8uTF7bs1f+0BZ8+eLV+16ODgkJmZ+e233xYOFW1hWoW/afI5N+35gPxvtHTpUnNzc0mSnJycPv74Y/kQubja8u/LCgew9jvv7+8vSZK/v3/Jq6i4xZcXs3fv3tr3kk+hv//++9rRkpOT5UH169cvcrfyIqegC8/8P//5jyRJ3bp1yz8f+bitXJeiyM2ghE+tOLqvNDmA79275+DgULNmzejo6FIF8HO/MsVtKiVs24W3Pa2SV3IJAayVkJDw9ddfDxo0SH7HsLCwEhazuM2guP4lLFRxn2Bx/cs1gIvbQen3m1KgMO0kZVhLokRHR3MRlk7atWtnZ2en0Wi++OKLksdUq9UljyBvhcW9fO4c7t2717Fjx3Xr1l2+fDk1NbXk99KaMGGCJEm7du3atm2bJEm+vr7W1tby/4wFJCUlPXduX375pSRJ7du3r1atWoFBixcvvnbt2gcffJCXl7d06dJWrVpdv369uPn0799fl+LlK4FtbGy0fZ67kgvT5LuQWHsPlZaJiYnckf9kZqmUUFJxM9eU/trmF1yKIjcDqZSfmu5vp1W7du358+c/evRo6dKlhYe++FdGS7upPHfbLmHbK3kll6xp06bvvPPOwYMH5fmfOXNGO6i4xSxuMyjcv4SFKu4TLNUnW4avVWHP3UGV0zdFO0kZ1pJABLBOrKys5P+FP/vss/nz59+6dSs9PT06OnrFihUdOnTIysqSJMnOzk6SpJ9++unhw4cLFy4sw72buszh8OHDDx8+HDx4cGRk5OrVq+UdqEz+504+A1NAz549XV1d//zzzzVr1kh/7Yjlk5A1a9YMDQ3NzMxMTExcs2bNyJEjS6gwMTHx3Xff/f777yVJkk8M5nfnzp1Bgwbdvn178eLFN27c6NevX3JysnyxdAm1FWfVqlUPHjyIjIzcvn27JEkeHh4lr6Li3kK+6/T06dM7d+5UqVTHjh2T69fX3ahl+Ny7du0qSVJ4ePjKlStTU1Pv3r27dOnS2bNnl/dSFLkZlPCp6dGsWbOaNm36448/5u/54l8ZWeFNpQzbtlTWlXzt2jUPD48VK1ZERkampqamp6eHhIScP39ekqQGDRqUsJjFbQbF9S9uoYr7BHX/ZPX1QUgl7qD0+00pTmnXUpmXVD84Ba2jrKysIv9rtrOzu3LliuavM2MyCwsL+T+ywqdxdu/eLeU7nzZ06FDpr1M0uszh+PHjhWvYuXOnRqOZMWOG/NLFxUVT6BTNggUL5KGNGjXS/vIhn5PMr1evXgUWvMifP/38/LQjaN/ol19+KTzmf/7zn+fWpinqFHT+A52mTZvKVxuVsIpKeIvnXr6kraRx48ZSKU9B6/i5F5h54TXfo0eP8l6KIjeD4j61tLS0Vq1aubi4xMfHF5iJ7ist//VKISEh8sy1p6Bf/CtTwqZS3LZd3DlVWQkrubhT0CEhIUWeA+jevfvTp09LXsziNgPd+/fq1au4T7CE72OBZdF9G87/4Rae+cSJE0vYQen3m1KqSUpYS0VuBhWD34BLJycnZ/369Z07d7azs7O2tnZzc/P395cvRNJoNDdu3Ojbt6+NjY2bm9v+/fuL+x2lhL2JjnOYNWtW9erVGzduvGDBgvHjx0uS9Mknn2g0mnv37g0ePNjW1laSJKVSWWADle/8k/LdiKL56xL/Vq1aWVpauri4jBo1KioqqsBS5/+m2djYdOrUacuWLflH0L5RZmZmYGBgly5dHB0dq1Wr1qZNm1WrVsnjlFybpqgA/u6779zc3CwtLXv27Pn7778/dyWX8BZPnz5dtGiRq6urubl5vXr1/Pz8CtzA8yIBrOOnVmDmubm5a9eubdOmjaWlZd26dUeOHBkZGVneS1HkZlDcpyYHcL169QrPp2wBrPnrF25tAL/4V6aETaW4bbvkAC5hJZfwG3B8fPwHH3zg4eFhY2Pj6OjYqVOn9evXZ2VlPXcxi9sMSuhfeKGK+wRL+D4WWBbdt+H8H27hPJs4caKm+B2Ufr8pJU+i+1oSKDo62iQ6Orpt27aFVyUAACgnly9f5jdgAAAEIIABABCAAAYAQAACGAAAAQhgAAAEIIABABCAAAYAQAACGAAAAQhgAAAEIIABABDAXOzbp6WlhYeHT5kyZdWqVYUfgx4WFjZ58uTExMSBAwdu27ZN27pkkbbv/jEjI6M8iwUAQCf169YZ5jWo5HEEB7DcvlCRLThmZ2f7+vouXrzY19fXz89v3rx5GzZsKGFWGRkZU956s7wKBQBAZ0Gbtz53HMGnoM+fP3/+/PmWLVsWHnTmzBlLS0s/Pz9nZ+cFCxZo2zIDAMAIVN7fgOPj4+U22CVJcnNze/DgQVpamtiSAADQF8GnoEuQmZlpb28vd9vY2Jibm6tUKgcHB7lPbNz1R4+V2pGLbBAbAICyUaZnK9Ofyt0PlVkZmTly9z1FZlZ2rtydmJwud6hzNZ/4dSrtW1TeALazs0tP/2vZ1Gq1Wm1nZ6cdamNjY69Wa1+am1feBQEAlIcMVc5DZZbcrcz4Oy8VqU8zVM/yMun+E7U6T+5OvPt3XibdeyJ3Z2WrUxSZhWfoaG/paG8ldzs7WlezeXaYV9fJxtrKTO5uULuauZmJJEnaPqVSeXOrRYsWMTExcndcXFydOnW0B8SSJDVu2KDA+L/+Fl5xxQEAdJCVnZvyUCV3Z2T+HW+pGdnK9Gy5O0Whynr67Jgy6f4Tde5feZn87MYWdW5e0v2/8vJpbori2Qyr2Vo4O1rL3Y7V/jcvbZ+lW10nW2vLZ+nYu2N9ucPczNSltq3cbW1pXtfJpvAMK0DlDeAuXbqo1erAwMDRo0cvWbLEx8dHdEUAYITUuXn5Dgf/jrcnmWptXj5UZmmPKVMUmVnZz05AJt17os7VyN1/H1+q/85La0uzus7Poq6aTb68tLd0tLeUu/MfX3Z5qba52bOLkxp7V5M7zM1MG9R+dgbU2sqsrpOtfpZctMoYwB06dPj222/bt2+/c+fOyZMn+/v79+3bNygoSHRdAGDYEpPTr954HJPwKOL3h7GJythEpTo3z9zMtEGdv+LN8u94q2Zrni8vrRyrPctLTzcn7TFlg9p2ZmYmcrdrvWcnKc3N/85LlKBSBPDBgwfzv4yMjJQ7evToERsbK6IiADB4yvTsmIRH0XGK2ERlxLUHsYlKa0vzTq2d3V0dR/Z2bdOshkezGtrDTVS8ShHAAIAXpM7Ni01UXk14HBWniEl4FPWHQpmR7dGshmdLZ49mNUb1a+LZ0ll71heVAQEMAAYpRaG6eO1hbKIy4vcHsYnKmITH7q6O7q6Onm5Ok0e6t2las3lDB9E1oiQEMAAYgAxVTkzC4+jripj4RzEJj6PiHpqbmXZqXcvd1XFwt4ZzJnm6uzpqf5qFQSCAAaAyikl49Met1Kg/FDEJj6LiFA+VWe6ujp4tnTya1RzZ27VdS6eKvGEG5YEABgDxHiqzLl57GJPwSP75NjZR6VrfXk7c8UNaLJ/e2d3VUXSN0DMCGAAqWoYqJzZRGX1dEZPwOCb+UVScQpIkj2Y1Pd2cenjWfde3jburYzVbnrBr5AhgACh3sYnKP24po/5QRMUpYhOVicnp8tVSHs1qDu7asF3LmkbzcAnojgAGAD17qMyKjlPEJDyWf76NTVQ6O1p7tnRyd3UcP6SFW+PqHs1qiq4R4hHAAPBCsrJzYxOV0XGKmIRHMQmPo/5QZGWrPZrV9Gzp1Kl1rf8b4e7RrAbnk1EYAQwApZOYnC7/fCtfLRWbqPRoVsPd1bFT61q9O9Zv19KJBzFCFwQwAJREmZ4dFffwasJj+e7bmITHjtUsPd2c3F0dX+/XpE2zGu6ujjzQEWVAAAPA39S5eTEJj//46+HJ2gc6dmpVy6NZjTe8mns0q8kDHaEXBDCAKi3p/pPovx6eHJPwOP52avOG1d1dHTu1dp480r1dCyfX+vbPnwtQegQwgCpEmZ4dm6i8KB/dxiliEh5ZW5p7ujl5NKvh3bMxD3RERSKAARgtuYGgP26lys0VaB/o2KlVLXdXx1H9mng0q8kDHSEKAQzAeGgbCIqKU8TEP5If6OjRrKZHsxqThrV0a+zIAx1ReRDAAAyV/EDHi7EP5aulYhIeSZLk2dLJo3nN/p1dZo7x8Ghek/PJqLQIYACG5FB40tkr9+Sfb5PuPfFoXlNuc35w14YdWzlzPhkGhAAGYBhOXkz2Xx0uSZJ3z8Y80BFGgAAGUNmdvJi89OvIFIXq8xmdR/RyFV0OoB8EMIDKS47epPsZC/+vwxtezXngFIwJAQygMiJ6YfQIYACVS1ScYlHghdhEJdEL40YAA6gsouIUS7++ePbK/SVTOu5dNZDohXEjgAGIp43euZM8g5f14+ZdVAUEMACRYhOV89afJ3pRBRHAAMSIv5322X8ij567M3tCO6IXVRABDKCiydF74PSf00e3ubLTl+Z1UTURwAAqTv7ovb53DNGLqowABlARUhSqpV9Hhhy7QfQCMgIYQPlKUahWfBe9Zf8f00d7EL2AFgEMoLxoo3fSMLdrIaPrOtmKrgioRAhgAPpH9ALPRQAD0CdlenZA8JWNe66NGdSM6AVKQAAD0A85etfvuurds9GlH14jeoGSEcAAXlT+6A3fPLJ5QwfRFQEGgAAGUHZZ2bmrv7/85Q9XiF6gtAhgAGWRlZ0btOfaqm3R/V9xIXqBMiCAAZSOHL2fb4nq8lLt/V8O9mzpJLoiwCARwAB0lT96Q9d5Eb3AiyCAATyfOjdve2j83HXniV5AXwhgACWRo/fTbyNd69kTvYAeEcAAiqaN3ga1q32z8NXeHeuLrggwKgQwgIKIXqACEMAA/se+U4lLgi462lsRvUC5IoABPCNHryRJn894ZVDXBqLLAYwcAQzg7+hdMqXjiF6uossBqgQCGKjSjp2/M/vLsxLRC1Q4Ahiook5eTF76deRDZdan0zoRvUDFI4CBKkeO3qT7GQv/r8MbXs3NzUxFVwRURQQwUIUQvUDlQQADVUJUnGLe+vPxt1OJXqCSIIABIxcVp1j69cWzV+5/PqMz0QtUHgQwYLS00Tt3kmfwsn7WlmaiKwLwNwIYMEIxCY8WBUYQvUBlRgADRiX+dtpn/4k8eu7O7AntiF6gMiOAASMhR++B039OH93m+n/HEL1AJUcAAwbvf6J37xhHe0vRFQF4PgIYMGApCtW89eeJXsAQEcCAQUpRqFZ8F/39L9eJXsBAEcCAgZGjd8v+PyYNc7uy8/W6TraiKwJQFgQwYDDyR++1kNFEL2DQCGDAACjTswOCr3wZfIXoBYwGAQxUanL0rt91dWRvV6IXMCYEMFBJaaPXu2ej8M0jmzd0EF0RAH0S/Fj2sLAwd3d3a2vr4cOHp6amFhh68uTJNm3a2Nvbjxo1SqlUCqkQqHgZqpylX19s4bMj8W56+OaRmz/uTfoCxkdkAGdnZ/v6+s6cOTMpKcnKymrevHn5h6rV6tGjRy9evDg5OdnKymrRokWi6gQqTFZ2bkBwTKvXdxG9gNETGcBnzpyxtLT08/NzdnZesGBBSEhI/qF37txJTU39xz/+YW9vP2bMmIsXL4qqE6gAcvQ2GRZ88mJy6DovohcweiIDOD4+3sPDQ+52c3N78OBBWlqadqiLi0udOnW2bNmSnp6+ffv2rl27CioTKF8FonfvqoEezWqKLgpAuRN5EVZmZqa9vb3cbWNjY25urlKpHBye/ddvbm6+fPnyCRMmvPXWW/Xr1z937tz/TpulVqu1L01MTSqsbEBf1Ll53x2IW7ghostLtUPXeXm2dBJdEYCKIzKA7ezs0tPT5W61Wq1Wq+3s7LRDIyMjP/roo9OnT3t6en711VdeXl5RUVFmZs8aeLkQeSnp7l3tyNZW1hVZOfCC1Ll520PjP/02snnD6kQvUDWJDOAWLVrExMTI3XFxcXXq1NEeEEuSdPz48f79+3fv3l2SpA8//HDx4sV3795t0KCBPPTV7gXPSAdt3lohVQMvRBu9DWpX+2bhq7071hddEQAxRP4G3KVLF7VaHRgYqFAolixZ4uPjk39o165dDx06FBERoVKp1q5dW7duXRcXF1GlAi9OPuHc6vVdW/bHfbPw1RNB3qQvUJWJDGALC4udO3cGBAS4uLhkZGQsW7ZM7t+hQ4dLly5179592bJlY8aMqVWr1r59+/bv329iwg+9MFT7TiW2H/cj0QtAS/CTsHr06BEbG1ugZ2RkpNzx9ttvv/322xVeFKBPWdm5ExadiL+duu6jbuQuAC0eRQmUI2V69jD/gw1q213Y5mNuJvjBcwAqFfYIQHlJUai6vvXfTq1rBS/rR/oCKICdAlAuYhOV7cf9OHVU67Xv8wwZAEXgFDSgf2FRKcP8D25a1GtU3yaiawFQSRHAgJ7tOX5z6rLTe1cN5JIrACUggAF9CgiOWbUt+kSQN89zBlAyAhjQm3nrz//3ZOLpTcNd69s/f2wAVRsBDOiBOjfvnU9/jb+ddnrTcGdHnkwO4PkIYOBFZahyfOcetbY0C/23VzVbC9HlADAM3IYEvJAUhWrAuz83qG23e0V/0heA7ghgoOxiE5V9phwY3LXhNwtf5VEbAEqFU9BAGUX8/sBn9uGFkztMea2V6FoAGB4CGCiLQ+FJk5ac3Di/x4herqJrAWCQCGCg1LaHxs/+8uzuFf17eNYVXQsAQ0UAA6Wz4ruojXuunQjydnd1FF0LAANGAAO6UufmfRhw7ui5O+GbR9R1shVdDgDDRgADOsnKzp2w6MRDZVb45hHcbgTgxXHjBPB8GaqcAdN+liTpyIYhpC8AvSCAgedIUahefnNvp9a1dq/oz82+APSFvQlQkthEZftxP04d1Xrt+11F1wLAqPAbMFCssKgUn9mH13/U/R8Dm4muBYCxIYCBou05fnPqstO7V/Tv3bG+6FoAGCECGCjCV7uufr4l6siGoZ4tnUTXAsA4EcBAQfPWn//vycTTm4a71rcXXQsAo0UAA39T5+a98+mv8bfTTgR586gNAOWKAAaeyVDl+M49am1pFvpvL272BVDeuA0JkCRJSlGoBrz7c4PadrtX9Cd9AVQAAhiQ4m+n9ZlyYHDXht8sfJVHbQCoGJyCRlUX8fsDn9mHF07uMOW1VqJrAVCFEMCo0o6dvzN+0Yn1c7qP6ttEdC0AqhYCGFXX9tD42V+e3b2ifw/PuqJrAVDlEMCoolZ/f/nLH66cCPJ2d3UUXQuAqogARpWjzs37MODc0XN3Lmzz4WZfAKIQwKha1Ll5Y+cfT1GowjeP4HYjAAJxxwWqkAxVTp8pByRJOhHkTfoCEIsARlWRolC9/ObeTq1r7V7Rn5t9AQjHbghVQmyi8uUJeyePdF/7flfRtQCAJPEbMKqCsKgUn9mH13/U/R8Dm4muBQCeIYBh5PYcvzl9xW87lvXr19lFdC0A8DcCGMbsq11XP98SFbrOy7Olk+haAOB/EMAwWosCI0KO3TgRNKx5QwfRtQBAQQQwjJA6N++dT3+Nv512IsibR20AqJwIYBibDFXO2AXHJEkK/bcXN/sCqLS4DQlGJUWhGvDuz3WdbPeuGkj6AqjMCGAYj/jbaX2mHOjfucE3C1/lURsAKjlOQcNIRPz+wGf24YWTO0x5rZXoWgDg+QhgGINj5++MX3Ri/Zzuo/o2EV0LAOiEAIbB23k4Ydbq8N0r+vfwrCu6FgDQFQEMw7b6+8tf/nDlRJC3u6uj6FoAoBQIYBgw/zXhB8/cvrDNh5t9ARgcAhgGSZ2bN3b+8RSF6sJWH243AmCIuFUDhidDldNnygFJkk4EeZO+AAwUAQwDk6JQdX1rX6fWtYKX9eVmXwCGi/0XDElsovLlCXsnDWu59v2upC8Ag8ZvwDAYYVEpvnOOrprV5Q2v5qJrAYAXRQDDMOw5fnP6it++/6RPv84uomsBAD0ggGEAgn689ummyP1rB3VqXUt0LQCgHwQwKrtFgREhx26cCBrWvKGD6FoAQG8IYFRe6tw8v+VhMQmPTgR586gNAEaGAEYllaHKGbvgmCRJR74ays2+AIwPN3KgMkpRqLzeC3V2tN67aiDpC8AoEcCodOJvp/WZcqB3x/qbP+7Nzb4AjBWnoFG5RMUphs06OHeS57uj24iuBQDKEQGMSuTY+TvjF51YP6f7qL5NRNcCAOWLAEZlsfNwwvSVv+1dNbCHZ13RtQBAuSOAUSms/v7ylz9cOb1puLuro+haAKAiCL7CJSwszN3d3draevjw4ampqQWGKhSKUaNG2dnZtW3b9tSpU0IqRAXwXxO+6b+xF7b5kL4Aqg6RAZydne3r6ztz5sykpCQrK6t58+YVGGH8+PENGjT4888/161bFxoaKqRIlCt1bp7vnKMRvz+4sNWHR20AqPR7VOwAACAASURBVFJEnoI+c+aMpaWln5+fJEkLFiwYOHDghg0btEMTExMjIiL27dtnaWnZq1evXr16iasU5SJDlTPM/5Czo/WJIG9uNwJQ1Yjc68XHx3t4eMjdbm5uDx48SEtL0w69dOlS06ZNJ06caGtr27lz5ytXrggqE+UiRaHq+tY+Tzen4GV9SV8AVZDII+DMzEx7e3u528bGxtzcXKVSOTg8e+C+UqmMiIiYPHnyN998s3Hjxtdeey02NtbMzEweGhl95cHDh9pZWVpaVnDxeBGxiUqv90Knjmo1Z6Kn6FoAQAyRAWxnZ5eeni53q9VqtVptZ2enHWpra/vyyy+/8847kiR98MEHy5cvT0hIaNmypTy0Qf16NWv8fcGOmZlZXHxCBdaOsguLSvGdc3TVrC5veDUXXQsACCMygFu0aBETEyN3x8XF1alTR3tALEmSm5tbQkKCWq02Nzc3MTGRJMnC4u9nAteu5VzB1UIv9p1KnLosbMuS3oO6NhBdCwCIJPK3ty5duqjV6sDAQIVCsWTJEh8fn/xD27VrV7t27aVLl6alpX311Vd169Zt3LixqFKhF0E/Xpu+4rf9aweRvgAgMoAtLCx27twZEBDg4uKSkZGxbNkyuX+HDh0uXbpkYmKye/fuw4cP16lTZ9u2bbt27TI15VIdA7b064tf/nDlyIahnVrXEl0LAIgn+ElYPXr0iI2NLdAzMjJS7mjduvW5c+cqvCjomTo3z295WEzCoxNB3tzsCwAyHkWJ8pWhypmw+ERWdu6Rr4bSsi8AaJXlpO7Zs2f1XgeMUopC5fVeqKO95f61g0hfAMivLAHs4+Pj7u6+fPnypKQkvRcEo5GYnN5nyoEennU3f9ybR20AQAFl2S0mJSWtXbv2ypUrrVq1Gjhw4Pbt21Uqld4rg0GLilP0nPzT9NFtlk/vLLoWAKiMyhLAZmZmXl5eP/zwQ3Jy8pgxYz788MN69epNnTo1Li5O7/XBEJ28mDxg2s9fzu727ug2omsBgEqq7CcG4+LiVq5c+cknn9SsWXPhwoWurq69evXaunWrHouDIdp5OMF3ztG9qwaO6ttEdC0AUHmV5SroDRs2bN269fr162PGjNm1a9fLL78s9x86dOiAAQPefPNNvVYIQxIQHPP5lqjTm4bTsi8AlKwsAfzLL7988MEHI0aMKNAEwksvveToyG636vJfE37wzO1LP7zGzb4A8FxlOQU9ZswYX1/f/On78ccfyx2///67fuqCQVHn5vnOORrx+4MLW31IXwDQRekCOCUlJSUlZcKECSn5/PbbbytXrnw2O54WWfVkqHIGTPtFkqQjG3jUBgDoqnSnoOvVq1egQ5IkOzu72bNn67MoGI4UhWrAtF/6v+LyxcxXuNkXAHRXugDOycmRJKlTp04RERF/z8Kc51lWUbGJSq/3QqeOajVnoqfoWgDAwJQuO/Py8iwtLaOiosqpGhiQsKiUsfOPfT7jlTe8mouuBQAMT+nOGbZv316SJJOilE95qKT2nUr0nXN006JepC8AlE3pjoBPnDghSdLt27fLpxgYhm/3xS4Jurh31cAuL9UWXQsAGKrSBXDt2rUlSWrQoEH5FAMDsPTrizsOJxzZMJRHbQDAiyhdAJdwqlmj0bxwMajU1Ll5M1aeibj24ESQNzf7AsALKl0Ac/K5yspQ5UxYfCIrO/fERm9u9gWAF1fqU9AFHj+JquChMstn9mHX+va7V/TnZl8A0AuugsZzJCan95z8Uw/Putv+1Yf0BQB94SpolCQm4ZHXjNDZE9rNHOshuhYAMCplvAo6LCxsx44d9+/fb9So0YQJE9q1a1c+5UGkkxeTfecc3Ti/Jy37AoDeleWMYmBg4NChQzUaTceOHTMyMnr27Pndd9/pvTKIFRaV4jP78N5VA0lfACgPZXmM82efffbTTz/16tVLfjl69Oi333574sSJei0MIoVFpfjOObp/7eAennVF1wIAxqksR8C5ublt27bVvmzfvv3Tp0/1VxIEi01Ujp1/bOP8HqQvAJSfsgTw2rVrZ8yYkZ2dLUlSRkbGrFmzNmzYoO/CIEbS/Sd9phxYNavLiF6uomsBAGNWulPQ2pYHc3Nzd+zYIUmSRqPRaDTbt29Xq9X6rw4VK0WhGjDt57mTPP8xsJnoWgDAyJUugOPj48upDgiXocoZ5n9ozMBm3HEEABWgdAHs6uoqd9y9ezcuLi4nJ0eSJLVafe3aNX9/f70XhwqTlZ3r9V5oD8+6H/+zo+haAKBKKMtV0EFBQTNmzKhfv/6tW7fc3NyuX7/et29fAthwqXPzJiw6UdfJdu37XUXXAgBVRRlvQzpw4MDAgQNtbW2jo6P/9a9/1a9fX++VocK8tfRUVrZ676qBogsBgCqkLFdB379//9VXX5UkycnJ6dGjR1OmTOEqaMPlvyY8MTk9+LN+POcZACpSWfa5HTp0+PXXXyVJatGiRUREhJ2dXWJiop7rQoVY8V3UwTO3Q//tRQuDAFDByhLA8+fPDwgIkCRp4sSJU6dOHTVqVLdu3fRdGMrdV7uubtkfdyKI9n0BQICy/Abs7e3t7e0tSdLEiRNr1qx569at8ePH67swlK89x29+viXqRNCwuk62omsBgKqoLAEsSVKB1pAcHR31WxbK1bHzd6YuO3160/DmDR1E1wIAVRStIVU5YVEp4xed2LtqoLsr/zYBgDC0hlS1xCYqfWYf/v6TvjS0AABi0RpSFRJ/O23AtJ83zu85qGsD0bUAQFVHa0hVRYpCNcz/4OwJ7Ub1bSK6FgAArSFVDRmqnAHTfpk0rCUNLQBAJUFrSMYvQ5Xj9V5o/1dc5kz0FF0LAOCZMraGdOnSpS1btty+fbthw4Zvv/12u3bt9F8a9EGdmzd2wTHX+vY0tAAAlUpZfgP+8ccfe/XqlZ2d3a1btydPnnTr1m3fvn16rwx6MXb+cWtL880f9xJdCADgf5TlNqRFixaFhIQMHPis8Zxhw4YtWLBgxIgRei0MeuC/JjxFoQr9txcNLQBAZVOWAP7zzz+7dv37fGbv3r1v3bqlv5KgH0u/vngyIvn0puE86hkAKqGyHBh5enrmf/TVV1991b59e/2VBD0ICI7ZcTghdB3NHAFAJVWWI+B169YNGjRo06ZNrq6ucXFxjx49OnTokN4rQ5nJDS1c2OZDQwsAUGmVJYDv3bsXHx//yy+/JCUljR07dsiQIfb29nqvDGWz71TirFVnTgR5N6htJ7oWAECxyhLAvr6+SUlJ//jHP/ReDV5QWFTK1GVhu1f0p6EFAKjkyvIbcEhIyIwZM86ePav3avAiYhIeDfM/GLyMhhYAwACU5Qh43LhxGo1m69atZmZm2p48ilKs2ESl14zQTYt69e5YX3QtAIDnK0sAR0RE6L0OvAi5oYWFkzvQ0AIAGIqyBLD2gZSoDJTp2X2mHJg+2mPKa61E1wIA0FXpfgNOTU194403mjVr9s9//vPJkyflVBN0l6HKGeZ/cHC3hjRzBACGpXQBPHv2bIVC8cUXX9y4cWPu3LnlVBN0pM7N85l92N3VkYYWAMDglO4U9P79+8PDw5s0aeLp6dmzZ89169aVU1l4LnVu3tj5xx3trQLn9RBdCwCg1EoXwPfu3ZN/AG7SpElycnK5VATd+K8OT1GoTgR509ACABiiUu+7TUxMtH8hyrz156PiFDRzBACGq9RXQee/Byl/d6dOnfRTEZ4nIDjmvycTTwR509ACABiu0gWwnZ1d7969C3dLkpSRkaG/qlCs7aHxq7ZF09ACABi60gUwKSvWnuM35647d2TDUNIXAAxdWR7EASHColKmLjsd+m8vGloAACPAJTyGIeL3Bz6zD+9dNbBT61qiawEA6AEBbABiE5U+sw9vnN+TZo4AwGgIDuCwsDB3d3dra+vhw4enpqYWOU5cXJyNjY1Sqazg2iqJFIVqwLSfP5/xCg0tAIAxERnA2dnZvr6+M2fOTEpKsrKymjdvXuFxNBqNn5/f06dPK768yiBFoeoz5cDsCe3e8GouuhYAgD6JDOAzZ85YWlr6+fk5OzsvWLAgJCSk8DiBgYGdO3c2Na2Kp8ozVDm+c46O7O1KQwsAYHxEBlt8fLyHx7NocXNze/DgQVpaWv4RkpKSgoKCFi1aJKI6wdS5eV7vhXq2dFo+vbPoWgAA+ifyNqTMzEx7e3u528bGxtzcXKVSOTg4aEfw8/Nbvny5rW0R97wqHj/Oyvr7vLSZcR0iyw0t1HWyXfsBzRwBgHESGcB2dnbp6elyt1qtVqvVdnZ22qHBwcHW1tZDhgwpctobN2/du39f+9LKyqpcS61gfsvDlOlPQ9fxqGcAMFoiA7hFixYxMTFyd1xcXJ06dbQHxJIk7dmzZ8+ePdpWH2rUqLF//35vb2/55csdPAvMLWjz1vIvuSL4rwmPTVTS0AIAGDeRAdylSxe1Wh0YGDh69OglS5b4+PjkH5r/mixzc/OHDx86Ohr/E6ACgmMOnrkdvnkkDS0AgHETeYxlYWGxc+fOgIAAFxeXjIyMZcuWyf07dOhw6dIlgYWJEvTjtfW7Yk4EeTvaW4quBQBQvgQ/C7pHjx6xsbEFekZGRhboo1arK6oiYfYcv/nppkgaWgCAKoLGGCqFkxeTJ39y6vSm4TS0AABVBJf5iBcWlTJ2/vH9awd7NKspuhYAQAUhgAWLTVSOnX9s4/weNLQAAFUKASxS0v0nfaYc+HJ2txG9XEXXAgCoUASwMHIzR3MnedLMEQBUQQSwGBmqHK8ZoWMGNqOhBQComghgATJUOV7vhfbuVP/jf3YUXQsAQAwCuKKpc/PeWnqqrpPt2vdpaAEAqi7uA65oby09pc7N272iv+hCAAAiEcAVyn9NeGJyOg0tAAAI4Iqz4ruoo+fuhG8eQUMLAAACuIIEBMds2R93Isib9AUASARwxdhz/OaqbdEngobR0AIAQEYAl7tD4UlTl50+vWl484YOomsBAFQWXApUvsKiUiYtObl31UCaOQIA5McRcDmKTVT6zD68Y1k/GloAABTAEXB5ib+dNmDazxvn9+zX2UV0LQCASocALhcpCtUw/4M0tAAAKA4BrH8Zqpw+Uw5MGtby3dFtRNcCAKikCGA9kxtaGNyt4ZyJnqJrAQBUXgSwPqlz88YuOOZa356GFgAAJSOA9Wns/OPWluabP+4luhAAQGXHbUh6478mPEWhOrJhKA0tAACeiwDWj0WBEWFRKSc2eltbmomuBQBgAAhgPQgIjgk5doOGFgAAuiOAX9TOwwmfb4m6sM2HhhYAALrj18oXsu9U4uwvz54I8m5Q2050LQAAQ8IRcNmFRaVMXRa2e0V/GloAAJQWAVxGMQmPhvkf3L92MA0tAADKgFPQZRGbqPSaEbppUS/SFwBQNgRwqaUoVF7vhS6Z0pGGFgAAZUYAl85DZVafKQdmjX3p/0a4i64FAGDACOBSyFDl+Mw+PLhbw5ljPUTXAgAwbASwrtS5eT6zD7u7OtLQAgDgxRHAOlHn5o2df9zR3ipwXg/RtQAAjAG3IenEf3X4Q2XWkQ1DaGgBAKAXBPDzfRhwNipOEfpvL9IXAKAvBPBzBATHHDj9Jw0tAAD0iwAuyXcH4lZti6ahBQCA3nFOtVh7jt9cuOHCkQ1DSV8AgN5xBFy0sKiUqctOH9kwlIYWAADlgSPgIkT8/sB3ztG9qwZ6tnQSXQsAwDgRwAXFJip9Zh9eP6c7DS0AAMoPAfw/UhSqPlMOfD7jFRpaAACUKwL4b3L6zp3k+YZXc9G1AACMHAH8jNzQwsjerjS0AACoAASwJEmSOjfP673QLi/VWT69s+haAABVAgH8rKGFuk62X8x8RXQtAICqgvuAJb/lYRmZOfvXDuJRzwCAClPVA9h/TXhsopKGFgAAFaxKB/Dq7y8fPHM7fPNIGloAAFSwqhvAQT9e27jn99ObhjvaW4quBQBQ5VTRAN5z/OanmyJpaAEAIEpVDOCTF5Mnf3IqfPNIGloAAIhS5a48CotKGTv/+P61g0lfAIBAVSuAYxOVvnOOblr0Kg0tAADEqkIBnJic3mfKgfVzug/t0Uh0LQCAqq6qBHCKQuX1XujcSZ40cwQAqAyqRABnqHK8ZoSOGdiMhhYAAJWE8QdwhirH673Q3p3qf/zPjqJrAQDgGSMPYHVu3ltLTzWobbf2/a6iawEA4G9Gfh/whEUn1Ll5wcv6iy4EAID/YcwB7L8mPOn+ExpaAABUQkYbwJ/959LRc3fCN4+goQUAQCVknAEcEBzz/S/XTwR5k74AgMrJCAN4z/Gbq7ZFn940nIYWAACVluAfR8PCwtzd3a2trYcPH56ampp/UGZm5qJFi5o1a+bo6Dhu3LgCQ4tz9sr96St+O7JhqGt9+/IpGQAAPRAZwNnZ2b6+vjNnzkxKSrKyspo3b17+oVeuXElKSjp48GBCQkJmZubcuXN1mWen1s5HNgyhoQUAQCUnMoDPnDljaWnp5+fn7Oy8YMGCkJCQ/EM7d+68efPmFi1aODk5TZ8+PTw8XJd5mpuZejSrWT71AgCgNyIDOD4+3sPj2bMh3dzcHjx4kJaWVuSYCQkJzZs3r8DSAAAoXyIvwsrMzLS3f/ZLrY2Njbm5uUqlcnBwKDBaWlramjVrtm/fnr/nb2fPJ6fc0760trIq72oBANAjkQFsZ2eXnp4ud6vVarVabWdnV2AclUo1cuTIjz76qGPH/3mSc1uPNq3cWmhfmpqa7vxxX3kXDACAvogM4BYtWsTExMjdcXFxderU0R4Qy1JTU4cPHz5hwoS33367wLT21ewkqWBaAwBgKET+BtylSxe1Wh0YGKhQKJYsWeLj45N/qEKhGDRo0JQpUyZPniyqQgAAyonIALawsNi5c2dAQICLi0tGRsayZcvk/h06dLh06VJAQMC5c+feeOMNExMTExMTc3MjfGYIAKDKEpxqPXr0iI2NLdAzMjJSkqT27dv/61//ElEUAADljmaCAAAQgAAGAEAAAhgAAAEIYAAABCCAAQAQgAAGAEAAAhgAAAEIYAAABCCAAQAQgAAGAEAAAhgAAAEIYAAABCCAAQAQgAAGAEAAAhgAAAEIYAAABCCAAQAQgAAGAEAAAhgAAAEIYAAABCCAAQAQgAAGAEAAAhgAAAEIYAAABCCAAQAQgAAGAEAAAhgAAAEIYAAABCCAAQAQgAAGAEAAAhgAAAEIYAAABCCAAQAQgAAGAEAAAhgAAAEIYAAABCCAAQAQgAAGAEAAAhgAAAEIYAAABCCAAQAQgAAGAEAAAhgAAAEIYAAABCCAAQAQgAAGAEAAAhgAAAEIYAAABCCAAQAQgAAGAEAAAhgAAAEIYAAABCCAAQAQgAAGAEAAAhgAAAEIYAAABCCAAQAQgAAGAEAAAhgAAAEIYAAABCCAAQAQgAAGAEAAAhgAAAEIYAAABCCAAQAQQHAAh4WFubu7W1tbDx8+PDU1tVRDAQAwXCIDODs729fXd+bMmUlJSVZWVvPmzdN9KAAABk1kAJ85c8bS0tLPz8/Z2XnBggUhISG6DwUAwKCJDOD4+HgPDw+5283N7cGDB2lpaToOBQDAoJkLfO/MzEx7e3u528bGxtzcXKVSOTg46DI0KfluRsYT7azMzc0qsHAAAF6UyAC2s7NLT0+Xu9VqtVqttrOz03GoMjVV8eiR9qWlhWWFlAwAgH6IDOAWLVrExMTI3XFxcXXq1NEe8j53qEcr9wJzu3z193KuFwAAvRH5G3CXLl3UanVgYKBCoViyZImPj4/uQwEAMGgij4AtLCx27tw5efJkf3//vn37BgUFyf07dOjw7bfftm/fvsihxbGytAzavLX8qwYA4Dns7e2eO45JdHR027ZtK6CainH6zFknp5qt3VqKLsQYfPPd9/83YZypKY9Le1HxN27eup3Ur1dP0YUYgwOHjrR/ycOlfj3RhRi8J09Ue3/+Zfzo10UXYgwioy7navJebu+p+ySXL19m3woAgAAEMAAAAhDAAAAIIPIirPJQs0YN+2rP/+kbumjUwEWSTERXYQzsbG2dnWqKrsJI1KnlbG1tJboKY2BmZuZSj5/S9cOhuoMmL6+0UxnbRVgAAFR+XIQFAIAYBDAAAAIQwAAACEAAAwAggPEEcFhYmLu7u7W19fDhw1NTU0WXY9jS0tIOHTrk6uoaEhIiuhbDlpmZuWjRombNmjk6Oo4bN44ts8wyMjL8/f3r169fu3bt9957T61Wi67IGMTFxdnY2CiVStGFGDZzc3OTv4wcOVL3CY0kgLOzs319fWfOnJmUlGRlZTVv3jzRFRm2/v37L1q0iIdQvrgrV64kJSUdPHgwISEhMzNz7ty5oisyVNHR0Xl5eRcuXIiIiDh79uzGjRtFV2TwNBqNn5/f06dPRRdi8BwdHTV/+e9//6v7hEZyH/CZM2csLS39/PwkSVqwYMHAgQM3bNgguigDdv78eUmSBg8eLLoQg9e5c+fOnTvL3dOnT//ggw/E1mO4unfv3r17d7l79OjRFy5cEFuPEQgMDOzcufOpU6dEF1J1GckhTnx8vIeHh9zt5ub24MGDtLQ0sSUBBSQkJDRv3lx0FYZNrVZfu3Ztx44dvXr1El2LYUtKSgoKClq0aJHoQoyBhYVFrVq1nJyc3nzzzcePH+s+oZEEcGZmpr29vdxtY2Njbm6uUqnElgTkl5aWtmbNGn4ceUGzZs1q3bq1jY3NmDFjRNdi2Pz8/JYvX25rayu6EGNw9+7dBw8exMTEPHr06N1339V9QiMJYDs7u/T0dLlbrVar1Wo7Ox5IicpCpVKNHDnyo48+6tixo+haDNu6deuSkpIaN2781ltvia7FgAUHB1tbWw8ZMkR0IUalXr16X3zxxYEDBzQajY6TGEkAt2jRIiYmRu6Oi4urU6eO9oAYECs1NdXLy2vcuHFvv/226FoMnomJiYuLy7Rp03799VfRtRiwPXv2hISEyFft5ubm1qhR48CBA6KLMgY5OTmmpqYmJro+Qt9ILsLq0qWLWq0ODAwcPXr0kiVLfHx8RFcESJIkKRSKoUOHvvfee+PGjRNdi2FbtmyZvb396NGjc3NzV65c2bdvX9EVGbD8txeam5s/fPjQ0dFRYD0GbcOGDampqW+++aYkSbNnz3799dd1n9ZIjoAtLCx27twZEBDg4uKSkZGxbNky0RUBkiRJAQEB586de+ONN+SjDXNzI/mXt+KNGTPmt99+a9u2bdu2bZ2cnLjNAZXEyJEj4+LiXn755Xbt2jVs2HDt2rW6T0trSAAAVDRaQwIAQAwCGAAAAQhgAAAEIIABABCAAAYAQAACGAAAAQhgAAAEIIABABCAAAYAQAACGAAAAQhgAAAEIIABABCAAAb0rFq1asOGDcvfp3///jt27Cjb3BITE8upDaUVK1bY29tXr15drVbn75+UlPTmm2/Wr1/fxsame/fu+/btK493B0AAA/p36tSpbdu2ia7iObZt2yY3ZVog4EeMGGFmZhYeHq5UKtevX3/gwIG9e/eKKhIwYgQwoH8rV66cNWtWSkpK/p7x8fHW1tbalz169NixY4d8gLtx48bGjRvXrVv3wIEDq1evdnJyatSo0aFDh7Qj79ixo169eg0bNgwKCpL7XL16tXfv3g4ODh07djx37pwkSYmJic7OzkePHnVwcMg/rSRJ0dHRr776qr29vYeHh3xEW61atatXr7755pve3t75x8zLy4uOjp41a1bjxo2trKzat2//zTff+Pj4FFe/3N/b29vR0dHd3f27777TLmzhnoVrliTpk08+cXFxsbGxGTFixI0bN0roqfvkgEEggAH969+//2uvvebn56fLyLm5ufHx8RcvXvT39x8zZkxsbOyNGzemTp36/vvva0f46aefrl69+v3333/00Ue//fZbRkbGgAED+vfvf+fOnQ8//HDo0KGPHz+WJEmj0WzduvX27duDBg3Szj89PX3QoEGjRo26c+fO6tWr33zzzejo6IyMDDc3tyNHjhw4cCB/MaampnPnzh01atRXX31V4B+IIj158mTAgAEvvfTSjRs3goOD9+/fX1zPIms+c+ZMUFDQqVOn7t69O2DAAPmfgyJ76j45YDCio6M1APTHzs7u+vXrqampDRo0CA4O1mg0/fr1Cw4Ovn79upWVlXa07t27BwcH37x508zMTO4TFxdnZmamVqs1Gs0ff/xha2ur0WjkEZ4+fSqPM23atOnTp+/cubNly5baWQ0YMODrr7++efOmJElnzpwpUM+OHTvatm2rfTl16tT33ntPo9HIAVzkIpw7d27y5MnOzs69evXav3+/3LPI+kNCQtzd3fPy8vJPXmTPImuOiYmpWbPmli1bHj58qB1UZE/dJwcMQnR0NEfAQLlwcHAICgqaMWPGgwcPdJzEwsJCkiQzMzNJkiwtLXNzc7WDLC0t5Y5GjRrdu3cvKSkpLi7O5C9HjhxJSEiQp+3atWuB2SYlJTVp0kT7slmzZrdv3y65ks6dO3/zzTfJycmzZs366KOPFi5cWNyYf/75Z8uWLU1MTJ7bs8ia27Rps3fv3sOHD7dq1WrAgAFXrlyRJKnInrpPDhiKcrm6EoAkSUOGDPHy8nr33Xfll/LRbV5enqmpqSRJ2dnZOs5Ho9E8efLEzs5OkqSbN282atSocePG3bt3DwsLyz9aYmJikZM3aNAgLi5O+zI2NrZhw4a6vK+FhcXIkSPNzMxmzpz56aefFll/48aN//jjD41Gkz9ui+tZuGZJkl599dVXX301Nzd3zZo1Y8eOjYmJKbJnqSYHDAJHwEA5CggIOH369IULFyRJql+/vqWl5ebNmzMyMpYuXXr58mUdZ6LRaKZNm/b48eOTJ08GBwdPmDBh8ODBSUlJX375ZWpq6u3bt1euXPmvf/2ruMmHDBmiUCiWLVuWlpa2f//+4ODg/G0FLgAAAYxJREFUSZMmFTdyenp63759t27dmpiYmJWVFRER8dlnn/Xp06e4+ocMGZKTkzNv3rzHjx9HR0d7e3tnZmYW2bPImiMjI8ePH3/t2rWcnBwbGxv5HECRPXWfHDAUBDBQjmrUqBEYGJiWliZJkpWV1caNGxcuXNi0adMaNWp06tRJx5mYmpqOHDmydevWEydO/Pe//92uXTs7O7sjR44cO3asadOmr7zySkxMzPjx44ub3N7e/tChQ6GhoS4uLnPnzt22bVv79u1LGHnLli2nT5/u2rWro6Pj+PHjhw0btmHDhuLqt7a2PnLkyNWrV5s2bTpq1KgBAwZYWVkV2bPImlu1atW0adNhw4bVrFlz+/bt3377rSRJRfbUfXLAUJhER0e3bdtWdBkAAFQhly9f5ggYAAABCGAAAAQggAEAEIAABgBAAAIYAAABCGAAAAQggAEAEIAABgBAAAIYAAABCGAAAAQggAEAEIAABgBAAAIYAAABCGAAAAQggAEAEMBckqTLly+LLgMAgKrl/wEuw9uXIXSTogAAAABJRU5ErkJggg=="/>
</div>
</div>
</div>
</body>
</html>




Alternatively, we can examine the case where we use an informative prior `Beta(5.4,10)`.


```sas
%let a_prior_informative = 2.4;
%let b_prior_informative = 2;


proc mcmc data=tbl outpost=ex2_3 seed=23 nmc=10000 maxtune=0 statistics=none diagnostics=none monitor=(xpred p0-p5) plots=none;
    ods exclude nobs parameters;
    parm diffuse;
    beginprior;
        xpred = rand("binomial", diffuse, 5);
        p0 = (xpred le 0);
        p1 = (xpred le 1);
        p2 = (xpred le 2);
        p3 = (xpred le 3);
        p4 = (xpred le 4);
        p5 = (xpred le 5);
    endprior;
    prior diffuse ~ beta(&a_prior_informative., &b_prior_informative.);
    model y ~ binomial(n,diffuse);
run;

proc univariate data=ex2_3 outtable=ex2_3_means noprint;
    var p0 p1 p2 p3 p4 p5;
run;            /* omit VAR statement to analyze all numerical variables */

data ex2_3_means2(keep=n probability_of_success _mean_ rename=(_mean_=cumulative));
    set ex2_3_means(keep=_var_ _mean_);
    m = lag(_mean_);
    n = _n_ - 1;
    if _n_ = 1 then probability_of_success = _mean_;
    else
        probability_of_success = _mean_ - m;
        drop m;
run;

Title "Probability of n number of successful launches given informative prior";
proc print data=ex2_3_means2; run;

proc sgplot data=ex2_3_means2;
series x=n y=cumulative;
title "Cumulative Distribution Function vs. n Number of Successful Launches";
yaxis label='Probability' min=0;
xaxis label='Number of Successes';
run;
```




<!DOCTYPE html>
<html lang="en" xml:lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta charset="utf-8"/>
<meta content="SAS 9.4" name="generator"/>
<title>SAS Output</title>
<style>
/*<![CDATA[*/
.body.c > table, .body.c > pre, .body.c div > table,
.body.c div > pre, .body.c > table, .body.c > pre,
.body.j > table, .body.j > pre, .body.j div > table,
.body.j div > pre, .body.j > table, .body.j > pre,
.body.c p.note, .body.c p.warning, .body.c p.error, .body.c p.fatal,
.body.j p.note, .body.j p.warning, .body.j p.error, .body.j p.fatal,
.body.c > table.layoutcontainer, .body.j > table.layoutcontainer { margin-left: auto; margin-right: auto }
.layoutregion.l table, .layoutregion.l pre, .layoutregion.l p.note,
.layoutregion.l p.warning, .layoutregion.l p.error, .layoutregion.l p.fatal { margin-left: 0 }
.layoutregion.c table, .layoutregion.c pre, .layoutregion.c p.note,
.layoutregion.c p.warning, .layoutregion.c p.error, .layoutregion.c p.fatal { margin-left: auto; margin-right: auto }
.layoutregion.r table, .layoutregion.r pre, .layoutregion.r p.note,
.layoutregion.r table, .layoutregion.r pre, .layoutregion.r p.note,
.layoutregion.r p.warning, .layoutregion.r p.error, .layoutregion.r p.fatal { margin-right: 0 }
article, aside, details, figcaption, figure, footer, header, hgroup, nav, section { display: block }
html{ font-size: 100% }
.body { margin: 1em; font-size: 13px; line-height: 1.231 }
sup { position: relative; vertical-align: baseline; bottom: 0.25em; font-size: 0.8em }
sub { position: relative; vertical-align: baseline; top: 0.25em; font-size: 0.8em }
ul, ol { margin: 1em 0; padding: 0 0 0 40px }
dd { margin: 0 0 0 40px }
nav ul, nav ol { list-style: none; list-style-image: none; margin: 0; padding: 0 }
img { border: 0; vertical-align: middle }
svg:not(:root) { overflow: hidden }
figure { margin: 0 }
table { border-collapse: collapse; border-spacing: 0 }
.layoutcontainer { border-collapse: separate; border-spacing: 0 }
p { margin-top: 0; text-align: left }
h1.heading1 { text-align: left }
h2.heading2 { text-align: left }
h3.heading3 { text-align: left }
h4.heading4 { text-align: left }
h5.heading5 { text-align: left }
h6.heading6 { text-align: left }
span { text-align: left }
table { margin-bottom: 1em }
td, th { text-align: left; padding: 3px 6px; vertical-align: top }
td[class$="fixed"], th[class$="fixed"] { white-space: pre }
section, article { padding-top: 1px; padding-bottom: 8px }
hr.pagebreak { height: 0px; border: 0; border-bottom: 1px solid #c0c0c0; margin: 1em 0 }
.stacked-value { text-align: left; display: block }
.stacked-cell > .stacked-value, td.data > td.data, th.data > td.data, th.data > th.data, td.data > th.data, th.header > th.header { border: 0 }
.stacked-cell > div.data { border-width: 0 }
.systitleandfootercontainer { white-space: nowrap; margin-bottom: 1em }
.systitleandfootercontainer > p { margin: 0 }
.systitleandfootercontainer > p > span { display: inline-block; width: 100%; white-space: normal }
.batch { display: table }
.toc { display: none }
.proc_note_group, .proc_title_group { margin-bottom: 1em }
p.proctitle { margin: 0 }
p.note, p.warning, p.error, p.fatal { display: table }
.notebanner, .warnbanner, .errorbanner, .fatalbanner,
.notecontent, .warncontent, .errorcontent, .fatalcontent { display: table-cell; padding: 0.5em }
.notebanner, .warnbanner, .errorbanner, .fatalbanner { padding-right: 0 }
.body > div > ol li { text-align: left }
.beforecaption > h4 { margin-top: 0; margin-bottom: 0 }
.c { text-align: center }
.r { text-align: right }
.l { text-align: left }
.j { text-align: justify }
.d { text-align: right }
.b { vertical-align: bottom }
.m { vertical-align: middle }
.t { vertical-align: top }
.accessiblecaption {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
a:active { color: #800080 }
.aftercaption {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
    padding-top: 4pt;
}
.batch > colgroup {
    border-left: 1px solid #c1c1c1;
    border-right: 1px solid #c1c1c1;
}
.batch > tbody, .batch > thead, .batch > tfoot {
    border-top: 1px solid #c1c1c1;
    border-bottom: 1px solid #c1c1c1;
}
.batch { border: hidden; }
.batch {
    background-color: #fafbfe;
    border: 1px solid #c1c1c1;
    border-collapse: separate;
    border-spacing: 1px;
    color: #000000;
    font-family: 'SAS Monospace', 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    padding: 7px;
    }
.beforecaption {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.body {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    margin-left: 8px;
    margin-right: 8px;
}
.bodydate {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    text-align: right;
    vertical-align: top;
    width: 100%;
}
.bycontentfolder {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.byline {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.bylinecontainer > col, .bylinecontainer > colgroup > col, .bylinecontainer > colgroup, .bylinecontainer > tr, .bylinecontainer > * > tr, .bylinecontainer > thead, .bylinecontainer > tbody, .bylinecontainer > tfoot { border: none; }
.bylinecontainer {
    background-color: #fafbfe;
    border: none;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.caption {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.cell, .container {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.contentfolder, .contentitem {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.contentproclabel, .contentprocname {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.contents {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: decimal;
    margin-left: 8px;
    margin-right: 8px;
}
.contentsdate {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.contenttitle {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: bold;
}
.continued {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
    width: 100%;
}
.data, .dataemphasis {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.dataemphasisfixed {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.dataempty {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.datafixed {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.datastrong {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.datastrongfixed {
    background-color: #ffffff;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.date {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.document {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.errorbanner {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.errorcontent {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.errorcontentfixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.extendedpage {
    background-color: #fafbfe;
    border-style: solid;
    border-width: 1pt;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
    text-align: center;
}
.fatalbanner {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.fatalcontent {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.fatalcontentfixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.folderaction {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.footer {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.footeremphasis {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.footeremphasisfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.footerempty {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.footerfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.footerstrong {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.footerstrongfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.frame {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.graph > colgroup {
    border-left: 1px solid #c1c1c1;
    border-right: 1px solid #c1c1c1;
}
.graph > tbody, .graph > thead, .graph > tfoot {
    border-top: 1px solid #c1c1c1;
    border-bottom: 1px solid #c1c1c1;
}
.graph { border: hidden; }
.graph {
    background-color: #fafbfe;
    border: 1px solid #c1c1c1;
    border-collapse: separate;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    }
.header {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.headeremphasis {
    background-color: #d8dbd3;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.headeremphasisfixed {
    background-color: #d8dbd3;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.headerempty {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.headerfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.headersandfooters {
    background-color: #edf2f9;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.headerstrong {
    background-color: #d8dbd3;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.headerstrongfixed {
    background-color: #d8dbd3;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #000000;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.heading1, .heading2, .heading3, .heading4, .heading5, .heading6 { font-family: Arial, Helvetica, sans-serif }
.index {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.indexaction, .indexitem {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.indexprocname {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.indextitle {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: bold;
}
.layoutcontainer, .layoutregion {
    border-width: 0;
    border-spacing: 30px;
}
.linecontent {
    background-color: #fafbfe;
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
a:link { color: #0000ff }
.list {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: disc;
}
.list10 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: square;
}
.list2 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: circle;
}
.list3, .list4, .list5, .list6, .list7, .list8, .list9 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: square;
}
.listitem {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: disc;
}
.listitem10 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: square;
}
.listitem2 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: circle;
}
.listitem3, .listitem4, .listitem5, .listitem6, .listitem7, .listitem8, .listitem9 {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: square;
}
.note {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.notebanner {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.notecontent {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.notecontentfixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.output > colgroup {
    border-left: 1px solid #c1c1c1;
    border-right: 1px solid #c1c1c1;
}
.output > tbody, .output > thead, .output > tfoot {
    border-top: 1px solid #c1c1c1;
    border-bottom: 1px solid #c1c1c1;
}
.output { border: hidden; }
.output {
    background-color: #fafbfe;
    border: 1px solid #c1c1c1;
    border-collapse: separate;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    }
.pageno {
    background-color: #fafbfe;
    border-spacing: 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
    text-align: right;
    vertical-align: top;
}
.pages {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: decimal;
    margin-left: 8px;
    margin-right: 8px;
}
.pagesdate {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.pagesitem {
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    list-style-type: none;
    margin-left: 6pt;
}
.pagesproclabel, .pagesprocname {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.pagestitle {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: bold;
}
.paragraph {
    background-color: #fafbfe;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.parskip > col, .parskip > colgroup > col, .parskip > colgroup, .parskip > tr, .parskip > * > tr, .parskip > thead, .parskip > tbody, .parskip > tfoot { border: none; }
.parskip {
    border: none;
    border-spacing: 0;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
    }
.prepage {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    text-align: left;
}
.proctitle {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.proctitlefixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowfooter {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowfooteremphasis {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.rowfooteremphasisfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.rowfooterempty {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowfooterfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.rowfooterstrong {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowfooterstrongfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowheader {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowheaderemphasis {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.rowheaderemphasisfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: italic;
    font-weight: normal;
}
.rowheaderempty {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowheaderfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.rowheaderstrong {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.rowheaderstrongfixed {
    background-color: #edf2f9;
    border-color: #b0b7bb;
    border-style: solid;
    border-width: 0 1px 1px 0;
    color: #112277;
    font-family: 'Courier New', Courier, monospace;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.systemfooter, .systemfooter10, .systemfooter2, .systemfooter3, .systemfooter4, .systemfooter5, .systemfooter6, .systemfooter7, .systemfooter8, .systemfooter9 {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.systemtitle, .systemtitle10, .systemtitle2, .systemtitle3, .systemtitle4, .systemtitle5, .systemtitle6, .systemtitle7, .systemtitle8, .systemtitle9 {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size: small;
    font-style: normal;
    font-weight: bold;
}
.systitleandfootercontainer > col, .systitleandfootercontainer > colgroup > col, .systitleandfootercontainer > colgroup, .systitleandfootercontainer > tr, .systitleandfootercontainer > * > tr, .systitleandfootercontainer > thead, .systitleandfootercontainer > tbody, .systitleandfootercontainer > tfoot { border: none; }
.systitleandfootercontainer {
    background-color: #fafbfe;
    border: none;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.table > col, .table > colgroup > col {
    border-left: 1px solid #c1c1c1;
    border-right: 0 solid #c1c1c1;
}
.table > tr, .table > * > tr {
    border-top: 1px solid #c1c1c1;
    border-bottom: 0 solid #c1c1c1;
}
.table { border: hidden; }
.table {
    border-color: #c1c1c1;
    border-style: solid;
    border-width: 1px 0 0 1px;
    border-collapse: collapse;
    border-spacing: 0;
    }
.titleandnotecontainer > col, .titleandnotecontainer > colgroup > col, .titleandnotecontainer > colgroup, .titleandnotecontainer > tr, .titleandnotecontainer > * > tr, .titleandnotecontainer > thead, .titleandnotecontainer > tbody, .titleandnotecontainer > tfoot { border: none; }
.titleandnotecontainer {
    background-color: #fafbfe;
    border: none;
    border-spacing: 1px;
    color: #000000;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
    width: 100%;
}
.titlesandfooters {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.usertext {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
a:visited { color: #800080 }
.warnbanner {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: bold;
}
.warncontent {
    background-color: #fafbfe;
    color: #112277;
    font-family: Arial, 'Albany AMT', Helvetica, Helv;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
.warncontentfixed {
    background-color: #fafbfe;
    color: #112277;
    font-family: 'Courier New', Courier;
    font-size:  normal;
    font-style: normal;
    font-weight: normal;
}
/*]]>*/
</style>
</head>
<body class="l body">
<div style="padding-bottom: 8px; padding-top: 1px">
</div>
<div style="padding-bottom: 8px; padding-top: 1px">
<div id="IDX" class="systitleandfootercontainer" style="border-spacing: 1px">
<p><span class="c systemtitle">Probability of n number of successful launches given informative prior</span> </p>
</div>
<div style="padding-bottom: 8px; padding-top: 1px">
<table class="table" style="border-spacing: 0" aria-label="Data Set WORK.EX2_3_MEANS2">
<caption aria-label="Data Set WORK.EX2_3_MEANS2"></caption>
<colgroup><col/></colgroup><colgroup><col/><col/><col/></colgroup>
<thead>
<tr>
<th class="r header" scope="col">Obs</th>
<th class="r header" scope="col">cumulative</th>
<th class="r header" scope="col">n</th>
<th class="r header" scope="col">probability_of_success</th>
</tr>
</thead>
<tbody>
<tr>
<th class="r rowheader" scope="row">1</th>
<td class="r data">0.1512</td>
<td class="r data">0</td>
<td class="r data">0.1512</td>
</tr>
<tr>
<th class="r rowheader" scope="row">2</th>
<td class="r data">0.4412</td>
<td class="r data">1</td>
<td class="r data">0.2900</td>
</tr>
<tr>
<th class="r rowheader" scope="row">3</th>
<td class="r data">0.7328</td>
<td class="r data">2</td>
<td class="r data">0.2916</td>
</tr>
<tr>
<th class="r rowheader" scope="row">4</th>
<td class="r data">0.9141</td>
<td class="r data">3</td>
<td class="r data">0.1813</td>
</tr>
<tr>
<th class="r rowheader" scope="row">5</th>
<td class="r data">0.9864</td>
<td class="r data">4</td>
<td class="r data">0.0723</td>
</tr>
<tr>
<th class="r rowheader" scope="row">6</th>
<td class="r data">1.0000</td>
<td class="r data">5</td>
<td class="r data">0.0136</td>
</tr>
</tbody>
</table>
</div>
</div>
<div style="padding-bottom: 8px; padding-top: 1px">
<hr class="pagebreak"/>
<div id="IDX1" style="padding-bottom: 8px; padding-top: 1px">
<div class="c">
<img style="height: 480px; width: 640px" alt="The SGPlot Procedure" src="data:image/png;base64,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"/>
</div>
</div>
</div>
</body>
</html>




Clearly the results above are different, but how do we go about selecting the best model?

## 2.4 The Marginal Distribution of the Data and Bayes’ Factors

Recall Bayes Theorem Equation 2.6:

$$
p\left(\theta \, | \, y\right) = \frac{f\left(\textbf{y} \, | \, \theta \right) p \left( \theta \right)}{m\left(\textbf{y}\right)}
$$

where

$$
m\left(\textbf{y}\right) = \int f\left(\textbf{y} \, | \, \theta\right)p \left( \theta \right)d \theta
$$

The denominator $m\left(\textbf{y}\right)$ is little more than a normalizing constant when our intent is parameter estimation and prediction. This changes when we consider model selection.

Suppose we have two probability models $M_{1}$ and $M_{2}$ with sampling and prior distributions $f_{1} \left( y \, | \, \theta_{1}, M_{1} \right)$, $p_{1}\left( \theta_{1} \, | \, M_{1} \right)$ and $f_{2} \left( y \, | \, \theta_{2}, M_{2} \right)$, $p_{2}\left( \theta_{2} \, | \, M_{2} \right)$ are entertained as approximations to the process underlying an observed set of data $y$.

Let $\textbf{P}(M_{1})$ denote the prior probability assigned to the first model, and let $\textbf{P}(M_{2}) = 1 - \textbf{P}(M_{1})$ denote the prior probability assigned to the second model. Then the *posterior odds* that model $M_{1}$ is true are:

$$
\begin{align*}
\frac{\textbf{P}\left[M_{1} \, | \, y\right]}{\textbf{P}\left[M_{2} \, | \, y\right]} &= \frac{\textbf{P}\left(y \, | \, M_{1}\right)\textbf{P}(M_{1})}{\textbf{P}\left(y \, | \, M_{2}\right)\textbf{P}(M_{2})}\\
 &= \frac{\textbf{P}(M_{1})\int_{\Theta_{1}}f_{1} \left( y \, | \, \theta_{1}, M_{1} \right)p_{1}\left( \theta_{1} \, | \, M_{1} \right)d\theta_{1}}{\textbf{P}(M_{2})\int_{\Theta_{2}}f_{2} \left( y \, | \, \theta_{2}, M_{2} \right)p_{2}\left( \theta_{2} \, | \, M_{2} \right)d\theta_{2}}\\
 &= \frac{\textbf{P}(M_{1})}{\textbf{P}(M_{2})} \times \frac{m_{1}\left(y \, | \, M_{1}\right)}{m_{2}\left(y \, | \, M_{2}\right)} \: \: \: \: \: \: \: \: \: \: \: \: \: \: \: \: (2.10)
\end{align*}
$$

Or in plain english,

$$
\text{Posterior odds} = \text{Prior odds} \times \text{Bayes' factor}
$$

where the *Bayes' factor* is defined to be the ratio of the marginal densities of the data under the two models considered. Take note that as Bayesians, we are computing the actual odds that a model is true - this is in contrast to frequentist methods that use p-values.

***Example 2.4 Calculating the Bayes’ factor between the uniform and informative prior models for the launch vehicle data***

Let's denote the model with the diffuse prior as $M_{1}$.<br>
Let's denote the model with the informative prior as $M_{2}$.<br>

Under the uniform prior distribution, the marginal probability of observing 3 successes in 11 launches can be computed as:

$$
\begin{align*}
m_{1}\left( 3 | M_{1} \right) &= \int^{1}_{0} \binom{11}{3} \pi^{3} \left( 1 - \pi \right)^{8}d\pi\\
 &= \binom{11}{3} \frac{\Gamma(4)\Gamma(9)}{\Gamma(13)} \int^{1}_{0} \frac{\Gamma(13)}{\Gamma(4)\Gamma(9)} \pi^{4-1} \left( 1 - \pi \right)^{9-1}d\pi \\
 &= \frac{11!}{3!8!} \times \frac{3!8!}{12!} \times 1 \\
 &= \frac{1}{12} \\
 &= 0.08333
\end{align*}
$$

Intuitively, a uniform distribution places equal likelihood on all values. In this case there are $\left[ 0,11 \right]$ possible values so there is a $\frac{1}{12}$ marginal probability of any of the values occuring.

Under the informative prior distribution, the marginal probability of observing 3 successes in 11 launches can be computed as:

$$
\begin{align*}
m_{2}\left( 3 | M_{2} \right) &= \int^{1}_{0} \binom{11}{3} \pi^{3} \left( 1 - \pi \right)^{8} \pi^{2.4-1} \left( 1 - \pi \right)^{2-1}d\pi\\
 &= \binom{11}{3} \frac{\Gamma(5.4)\Gamma(10)}{\Gamma(15.4)} \int^{1}_{0} \frac{\Gamma(15.4)}{\Gamma(5.4)\Gamma(10)} \pi^{5.4-1} \left( 1 - \pi \right)^{10-1}d\pi \\
 &= \frac{11!}{3!8!} \times \frac{\Gamma(5.4)9!}{\Gamma(15.4)} \times 1 \\
 &= 0.01045
\end{align*}
$$

Thus the Bayes' factor in favor of the first model is $\frac{0.08333}{0.01045} = 7.97$ or about 8 to 1. If both models are given equal weight a priori, (i.e. $\textbf{P}(M_{1}) = \textbf{P}(M_{2}) = 0.5$), then the posterior probability that the first model is true is:

$$
\begin{align*}
\textbf{P}\left[M_{1} \, | \, y \right] &= \frac{\textbf{P}\left(y \, | \, M_{1} \right)\textbf{P}(M_{1})}{\textbf{P}\left(y \, | \, M_{1} \right)\textbf{P}(M_{1}) + \textbf{P}\left(y \, | \, M_{2} \right)\textbf{P}(M_{2})}\\
 &= \frac{\textbf{P}(M_{1})m_{1}\left(y \, | \, M_{1} \right)}{\textbf{P}(M_{1})m_{1}\left(y \, | \, M_{1} \right) + \textbf{P}(M_{2})m_{2}\left(y \, | \, M_{2} \right)}\\
 &= \frac{(0.5)(0.08333)}{(0.5)(0.08333) + (0.5)(0.01045)} \\
 &= 0.89
\end{align*}
$$

The probability 0.89 is the posterior probability that the model employing the uniform prior distribution is true, given that one of the two models is true and assuming that both models are given equal prior weight.
* This statement is fundamentally, philosophically different than frequentist hypothesis testing
    * Frequentist probability statements refer only to the probability of observing a test statistic more extreme than the one actually observed
    * Such statements do not directly address the question of whether a particular model is true

One asterisk on this approach is that Bayes' Factors are only defined when proper prior distributions are used. A *proper prior* integrates to one.

# Fin!
