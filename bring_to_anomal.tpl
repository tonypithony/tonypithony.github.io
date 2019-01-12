<body bgcolor="#FFE4C4">
<h1 align="center">Аномалии и патологии роговицы и глаза человека</h1>
<table border="2" cellpadding="10" cellspacing="0" nowrap>
<tr><th>Название</th><th>Тип мутации</th><th>Толщина</th><th>Помутнение</th><th>Причины</th></tr>
%for row in rows:
	<tr>
		%for col in row:
			<td valign="middle" align="left">{{col}}</td>
		%end
	</tr>
%end
</table> 
</body>