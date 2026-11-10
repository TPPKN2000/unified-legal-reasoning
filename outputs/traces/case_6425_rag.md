# Civil law simulation

## A.1 — rule_based

**Prompt**
```
Considering the following facts:
1. - Theo đơn khởi kiện đề ngày 12/8/2010 và đơn khởi kiện bổ sung ngày
2. 03/2/2013, các lời khai trong quá trình giải quyết vụ án nguyên đơn ông A trình
3. bày: Vào năm 1993 ông A có nhận chuyển nhượng của ông M phần đất ngang
4. 05m, dài 50m, diện tích 250m2 thuộc thửa số 07, tờ bản đồ số 35, tọa lạc tại ấp X,
5. xã Y, huyện Z, tỉnh Sóc Trăng. Đến năm 2000 phần đất trên được UBND tỉnh Sóc
6. Trăng cấp giấy chứng nhận quyền sử dụng đất số 000362 ngày 01/3/2000 có tứ
7. cận: Phía đông giáp đất hộ bà B số đo 49,7m; Phía tây giáp với đất hộ ông C số đo
8. 49,7m; Phía nam giáp với đường W số đo 5m; Phía bắc giáp với kênh thủy lợi số
9. đo 5m. Hiện tại phần đất của ông chỉ còn lại 0,4m. Phần đất bà B chồng lên đất
10. ông chiều ngang 1,2m, chiều dài 50m. Phần đất bà E chồng lên đất ông chiều
11. ngang 3m, chiều dài 50m. Còn lại 0,8m chiều ngang nằm trong giấy của bà E
12. 0,4m.
13. Nên ông A khởi kiện yêu cầu Tòa án xử buộc bà B trả lại cho ông phần đất
14. đã lấn chiếm diện tích 60m2, buộc bà E và ông C trả lại phần đất lấn chiếm 170m2.
15. Đồng thời yêu cầu hủy giấy chứng nhận quyền sử dụng đất số 0013 do UBND tỉnh
16. Sóc Trăng cấp ngày 05/10/1998 của hộ ông N nhưng đã chuyển nhượng cho bà E
17. và hủy giấy chứng nhận quyền sử dụng đất số 2713 do UBND huyện Z cấp cho
18. ông P nhưng đã chuyển nhượng cho bà B.
19. Tại phiên tòa sơ thẩm ngày 09/9/2015, ông A đã thay đổi yêu cầu khởi kiện
20. là yêu cầu bà B, ông D trả lại giá trị quyền sử dụng đất đối với diện tích theo đo
21. đạc thực tế là 62m2 và buộc ông C, bà E trả giá trị quyền sử dụng đất đối với diện
22. tích 21,1m2; đồng thời rút lại yêu cầu hủy các giấy chứng nhận quyền sử dụng đất
23. nêu trên.
24. - Theo các lời khai trong quá trình giải quyết vụ án bị đơn bà B (đồng thời
25. là người đại diện hợp pháp của người có quyền lợi, nghĩa vụ liên quan ông D)
26. trình bày: Vào năm 2007, ông D và bà B có nhận chuyển nhượng của bà O phần
27. đất diện tích 272,7m2 thuộc thửa số 35, tờ bản đồ số 63, tọa lạc tại ấp X, xã Y,
28. huyện Z, tỉnh Sóc Trăng. Ông bà đã được UBND huyện Z cấp giấy chứng nhận
29. quyền sử dụng đất số AL 687167 vào năm 2008. Ông bà không đồng ý với yêu cầu
30. khởi kiện của ông A vì ông bà không có lấn chiếm đất của ông A.
31. - Theo các lời khai trong quá trình giải quyết vụ án bị đơn ông C và người
32. có quyền lợi, nghĩa vụ liên quan bà E trình bày: Vào năm 2007, ông C và bà E có
33. nhận chuyển nhượng của ông R phần đất diện tích 400m2 thuộc thửa số 970, tờ bản
34. đồ số 5, tọa lạc tại ấp X, xã Y, huyện Z, tỉnh Sóc Trăng. Thửa đất trên UBND
35. huyện Z cấp giấy chứng nhận quyền sử dụng đất số 0013 cho hộ ông N vào ngày
36. 05/10/1998 đến tháng 10/2007 đã chuyển tên cho bà E. Ông bà không đồng ý với
37. yêu cầu khởi kiện của ông A vì ông bà không có lấn chiếm đất của ông A. Nếu
38. việc cấp đất có chồng lấn là trách nhiệm của cơ quan Nhà nước.
39. - Tại văn bản số 160/UBND-TD ngày 12/02/2015, người có quyền lợi, nghĩa
40. vụ liên quan Ủy ban nhân dân tỉnh Sóc Trăng trình bày: Đối với việc hợp thức hóa
41. quyền sử dụng đất cho ông N, ngày 19/10/1993 UBND huyện Z ban hành Quyết
42. định số 638/QĐ.UBTX.93 về việc tạm cấp 150m2 đất (chiều ngang 5m, chiều dài
43. 30m) cho ông N, nhưng thực tế ông N sử dụng diện tích 400m2 (chiền ngang 8m,
44. chiều dài 50m), dư 250m2. Theo công văn số 1132/CV.HC.97 ngày 26/11/1997
45. của Chủ tịch UBND tỉnh Sóc Trăng chấp nhận hợp thức hóa cho các hộ gia đình và
46. cá nhân được UBND huyện Z cấp đất hoặc chuyển nhượng đất của các hộ được
47. cấp đất có số đo và diện tích dư ra so với quyết định cấp đất và đã nộp tiền sử dụng
48. diện tích đất dư. Năm 1998, ông N đăng ký xin cấp giấy chứng nhận quyền sử
49. dụng đất diện tích 400m2 (trong đó có phần đất dư 250m2) và ông đã nộp tiền sử
50. dụng đất tại Cục thuế tỉnh Sóc Trăng vào ngày 03/01/1997. Ngày 02/10/1998,
51. UBND tỉnh Sóc Trăng cấp giấy chứng nhận quyền sử dụng đất cho ông N, số I -
52. 195964, thuộc thửa 970, tờ bản đồ số 05, diện tích 400m2. Ngày 18/01/2005, ông N
53. chuyển nhượng diện tích 400m2 cho ông R sử dụng. Năm 2007, ông R chuyển
54. nhượng hết thửa cho ông C và bà E sử dụng đến nay.
55. Đối với phần đất cấp cho ông M, sau này chuyển nhượng cho ông A. Ngày
56. 19/10/1993, UBND huyện Z ban hành Quyết định số 639/QĐ.UBTX.93 về việc
57. tạm cấp 150m2 đất (chiều ngang 5m, chiều dài 30m), tọa lạc tại ấp X, xã Y, huyện
58. Z, tỉnh Sóc Trăng cho ông M nhưng thực tế ông M sử dụng diện tích 250m2 (chiều
59. ngang 5m, chiều dài 50m), dư 100m2.
60. Ngày 26/11/1997, Chủ tịch UBND tỉnh Sóc Trăng có công văn số
61. 1132/CV.HC.97 chấp nhận hợp thức hóa cho các hộ gia đình và cá nhân được
62. UBND huyện Z cấp đất hoặc chuyển nhượng đất của các hộ được cấp đất có số đo
63. và diện tích dư ra so với quyết định cấp đất và đã nộp tiền sử dụng diện tích đất dư.
64. Năm 1998, ông M đăng ký xin cấp giấy chứng nhận quyền sử dụng đất
65. 250m2 (trong đó có phần đất dư là 100m2) ông M đã nộp tiền sử dụng đất tại Cục
66. thuế tỉnh Sóc Trăng ngày 31/8/1998. Ngày 12/10/1998, UBND tỉnh Sóc Trăng cấp
67. giấy chứng nhận quyền sử dụng đất cho ông M số M 828092, thuộc thửa 971, tờ
68. bản đồ số 5, diện tích 250m2. Năm 1999 ông M chuyển nhượng quyền sử dụng đất
69. 250m2 trên cho ông A. Ngày 01/3/2000 UBND tỉnh Sóc Trăng cấp giấy chứng
70. nhận quyền sử dụng đất cho ông A, diện tích 250m2, thuộc thửa số 7, tờ bản đồ số
71. 35.
72. Ngày 21/10/2003, UBND tỉnh Sóc Trăng ban hành Quyết định số
73. 1439/QĐ.HC.03 cấp diện tích 264m2 (chiều ngang 5,5m, chiều dài 48m), thửa số
74. 63, tờ bản đồ số 35, tọa lạc tại ấp X, xã Y, huyện Z, tỉnh Sóc Trăng cho ông P.
75. Ngày 26/10/2003, Sở Địa chính tỉnh Sóc Trăng (nay là Sở Tài nguyên và
76. Môi trường) có biên bản bàn giao đất cho ông P, diện tích 264m2.
77. Năm 2003, ông P đăng ký xin cấp giấy chứng nhận quyền sử dụng đất diện
78. tích 272,7m2 (chiều ngang trước giáp đường W 5,50m, chiều ngang sau giáp
79. mương nước 5,49m, chiều dài một cạnh là 49,74m và một cạnh là 49,71m) tăng
80. diện tích 8,7m2 so với quyết định cấp đất, diện tích 272,7m2 ông P đã nộp tiền sử
81. dụng đất tại Kho bạc tỉnh Sóc Trăng ngày 07/01/2004.
82. Ngày 16/3/2004, ông P chuyển nhượng diện tích 272,7m2 cho bà O (có xác
83. nhận của UBND xã Y).
84. Ngày 25/12/2007, bà O chuyển nhượng diện tích 272,7m2 cho bà B (có xác
85. nhận của UBND xã Y).
86. Ngày 10/3/2008, UBND huyện Z cấp giấy chứng nhận quyền sử dụng đất
87. trên cho bà B, giấy mang số AL 687167, thuộc thửa 63, tờ bản đồ số 35, diện tích
88. 272,7m2.
89. Qua xác định phần đất bà B hiện nay có một phần chồng và một phần lấn
90. qua đất của ông A, cụ thể như sau:
91. UBND tỉnh Sóc Trăng cấp đất cho ông P chồng lên phần đất của ông A diện
92. tích 166,9m2 hiện nay bà B đã cất nhà trọ.
93. Bà B sử dụng đất lấn qua đất ông A diện tích 62m2 (chiều ngang giáp đường
94. W 1,20m, chiều ngang sau 1,39m, chiều dài 49,75m), bà B sử dụng lối đi vào nhà
95. trọ.
96. Ông C và bà E đang sử dụng lấn sang thửa đất của ông A diện tích (0,35 +
97. 0,5 x 49,73m) = 21,1m2 (Kèm theo sơ đồ hiện trạng sử dụng đất, do Văn phòng
98. đăng ký quyền sử dụng đất tỉnh thiết lập ngày 07/8/2014).
99. * Sự việc được Tòa án nhân dân tỉnh Sóc Trăng thụ lý, giải quyết. Tại bản án
100. dân sự sơ thẩm số 19/2015/DS-ST, ngày 09/9/2015 đã quyết định áp dụng khoản 7
101. Điều 25, khoản 1 và 2 Điều 32a, điểm a khoản 1 Điều 34, khoản 1 Điều 131, Điều
102. 141, Điều 142, khoản 1 Điều 199, Điều 217, khoản 1 Điều 218, Điều 245 và Điều
103. 250 của Bộ luật tố tụng dân sự năm 2004 sửa đổi, bổ sung năm 2011; Khoản 1
104. Điều 203 Luật đất đai năm 2013; Pháp lệnh số 10/2009/UBTVQH12 ngày
105. 27/12/2009 của Quốc hội về án phí, lệ phí Tòa án. Tuyên xử:
106. 1. Đình chỉ việc giải quyết đối với yêu cầu hủy giấy chứng nhận quyền sử
107. dụng đất của nguyên đơn ông A, về việc yêu cầu hủy Giấy chứng nhận quyền sử
108. dụng đất số I - 195964 của UBND tỉnh Sóc Trăng cấp ngày 05/10/1998 cho hộ ông
109. N và Giấy chứng nhận quyền sử dụng đất số 2713 của UBND huyện Z cấp ngày
110. 16/3/2004 cho hộ ông P.
111. 2. Chấp nhận yêu cầu khởi kiện của nguyên đơn ông A về việc yêu cầu các
112. bị đơn bà B, ông C và người có quyền lợi, nghĩa vụ liên quan ông D, bà E hoàn trả
113. giá trị quyền sử dụng đất đã lấn chiếm và UBND tỉnh Sóc Trăng bồi hoàn giá trị
114. quyền sử dụng đất đã cấp đất cho ông P chồng lấn lên đất ông A bị mất.
115. Buộc UBND tỉnh Sóc Trăng có trách nhiệm bồi hoàn cho ông A diện tích
116. đất chồng lấn bị mất 166,9m2, tại thửa đất số 07, tờ bản đồ số 35, tọa lạc tại ấp X,
117. xã Y, huyện Z, tỉnh Sóc Trăng với số tiền 584.150.000đồng.
118. Buộc ông C và bà E có trách nhiệm hoàn trả cho ông A giá trị diện tích đất
119. đã lấn chiếm 21,1m2, tại thửa đất số 07, tờ bản đồ số 35, tọa lạc tại ấp X, xã Y,
120. huyện Z, tỉnh Sóc Trăng với số tiền 73.850.000đồng.
121. Buộc bà B và ông D có trách nhiệm hoàn trả cho ông A giá trị diện tích đất
122. đã lấn chiếm 62m2, tại thửa đất số 07, tờ bản đồ số 35, tọa lạc tại ấp X, xã Y, huyện
123. Z, tỉnh Sóc Trăng với số tiền 217.000.000đồng.
124. Sau khi bản án có hiệu lực pháp luật và có đơn yêu cầu thi hành án, UBND
125. tỉnh Sóc Trăng, ông C, bà E, bà B và ông D còn phải chịu lãi suất cơ bản do Ngân
126. hàng Nhà nước Việt Nam công bố, tương ứng với số tiền và thời gian chậm thanh
127. toán.
128. 3. Ông C và bà E được quyền sử dụng diện tích đất 21,1m2, tại thửa đất số
129. 07, tờ bản đồ số 35, tọa lạc tại ấp X, xã Y, huyện Z, tỉnh Sóc Trăng do ông A đứng
130. tên giấy chứng nhận quyền sử dụng đất. (có tuyên tứ cận kèm theo)
131. 4. Bà B và ông D được quyền sử dụng diện tích đất 62m2, tại thửa đất số 07,
132. tờ bản đồ số 35, tọa lạc tại ấp X, xã Y, huyện Z, tỉnh Sóc Trăng do ông A đứng tên
133. giấy chứng nhận quyền sử dụng đất. (có tuyên tứ cận kèm theo)
134. Sau khi bản án có hiệu lực pháp luật ông C, bà E, bà B và ông D tự kê khai,
135. làm thủ tục xin cấp giấy chứng nhận quyền sử dụng đất theo quy định của pháp
136. luật đối với diện tích đất được giao nêu trên.
137. Ngoài ra, bản án sơ thẩm còn tuyên về án phí sơ thẩm, chi phí thẩm định,
138. định giá và thông báo quyền kháng cáo cho các đương sự theo quy định pháp luật.
139. * Sau khi xét xử sơ thẩm, bị đơn bà B và người có quyền lợi, nghĩa vụ liên
140. quan UBND tỉnh Sóc Trăng có kháng cáo, Viện trưởng Viện kiểm sát nhân dân
141. cấp cao tại thành phố Hồ Chí Minh có kháng nghị bản án dân sự sơ thẩm nên sự
142. việc được Tòa án nhân dân cấp cao tại thành phố Hồ Chí Minh thụ lý, giải quyết.
143. Tại Bản án dân sự phúc thẩm số 37/2017/DS-PT, ngày 30/3/2017 đã quyết định
144. căn cứ khoản 3 Điều 308 Bộ luật tố tụng dân sự: Chấp nhận kháng cáo của bị đơn
145. bà B và người có quyền lợi, nghĩa vụ liên quan UBND tỉnh Sóc Trăng và kháng
146. nghị của Viện trưởng Viện kiểm sát nhân dân cấp cao tại thành phố Hồ Chí Minh.
147. Hủy bản án dân sự sơ thẩm số 19/2015/DS-ST, ngày 09/9/2015 của Tòa án nhân
148. dân tỉnh Sóc Trăng và chuyển hồ sơ về cho Tòa án cấp sơ thẩm giải quyết lại vụ án
149. theo thủ tục sơ thẩm.
150. - Theo đơn khởi kiện (v/v yêu cầu Tòa án tiếp tục xét xử vụ án) đề ngày
151. 10/5/2017, biên bản lấy lời khai ngày 15/6/2017 và đơn khởi kiện (sửa đổi, bổ
152. sung) đề ngày 13/7/2017, nguyên đơn ông A trình bày: Ông A xác định hiện nay
153. ông yêu cầu Tòa án giải quyết: Buộc bà B, ông D trả lại cho ông giá trị phần đất
154. lấn chiếm diện tích 62m2 (chiều ngang trước 1,2m, chiều ngang sau 1,3m, chiều
155. dài 49,35m) và giá trị phần đất UBND tỉnh Sóc Trăng đã cấp giấy chứng nhận
156. quyền sử dụng đất chồng lên đất của ông diện tích 166,9m2; buộc ông C, bà E trả
157. lại cho ông giá trị phần đất lấn chiếm diện tích 21,1m2; ông yêu cầu trả giá trị đất
158. theo giá Nhà nước quy định tại thời điểm xét xử sơ thẩm, không yêu cầu trả đất.
159. * Tại phiên tòa sơ thẩm, người đại diện hợp pháp của nguyên đơn ông A giữ
160. nguyên yêu cầu khởi kiện. Các đương sự không tự thỏa thuận được với nhau về
161. việc giải quyết vụ án.
162. * Kiểm sát viên phát biểu ý kiến Viện kiểm sát về việc tuân thủ và chấp
163. hành pháp luật tố tụng của Thẩm phán, Hội đồng xét xử, người tiến hành tố tụng
164. và người tham gia tố tụng trong quá trình giải quyết vụ án trong giai đoạn xét xử
165. sơ thẩm, kể từ khi thụ lý vụ án cho đến trước thời điểm Hội đồng xét xử nghị án.
166. Đồng thời, phát biểu về tính có căn cứ và hợp pháp của việc khởi kiện, về quan
167. điểm đường lối giải quyết vụ án, đề nghị Hội đồng xét xử giải quyết vụ án theo
168. hướng chấp nhận một phần yêu cầu khởi kiện của ông A, buộc bà B, ông D trả lại
169. cho ông A phần đất lấn chiếm diện tích 62m2 và buộc ông C, bà E trả lại cho ông A
170. giá trị phần đất lấn chiếm diện tích 21,1m2; đối với yêu cầu khởi kiện của ông A về
171. việc yêu cầu bà B, ông D trả lại giá trị phần đất UBND tỉnh Sóc Trăng đã cấp giấy
172. chứng nhận quyền sử dụng đất chồng lên đất của ông A diện tích 166,9m2 thì đề
173. nghị tách ra giải quyết trong vụ án khác khi ông A có yêu cầu.
Considering the following rules: Applicable provisions of Vietnamese law:
1. [BLDS 2015] Điều 175. Ranh giới giữa các bất động sản. 1. Ranh giới giữa các bất động sản liền kề được xác định theo thoả thuận hoặc theo quyết định của cơ quan nhà nước có thẩm quyền. Ranh giới cũng có thể được xác định theo tập quán hoặc theo ranh giới đã tồn tại từ 30 năm trở lên mà không có tranh chấp. Không được lấn, chiếm, thay đổi mốc giới ngăn cách, kể cả trường hợp ranh giới là kênh, mương, hào, rãnh, bờ ruộng. Mọi chủ thể có nghĩa vụ tôn trọng, duy trì ranh giới chung. 2. Người sử dụng đất được sử dụng không gian và lòng đất theo chiều thẳng đứng từ ranh giới của thửa đất phù hợp với quy định của pháp luật và không được làm ảnh hưởng đến việc sử dụng đất của người khác. Người sử dụng đất chỉ được trồng 
2. [BLDS 2015] Điều 325. Thế chấp quyền sử dụng đất mà không thế chấp tài sản gắn liền với đất. 1. Trường hợp thế chấp quyền sử dụng đất mà không thế chấp tài sản gắn liền với đất và người sử dụng đất đồng thời là chủ sở hữu tài sản gắn liền với đất thì tài sản được xử lý bao gồm cả tài sản gắn liền với đất, trừ trường hợp có thỏa thuận khác. 2. Trường hợp thế chấp quyền sử dụng đất mà người sử dụng đất không đồng thời là chủ sở hữu tài sản gắn liền với đất thì khi xử lý quyền sử dụng đất, chủ sở hữu tài sản gắn liền với đất được tiếp tục sử dụng đất trong phạm vi quyền, nghĩa vụ của mình; quyền và nghĩa vụ của bên thế chấp trong mối quan hệ với chủ sở hữu tài sản gắn liền với đất được chuyển giao cho người nhận chu
3. [BLDS 2015] Điều 326. Thế chấp tài sản gắn liền với đất mà không thế chấp quyền sử dụng đất. 1. Trường hợp chỉ thế chấp tài sản gắn liền với đất mà không thế chấp quyền sử dụng đất và chủ sở hữu tài sản gắn liền với đất đồng thời là người sử dụng đất thì tài sản được xử lý bao gồm cả quyền sử dụng đất, trừ trường hợp có thỏa thuận khác. 2. Trường hợp chỉ thế chấp tài sản gắn liền với đất mà không thế chấp quyền sử dụng đất và chủ sở hữu tài sản gắn liền với đất không đồng thời là người sử dụng đất thì khi xử lý tài sản gắn liền với đất, người nhận chuyển quyền sở hữu tài sản gắn liền với đất được tiếp tục sử dụng đất trong phạm vi quyền, nghĩa vụ của chủ sở hữu tài sản gắn liền với đất được chuyển giao, trừ trườn
4. [BLDS 2015] Điều 501. Nội dung của hợp đồng về quyền sử dụng đất. 1. Quy định chung về hợp đồng và nội dung của hợp đồng thông dụng có liên quan trong Bộ luật này cũng được áp dụng với hợp đồng về quyền sử dụng đất, trừ trường hợp pháp luật có quy định khác. 2. Nội dung của hợp đồng về quyền sử dụng đất không được trái với quy định về mục đích sử dụng, thời hạn sử dụng đất, quy hoạch, kế hoạch sử dụng đất và các quyền, nghĩa vụ khác theo quy định của pháp luật về đất đai và quy định khác của pháp luật có liên quan
5. [BLDS 2015] Điều 502. Hình thức, thủ tục thực hiện hợp đồng về quyền sử dụng đất. 1. Hợp đồng về quyền sử dụng đất phải được lập thành văn bản theo hình thức phù hợp với quy định của Bộ luật này, pháp luật về đất đai và quy định khác của pháp luật có liên quan. 2. Việc thực hiện hợp đồng về quyền sử dụng đất phải đúng trình tự, thủ tục theo quy định của pháp luật về đất đai và quy định khác của pháp luật có liên quan
According to the given rules, please evaluate whether the court accepts the plaintiff's claims in whole or in part.
```
**Response**
```
Để đánh giá xem Tòa án đã chấp nhận yêu cầu của nguyên đơn trong toàn bộ hay một phần, chúng ta cần phân tích từng yêu cầu khởi kiện của ông A:

1. Yêu cầu thứ nhất: Buộc bà B, ông D trả lại cho ông A giá trị phần đất lấn chiếm diện tích 62m2.
   - Theo bản án sơ thẩm, yêu cầu này đã được chấp nhận. Tòa án đã tuyên buộc bà B và ông D trả lại cho ông A giá trị đất lấn chiếm 62m2.

2. Yêu cầu thứ hai: Buộc ông C, bà E trả lại cho ông A giá trị phần đất lấn chiếm diện tích 21,1m2.
   - Theo bản án sơ thẩm, yêu cầu này cũng đã được chấp nhận. Tòa án đã tuyên buộc ông C và bà E trả lại cho ông A giá trị đất lấn chiếm 21,1m2.

3. Yêu cầu thứ ba: Buộc UBND tỉnh Sóc Trăng bồi hoàn cho ông A diện tích đất chồng lấn bị mất 166,9m2.
   - Theo bản án sơ thẩm, yêu cầu này cũng đã được chấp nhận. Tòa án đã tuyên buộc UBND tỉnh Sóc Trăng bồi hoàn cho ông A diện tích đất chồng lấn bị mất 166,9m2.

4. Yêu cầu thứ tư: Buộc UBND tỉnh Sóc Trăng bồi hoàn cho ông A giá trị đất đã lấn chiếm 166,9m2 theo giá Nhà nước quy định tại thời điểm xét xử sơ thẩm.
   - Theo bản án sơ thẩm, yêu cầu này đã được chấp nhận. Tòa án tuyên buộc UBND tỉnh Sóc Trăng bồi hoàn cho ông A giá trị đất lấn chiếm 166,9m2 theo giá Nhà nước quy định tại thời điểm xét xử sơ thẩm.

Từ phân tích trên, tất cả các yêu cầu khởi kiện của ông A đều được Tòa án chấp nhận. 

Yêu cầu của nguyên đơn được chấp nhận (toàn bộ).
```

## A.2#1 — abductive (defendant)

**Prompt**
```
Considering the following facts:
1. - Theo đơn khởi kiện đề ngày 12/8/2010 và đơn khởi kiện bổ sung ngày
2. 03/2/2013, các lời khai trong quá trình giải quyết vụ án nguyên đơn ông A trình
3. bày: Vào năm 1993 ông A có nhận chuyển nhượng của ông M phần đất ngang
4. 05m, dài 50m, diện tích 250m2 thuộc thửa số 07, tờ bản đồ số 35, tọa lạc tại ấp X,
5. xã Y, huyện Z, tỉnh Sóc Trăng. Đến năm 2000 phần đất trên được UBND tỉnh Sóc
6. Trăng cấp giấy chứng nhận quyền sử dụng đất số 000362 ngày 01/3/2000 có tứ
7. cận: Phía đông giáp đất hộ bà B số đo 49,7m; Phía tây giáp với đất hộ ông C số đo
8. 49,7m; Phía nam giáp với đường W số đo 5m; Phía bắc giáp với kênh thủy lợi số
9. đo 5m. Hiện tại phần đất của ông chỉ còn lại 0,4m. Phần đất bà B chồng lên đất
10. ông chiều ngang 1,2m, chiều dài 50m. Phần đất bà E chồng lên đất ông chiều
11. ngang 3m, chiều dài 50m. Còn lại 0,8m chiều ngang nằm trong giấy của bà E
12. 0,4m.
13. Nên ông A khởi kiện yêu cầu Tòa án xử buộc bà B trả lại cho ông phần đất
14. đã lấn chiếm diện tích 60m2, buộc bà E và ông C trả lại phần đất lấn chiếm 170m2.
15. Đồng thời yêu cầu hủy giấy chứng nhận quyền sử dụng đất số 0013 do UBND tỉnh
16. Sóc Trăng cấp ngày 05/10/1998 của hộ ông N nhưng đã chuyển nhượng cho bà E
17. và hủy giấy chứng nhận quyền sử dụng đất số 2713 do UBND huyện Z cấp cho
18. ông P nhưng đã chuyển nhượng cho bà B.
19. Tại phiên tòa sơ thẩm ngày 09/9/2015, ông A đã thay đổi yêu cầu khởi kiện
20. là yêu cầu bà B, ông D trả lại giá trị quyền sử dụng đất đối với diện tích theo đo
21. đạc thực tế là 62m2 và buộc ông C, bà E trả giá trị quyền sử dụng đất đối với diện
22. tích 21,1m2; đồng thời rút lại yêu cầu hủy các giấy chứng nhận quyền sử dụng đất
23. nêu trên.
24. - Theo các lời khai trong quá trình giải quyết vụ án bị đơn bà B (đồng thời
25. là người đại diện hợp pháp của người có quyền lợi, nghĩa vụ liên quan ông D)
26. trình bày: Vào năm 2007, ông D và bà B có nhận chuyển nhượng của bà O phần
27. đất diện tích 272,7m2 thuộc thửa số 35, tờ bản đồ số 63, tọa lạc tại ấp X, xã Y,
28. huyện Z, tỉnh Sóc Trăng. Ông bà đã được UBND huyện Z cấp giấy chứng nhận
29. quyền sử dụng đất số AL 687167 vào năm 2008. Ông bà không đồng ý với yêu cầu
30. khởi kiện của ông A vì ông bà không có lấn chiếm đất của ông A.
31. - Theo các lời khai trong quá trình giải quyết vụ án bị đơn ông C và người
32. có quyền lợi, nghĩa vụ liên quan bà E trình bày: Vào năm 2007, ông C và bà E có
33. nhận chuyển nhượng của ông R phần đất diện tích 400m2 thuộc thửa số 970, tờ bản
34. đồ số 5, tọa lạc tại ấp X, xã Y, huyện Z, tỉnh Sóc Trăng. Thửa đất trên UBND
35. huyện Z cấp giấy chứng nhận quyền sử dụng đất số 0013 cho hộ ông N vào ngày
36. 05/10/1998 đến tháng 10/2007 đã chuyển tên cho bà E. Ông bà không đồng ý với
37. yêu cầu khởi kiện của ông A vì ông bà không có lấn chiếm đất của ông A. Nếu
38. việc cấp đất có chồng lấn là trách nhiệm của cơ quan Nhà nước.
39. - Tại văn bản số 160/UBND-TD ngày 12/02/2015, người có quyền lợi, nghĩa
40. vụ liên quan Ủy ban nhân dân tỉnh Sóc Trăng trình bày: Đối với việc hợp thức hóa
41. quyền sử dụng đất cho ông N, ngày 19/10/1993 UBND huyện Z ban hành Quyết
42. định số 638/QĐ.UBTX.93 về việc tạm cấp 150m2 đất (chiều ngang 5m, chiều dài
43. 30m) cho ông N, nhưng thực tế ông N sử dụng diện tích 400m2 (chiền ngang 8m,
44. chiều dài 50m), dư 250m2. Theo công văn số 1132/CV.HC.97 ngày 26/11/1997
45. của Chủ tịch UBND tỉnh Sóc Trăng chấp nhận hợp thức hóa cho các hộ gia đình và
46. cá nhân được UBND huyện Z cấp đất hoặc chuyển nhượng đất của các hộ được
47. cấp đất có số đo và diện tích dư ra so với quyết định cấp đất và đã nộp tiền sử dụng
48. diện tích đất dư. Năm 1998, ông N đăng ký xin cấp giấy chứng nhận quyền sử
49. dụng đất diện tích 400m2 (trong đó có phần đất dư 250m2) và ông đã nộp tiền sử
50. dụng đất tại Cục thuế tỉnh Sóc Trăng vào ngày 03/01/1997. Ngày 02/10/1998,
51. UBND tỉnh Sóc Trăng cấp giấy chứng nhận quyền sử dụng đất cho ông N, số I -
52. 195964, thuộc thửa 970, tờ bản đồ số 05, diện tích 400m2. Ngày 18/01/2005, ông N
53. chuyển nhượng diện tích 400m2 cho ông R sử dụng. Năm 2007, ông R chuyển
54. nhượng hết thửa cho ông C và bà E sử dụng đến nay.
55. Đối với phần đất cấp cho ông M, sau này chuyển nhượng cho ông A. Ngày
56. 19/10/1993, UBND huyện Z ban hành Quyết định số 639/QĐ.UBTX.93 về việc
57. tạm cấp 150m2 đất (chiều ngang 5m, chiều dài 30m), tọa lạc tại ấp X, xã Y, huyện
58. Z, tỉnh Sóc Trăng cho ông M nhưng thực tế ông M sử dụng diện tích 250m2 (chiều
59. ngang 5m, chiều dài 50m), dư 100m2.
60. Ngày 26/11/1997, Chủ tịch UBND tỉnh Sóc Trăng có công văn số
61. 1132/CV.HC.97 chấp nhận hợp thức hóa cho các hộ gia đình và cá nhân được
62. UBND huyện Z cấp đất hoặc chuyển nhượng đất của các hộ được cấp đất có số đo
63. và diện tích dư ra so với quyết định cấp đất và đã nộp tiền sử dụng diện tích đất dư.
64. Năm 1998, ông M đăng ký xin cấp giấy chứng nhận quyền sử dụng đất
65. 250m2 (trong đó có phần đất dư là 100m2) ông M đã nộp tiền sử dụng đất tại Cục
66. thuế tỉnh Sóc Trăng ngày 31/8/1998. Ngày 12/10/1998, UBND tỉnh Sóc Trăng cấp
67. giấy chứng nhận quyền sử dụng đất cho ông M số M 828092, thuộc thửa 971, tờ
68. bản đồ số 5, diện tích 250m2. Năm 1999 ông M chuyển nhượng quyền sử dụng đất
69. 250m2 trên cho ông A. Ngày 01/3/2000 UBND tỉnh Sóc Trăng cấp giấy chứng
70. nhận quyền sử dụng đất cho ông A, diện tích 250m2, thuộc thửa số 7, tờ bản đồ số
71. 35.
72. Ngày 21/10/2003, UBND tỉnh Sóc Trăng ban hành Quyết định số
73. 1439/QĐ.HC.03 cấp diện tích 264m2 (chiều ngang 5,5m, chiều dài 48m), thửa số
74. 63, tờ bản đồ số 35, tọa lạc tại ấp X, xã Y, huyện Z, tỉnh Sóc Trăng cho ông P.
75. Ngày 26/10/2003, Sở Địa chính tỉnh Sóc Trăng (nay là Sở Tài nguyên và
76. Môi trường) có biên bản bàn giao đất cho ông P, diện tích 264m2.
77. Năm 2003, ông P đăng ký xin cấp giấy chứng nhận quyền sử dụng đất diện
78. tích 272,7m2 (chiều ngang trước giáp đường W 5,50m, chiều ngang sau giáp
79. mương nước 5,49m, chiều dài một cạnh là 49,74m và một cạnh là 49,71m) tăng
80. diện tích 8,7m2 so với quyết định cấp đất, diện tích 272,7m2 ông P đã nộp tiền sử
81. dụng đất tại Kho bạc tỉnh Sóc Trăng ngày 07/01/2004.
82. Ngày 16/3/2004, ông P chuyển nhượng diện tích 272,7m2 cho bà O (có xác
83. nhận của UBND xã Y).
84. Ngày 25/12/2007, bà O chuyển nhượng diện tích 272,7m2 cho bà B (có xác
85. nhận của UBND xã Y).
86. Ngày 10/3/2008, UBND huyện Z cấp giấy chứng nhận quyền sử dụng đất
87. trên cho bà B, giấy mang số AL 687167, thuộc thửa 63, tờ bản đồ số 35, diện tích
88. 272,7m2.
89. Qua xác định phần đất bà B hiện nay có một phần chồng và một phần lấn
90. qua đất của ông A, cụ thể như sau:
91. UBND tỉnh Sóc Trăng cấp đất cho ông P chồng lên phần đất của ông A diện
92. tích 166,9m2 hiện nay bà B đã cất nhà trọ.
93. Bà B sử dụng đất lấn qua đất ông A diện tích 62m2 (chiều ngang giáp đường
94. W 1,20m, chiều ngang sau 1,39m, chiều dài 49,75m), bà B sử dụng lối đi vào nhà
95. trọ.
96. Ông C và bà E đang sử dụng lấn sang thửa đất của ông A diện tích (0,35 +
97. 0,5 x 49,73m) = 21,1m2 (Kèm theo sơ đồ hiện trạng sử dụng đất, do Văn phòng
98. đăng ký quyền sử dụng đất tỉnh thiết lập ngày 07/8/2014).
99. * Sự việc được Tòa án nhân dân tỉnh Sóc Trăng thụ lý, giải quyết. Tại bản án
100. dân sự sơ thẩm số 19/2015/DS-ST, ngày 09/9/2015 đã quyết định áp dụng khoản 7
101. Điều 25, khoản 1 và 2 Điều 32a, điểm a khoản 1 Điều 34, khoản 1 Điều 131, Điều
102. 141, Điều 142, khoản 1 Điều 199, Điều 217, khoản 1 Điều 218, Điều 245 và Điều
103. 250 của Bộ luật tố tụng dân sự năm 2004 sửa đổi, bổ sung năm 2011; Khoản 1
104. Điều 203 Luật đất đai năm 2013; Pháp lệnh số 10/2009/UBTVQH12 ngày
105. 27/12/2009 của Quốc hội về án phí, lệ phí Tòa án. Tuyên xử:
106. 1. Đình chỉ việc giải quyết đối với yêu cầu hủy giấy chứng nhận quyền sử
107. dụng đất của nguyên đơn ông A, về việc yêu cầu hủy Giấy chứng nhận quyền sử
108. dụng đất số I - 195964 của UBND tỉnh Sóc Trăng cấp ngày 05/10/1998 cho hộ ông
109. N và Giấy chứng nhận quyền sử dụng đất số 2713 của UBND huyện Z cấp ngày
110. 16/3/2004 cho hộ ông P.
111. 2. Chấp nhận yêu cầu khởi kiện của nguyên đơn ông A về việc yêu cầu các
112. bị đơn bà B, ông C và người có quyền lợi, nghĩa vụ liên quan ông D, bà E hoàn trả
113. giá trị quyền sử dụng đất đã lấn chiếm và UBND tỉnh Sóc Trăng bồi hoàn giá trị
114. quyền sử dụng đất đã cấp đất cho ông P chồng lấn lên đất ông A bị mất.
115. Buộc UBND tỉnh Sóc Trăng có trách nhiệm bồi hoàn cho ông A diện tích
116. đất chồng lấn bị mất 166,9m2, tại thửa đất số 07, tờ bản đồ số 35, tọa lạc tại ấp X,
117. xã Y, huyện Z, tỉnh Sóc Trăng với số tiền 584.150.000đồng.
118. Buộc ông C và bà E có trách nhiệm hoàn trả cho ông A giá trị diện tích đất
119. đã lấn chiếm 21,1m2, tại thửa đất số 07, tờ bản đồ số 35, tọa lạc tại ấp X, xã Y,
120. huyện Z, tỉnh Sóc Trăng với số tiền 73.850.000đồng.
121. Buộc bà B và ông D có trách nhiệm hoàn trả cho ông A giá trị diện tích đất
122. đã lấn chiếm 62m2, tại thửa đất số 07, tờ bản đồ số 35, tọa lạc tại ấp X, xã Y, huyện
123. Z, tỉnh Sóc Trăng với số tiền 217.000.000đồng.
124. Sau khi bản án có hiệu lực pháp luật và có đơn yêu cầu thi hành án, UBND
125. tỉnh Sóc Trăng, ông C, bà E, bà B và ông D còn phải chịu lãi suất cơ bản do Ngân
126. hàng Nhà nước Việt Nam công bố, tương ứng với số tiền và thời gian chậm thanh
127. toán.
128. 3. Ông C và bà E được quyền sử dụng diện tích đất 21,1m2, tại thửa đất số
129. 07, tờ bản đồ số 35, tọa lạc tại ấp X, xã Y, huyện Z, tỉnh Sóc Trăng do ông A đứng
130. tên giấy chứng nhận quyền sử dụng đất. (có tuyên tứ cận kèm theo)
131. 4. Bà B và ông D được quyền sử dụng diện tích đất 62m2, tại thửa đất số 07,
132. tờ bản đồ số 35, tọa lạc tại ấp X, xã Y, huyện Z, tỉnh Sóc Trăng do ông A đứng tên
133. giấy chứng nhận quyền sử dụng đất. (có tuyên tứ cận kèm theo)
134. Sau khi bản án có hiệu lực pháp luật ông C, bà E, bà B và ông D tự kê khai,
135. làm thủ tục xin cấp giấy chứng nhận quyền sử dụng đất theo quy định của pháp
136. luật đối với diện tích đất được giao nêu trên.
137. Ngoài ra, bản án sơ thẩm còn tuyên về án phí sơ thẩm, chi phí thẩm định,
138. định giá và thông báo quyền kháng cáo cho các đương sự theo quy định pháp luật.
139. * Sau khi xét xử sơ thẩm, bị đơn bà B và người có quyền lợi, nghĩa vụ liên
140. quan UBND tỉnh Sóc Trăng có kháng cáo, Viện trưởng Viện kiểm sát nhân dân
141. cấp cao tại thành phố Hồ Chí Minh có kháng nghị bản án dân sự sơ thẩm nên sự
142. việc được Tòa án nhân dân cấp cao tại thành phố Hồ Chí Minh thụ lý, giải quyết.
143. Tại Bản án dân sự phúc thẩm số 37/2017/DS-PT, ngày 30/3/2017 đã quyết định
144. căn cứ khoản 3 Điều 308 Bộ luật tố tụng dân sự: Chấp nhận kháng cáo của bị đơn
145. bà B và người có quyền lợi, nghĩa vụ liên quan UBND tỉnh Sóc Trăng và kháng
146. nghị của Viện trưởng Viện kiểm sát nhân dân cấp cao tại thành phố Hồ Chí Minh.
147. Hủy bản án dân sự sơ thẩm số 19/2015/DS-ST, ngày 09/9/2015 của Tòa án nhân
148. dân tỉnh Sóc Trăng và chuyển hồ sơ về cho Tòa án cấp sơ thẩm giải quyết lại vụ án
149. theo thủ tục sơ thẩm.
150. - Theo đơn khởi kiện (v/v yêu cầu Tòa án tiếp tục xét xử vụ án) đề ngày
151. 10/5/2017, biên bản lấy lời khai ngày 15/6/2017 và đơn khởi kiện (sửa đổi, bổ
152. sung) đề ngày 13/7/2017, nguyên đơn ông A trình bày: Ông A xác định hiện nay
153. ông yêu cầu Tòa án giải quyết: Buộc bà B, ông D trả lại cho ông giá trị phần đất
154. lấn chiếm diện tích 62m2 (chiều ngang trước 1,2m, chiều ngang sau 1,3m, chiều
155. dài 49,35m) và giá trị phần đất UBND tỉnh Sóc Trăng đã cấp giấy chứng nhận
156. quyền sử dụng đất chồng lên đất của ông diện tích 166,9m2; buộc ông C, bà E trả
157. lại cho ông giá trị phần đất lấn chiếm diện tích 21,1m2; ông yêu cầu trả giá trị đất
158. theo giá Nhà nước quy định tại thời điểm xét xử sơ thẩm, không yêu cầu trả đất.
159. * Tại phiên tòa sơ thẩm, người đại diện hợp pháp của nguyên đơn ông A giữ
160. nguyên yêu cầu khởi kiện. Các đương sự không tự thỏa thuận được với nhau về
161. việc giải quyết vụ án.
162. * Kiểm sát viên phát biểu ý kiến Viện kiểm sát về việc tuân thủ và chấp
163. hành pháp luật tố tụng của Thẩm phán, Hội đồng xét xử, người tiến hành tố tụng
164. và người tham gia tố tụng trong quá trình giải quyết vụ án trong giai đoạn xét xử
165. sơ thẩm, kể từ khi thụ lý vụ án cho đến trước thời điểm Hội đồng xét xử nghị án.
166. Đồng thời, phát biểu về tính có căn cứ và hợp pháp của việc khởi kiện, về quan
167. điểm đường lối giải quyết vụ án, đề nghị Hội đồng xét xử giải quyết vụ án theo
168. hướng chấp nhận một phần yêu cầu khởi kiện của ông A, buộc bà B, ông D trả lại
169. cho ông A phần đất lấn chiếm diện tích 62m2 và buộc ông C, bà E trả lại cho ông A
170. giá trị phần đất lấn chiếm diện tích 21,1m2; đối với yêu cầu khởi kiện của ông A về
171. việc yêu cầu bà B, ông D trả lại giá trị phần đất UBND tỉnh Sóc Trăng đã cấp giấy
172. chứng nhận quyền sử dụng đất chồng lên đất của ông A diện tích 166,9m2 thì đề
173. nghị tách ra giải quyết trong vụ án khác khi ông A có yêu cầu.
Considering the following rules: Applicable provisions of Vietnamese law:
1. [BLDS 2015] Điều 175. Ranh giới giữa các bất động sản. 1. Ranh giới giữa các bất động sản liền kề được xác định theo thoả thuận hoặc theo quyết định của cơ quan nhà nước có thẩm quyền. Ranh giới cũng có thể được xác định theo tập quán hoặc theo ranh giới đã tồn tại từ 30 năm trở lên mà không có tranh chấp. Không được lấn, chiếm, thay đổi mốc giới ngăn cách, kể cả trường hợp ranh giới là kênh, mương, hào, rãnh, bờ ruộng. Mọi chủ thể có nghĩa vụ tôn trọng, duy trì ranh giới chung. 2. Người sử dụng đất được sử dụng không gian và lòng đất theo chiều thẳng đứng từ ranh giới của thửa đất phù hợp với quy định của pháp luật và không được làm ảnh hưởng đến việc sử dụng đất của người khác. Người sử dụng đất chỉ được trồng 
2. [BLDS 2015] Điều 325. Thế chấp quyền sử dụng đất mà không thế chấp tài sản gắn liền với đất. 1. Trường hợp thế chấp quyền sử dụng đất mà không thế chấp tài sản gắn liền với đất và người sử dụng đất đồng thời là chủ sở hữu tài sản gắn liền với đất thì tài sản được xử lý bao gồm cả tài sản gắn liền với đất, trừ trường hợp có thỏa thuận khác. 2. Trường hợp thế chấp quyền sử dụng đất mà người sử dụng đất không đồng thời là chủ sở hữu tài sản gắn liền với đất thì khi xử lý quyền sử dụng đất, chủ sở hữu tài sản gắn liền với đất được tiếp tục sử dụng đất trong phạm vi quyền, nghĩa vụ của mình; quyền và nghĩa vụ của bên thế chấp trong mối quan hệ với chủ sở hữu tài sản gắn liền với đất được chuyển giao cho người nhận chu
3. [BLDS 2015] Điều 326. Thế chấp tài sản gắn liền với đất mà không thế chấp quyền sử dụng đất. 1. Trường hợp chỉ thế chấp tài sản gắn liền với đất mà không thế chấp quyền sử dụng đất và chủ sở hữu tài sản gắn liền với đất đồng thời là người sử dụng đất thì tài sản được xử lý bao gồm cả quyền sử dụng đất, trừ trường hợp có thỏa thuận khác. 2. Trường hợp chỉ thế chấp tài sản gắn liền với đất mà không thế chấp quyền sử dụng đất và chủ sở hữu tài sản gắn liền với đất không đồng thời là người sử dụng đất thì khi xử lý tài sản gắn liền với đất, người nhận chuyển quyền sở hữu tài sản gắn liền với đất được tiếp tục sử dụng đất trong phạm vi quyền, nghĩa vụ của chủ sở hữu tài sản gắn liền với đất được chuyển giao, trừ trườn
4. [BLDS 2015] Điều 501. Nội dung của hợp đồng về quyền sử dụng đất. 1. Quy định chung về hợp đồng và nội dung của hợp đồng thông dụng có liên quan trong Bộ luật này cũng được áp dụng với hợp đồng về quyền sử dụng đất, trừ trường hợp pháp luật có quy định khác. 2. Nội dung của hợp đồng về quyền sử dụng đất không được trái với quy định về mục đích sử dụng, thời hạn sử dụng đất, quy hoạch, kế hoạch sử dụng đất và các quyền, nghĩa vụ khác theo quy định của pháp luật về đất đai và quy định khác của pháp luật có liên quan
5. [BLDS 2015] Điều 502. Hình thức, thủ tục thực hiện hợp đồng về quyền sử dụng đất. 1. Hợp đồng về quyền sử dụng đất phải được lập thành văn bản theo hình thức phù hợp với quy định của Bộ luật này, pháp luật về đất đai và quy định khác của pháp luật có liên quan. 2. Việc thực hiện hợp đồng về quyền sử dụng đất phải đúng trình tự, thủ tục theo quy định của pháp luật về đất đai và quy định khác của pháp luật có liên quan
Please suggest hypotheses to support why the outcome of the case might be the court rejects all of the plaintiff's claims.
```
**Response**
```
Để xác định liệu yêu cầu của nguyên đơn có được chấp nhận hay không, chúng ta cần phân tích từng yêu cầu cụ thể và xem xét các quy định pháp luật liên quan.

1. Yêu cầu thứ nhất: "Buộc bà B, ông D trả lại cho ông A giá trị phần đất lấn chiếm diện tích 62m2".
   - Theo Điều 175 BLDS 2015, ranh giới giữa các bất động sản liền kề được xác định theo thoả thuận hoặc quyết định của cơ quan nhà nước có thẩm quyền. Không được lấn, chiếm, thay đổi mốc giới ngăn cách.
   - Từ thông tin cung cấp, không có thoả thuận nào về ranh giới giữa đất của ông A và bà B, ông D. Việc bà B, ông D sử dụng đất lấn chiếm không được pháp luật thừa nhận.
   - Tuy nhiên, việc xác định giá trị đất lấn chiếm cần dựa trên giá đất theo quy định của Nhà nước tại thời điểm xét xử sơ thẩm. Đây là yêu cầu phức tạp và đòi hỏi xác định giá đất cụ thể, có thể khó khăn.

2. Yêu cầu thứ hai: "Buộc ông C, bà E trả lại cho ông A giá trị phần đất lấn chiếm diện tích 21,1m2".
   - Theo Điều 175 BLDS 2015, ranh giới giữa các bất động sản liền kề được xác định theo thoả thuận hoặc quyết định của cơ quan nhà nước có thẩm quyền. Không được lấn, chiếm, thay đổi mốc giới ngăn cách.
   - Từ thông tin cung cấp, không có thoả thuận nào về ranh giới giữa đất của ông A và ông C, bà E. Việc ông C, bà E sử dụng đất lấn chiếm không được pháp luật thừa nhận.
   - Tương tự như yêu cầu thứ nhất, việc xác định giá trị đất lấn chiếm cũng cần dựa trên giá đất theo quy định của Nhà nước tại thời điểm xét xử sơ thẩm.

3. Yêu cầu thứ ba: "Buộc UBND tỉnh Sóc Trăng có trách nhiệm bồi hoàn cho ông A diện tích đất chồng lấn bị mất 166,9m2".
   - Theo Điều 175 BLDS 2015, ranh giới giữa các bất động sản liền kề được xác định theo thoả thuận hoặc quyết định của cơ quan nhà nước có thẩm quyền. Không được lấn, chiếm, thay đổi mốc giới ngăn cách.
   - UBND tỉnh Sóc Trăng đã cấp đất cho ông P chồng lên đất của ông A, nhưng việc cấp đất này không tuân theo quy định pháp luật về ranh giới đất.
   - Tuy nhiên, việc bồi
```

## judge#1 — judge

**Prompt**
```

```
**Response**
```
llm judge rejected all
```

## Result
- outcome: **the court accepts the plaintiff's claims in whole or in part**
- converged: True
- accepted hypotheses: