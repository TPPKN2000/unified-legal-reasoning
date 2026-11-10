# Civil law simulation

## A.1 — rule_based

**Prompt**
```
Considering the following facts:
1. Trong  đơn  khởi  kiện  ngày  05/01/2016,  quá trình giải quyết  vụ  án  và  tại
2. phiên  tòa,  nguyên  đơn  ông  Nguyễn  Hữu  C,  người  đại  diện  theo  ủy  quyền  của
3. nguyên  đơn  ông  Nguyễn  Văn  G  và  người  có  quyền  lợi  nghĩa  vụ  liên  quan  bà
4. Đàm Thị T trình bày:
5. Cha mẹ ông C là cụ Nguyễn Hữu Nhị và cụ Lê Thị Hường đều mất không
6. để lại di chúc. Di sản của 2 cụ là mảnh đất có diện tích 1845m2 thuộc thửa 539
7. tại xóm 4 xã T S, Đô Lương, Nghệ An được Nhà nước giao theo chính sách di
8. dân từ năm 1979. Hai cụ có 3 người con gồm ông C, ông Nguyễn Hữu Thắng và
9. bà Nguyễn Thị Thìn. Năm 2009, ông C, ông Thắng và bà Thìn đã họp bàn với
10. nhau  và  thống  nhất  giao  toàn  bộ  di  sản  của  2  cụ  cho  ông  C  được  toàn  quyền
11. quản lý, sử dụng.
12. Cũng  năm  1979,  vợ  chồng  ông  C  cũng  được  giao  thửa  đất  540,  diện  tích
13. 2110 m2 để làm nhà ở ngay bên cạnh đất cụ Nhị - cụ Hường. Đến năm 1990, do
14. bão  làm  đổ  nhà  nên vợ  chồng  ông  C tạm  chuyển  đến vị trí  khác  làm  nhà  ở và
15. được nhà nước cấp Giấy chứng nhận quyền sử dụng đất  đối với phần đất mới.
16. Sau khi 2 cụ mất, ông C là người con duy nhất còn sinh sống tại địa phương nên
17. trực tiếp quản lý đất các cụ. Năm 1995, ông C cho ông L, ông T mượn một phần
18. để phơi rơm, trồng sắn và một phần cho xã mượn làm sân bóng cho thiếu niên
19. xóm 4.
20. Ông C, bà T khẳng định không có việc gia đình bỏ hoang thửa 539 + 540 từ
21. năm 1984 và ông C vẫn quản lý đất của cha mẹ, vợ chồng ông thông qua việc
22. cho ông T, ông L và xã mượn tạm sử dụng, các cây cối của gia đình trồng vẫn
23. tồn tại trên đất.
24. Tuy nhiên, quá trình mượn đất, ông T, ông L đã trồng cây lâu năm trên đất
25. rồi không chịu trả nữa. Hiện trạng trên thửa đất 18 (ông L đang sử dụng) có 09
26. cây bạch đàn do anh em ông C trồng từ những năm 1980 và các cây cối trên đất
27. ông L trồng thêm từ sau 1994; trên thửa đất 53 (ông T đang sử dụng) có ngôi mộ
28. của cụ Đào Thị Toại và những cây cối do ông T mới trồng lên trên đất.
29. Sau  khi  họp  bàn  phân  chia  di  sản,  ông  C  làm  đơn  xin  lập  hồ  sơ  cấp  giấy
30. chứng nhận quyền sử dụng đất đối với thửa 539 và 540 (có một phần thuộc thửa
31. 18 và thửa 53 - Bản đồ địa chính) thì UBND xã T S không đồng ý vì cho rằng
32. đó là đất của UBND xã chứ không phải của gia đình ông còn ông T, ông L cũng
33. không  chịu  thu  hoạch  cây  cối  trên  đất  để  trả  lại  cho  ông  bà  nên  đã  phát  sinh
34. tranh chấp từ năm 2005 cho đến nay.
35. Nay ông bà yêu cầu ông T, ông L phải thu hoạch cây cối và trả lại thửa đất
36. 18 và thửa 53, tờ bản đồ 13 thuộc xóm 4 xã T S, Đô Lương, Nghệ An cho vợ chồng  ông  bà  theo  kết  quả  đo  đạc  thẩm  định  tại  chỗ  ngày  12/6/2017;  ông  bà
37. không đồng ý bồi thường tiền cây cối trên đất cũng như công sức bảo quản giữ
38. gìn đất cho ông T và ông L vì họ đã được hưởng lợi từ việc sử dụng đất. Về ngôi
39. mộ của cụ Đào Thị Toại trên thửa đất 53 thì ông bà thống nhất giữ lại toàn bộ
40. khuôn viên ngôi mộ như đề nghị của ông H và cụ V.
41. Ngoài ra, quá trình tranh chấp đất đai với ông T, ông L, ông C có làm đơn
42. yêu  cầu  UBND  xã  T  S,  UBND  huyện  Đ  L  giải  quyết.  Ông  đã  nhận  được  các
43. Quyết định: Quyết định số 310/UBND.TN ngày 26/9/2012 của UBND huyện Đ
44. L; Quyết định số 940/QĐ-UBND ngày 27/5/2013 của Chủ tịch UBND huyện Đ
45. L;  Quyết  định  số  14/QĐ-UBND  ngày  05/3/2012  của  UBND  xã  T  S  và  Quyết
46. định  số  27/QĐ-UBND  ngày  26/4/2012  của  Chủ  tịch  UBND  xã  TS.  Theo  ông,
47. các Quyết định này đều vi phạm pháp luật, làm ảnh hưởng đến quyền và lợi ích
48. hợp pháp của gia đình ông bởi vì:
49. - Đây là đất của bố mẹ ông và vợ chồng ông, đã có trong hồ sơ địa chính từ
50. năm  1983 – 1984 nhưng  UBND xã  T  S, UBND  huyện  Đ  L kết luận  không  có
51. giấy tờ là không đúng.
52. - Gia đình ông không bỏ hoang đất từ năm 1984 mà cho UBND xã, ông T,
53. ông  L  mượn  đất  từ  năm  1995.  Khoảng  thời  gian  từ  1984  đến  1995,  vợ  chồng
54. ông  C vẫn  quản lý sử  dụng bình thường. Đồng  thời, trên đất vẫn  tồn tại nhiều
55. cây bạch đàn do ông C và em trai là ông Thắng trồng từ năm 1980.
56. - Việc chính quyền không thu thuế không phải là lỗi của gia đình ông bà vì
57. thời  gian  1995  –  2005,  ông  C  cho  người  khác  mượn  đất  sử  dụng  chứ  ông  bà
58. không trực tiếp sử dụng, hơn nữa chính quyền cũng không thông báo cho ông bà
59. việc phải thực hiện nghĩa vụ gì cả.
60. - Ông bà không kê khai xin cấp Giấy chứng nhận quyền sử dụng đất khi có
61. Nghị định 64CP vì lúc đó không am hiểu pháp luật và cũng do đang cho người
62. khác mượn đất.
63. - Về hình thức, quy trình giải quyết khiếu nại đều vi phạm pháp luật. Trong
64. đơn ngày 12/12/2011, ông C yêu cầu giải quyết tranh chấp đất giữa ông với ông
65. T – ông L nhưng UBND xã lại giải quyết khiếu nại bằng Quyết định 14 là không
66. đúng vì ông không khiếu nại quyết định hành chính hay hành vi hành chính. Do
67. vậy, chủ tịch UBND huyện giải quyết khiếu nại lần 2 đối với Quyết định 14 là
68. cũng vi phạm pháp luật. Đối với Quyết định 27 thì xã giải quyết việc ông C yêu
69. cầu  cấp  giấy  chứng  nhận  quyền  sử  dụng  đất  là  không  đúng  thẩm  quyền  vì
70. UBND xã chỉ có quyền lập hồ sơ, không có quyền cấp giấy. Quyết định 310 của
71. UBND huyện Đ L vi phạm thẩm quyền vì đáng lẽ là thuộc thẩm quyền của Chủ
72. tịch UBND huyện Đ L.
73. - Riêng nội dung liên quan đến 77,9m2 đất đã thu hồi và 06 cây bạch đàn
74. đã giải tỏa để làm đường liên xã Trung  – Xuân được xem xét trong các Quyết
75. định trên thì ông không đề nghị Tòa án giải quyết vì không liên quan đến vụ án.
76. Cụ thể trong từng Quyết định, ông C yêu cầu Tòa án hủy những phần sau:
77. Quyết  định  14:  yêu  cầu  hủy  toàn  bộ  vì  Quyết  định  căn  cứ  vào  nội  dung
78. phần kết luận gia đình ông C không có nhu cầu sử dụng và phần xác minh đất do
79. UBND xã quản lý là không đúng.
80. Quyết định 27: yêu cầu hủy tòan bộ bởi nội dung kết luận ông khiếu nại sai
81. và đề nghị cấp giấy không có cơ sở.
82. Quyết định 940: hủy toàn bộ bởi các nội dung kết luận đất không phải của
83. ông Chiến là vi phạm.
84. Quyết định 310: chỉ yêu cầu hủy nội dung kết luận việc ông C yêu cầu cấp
85. lại quyền sử dụng đất 5419m2 là không có cơ sở xem xét giải quyết, Quyết định
86. xác  định  “thực  chất  đất  không  thuộc  quyền  sử  dụng  của  gia  đình  ông  C”;  xác
87. định UBND xã T S là chủ sử dụng đất theo sổ mục kê, sơ đồ kỹ thuật thửa đất
88. và phần nội dung giao cho UBND xã T S sớm có kế hoạch đưa phần diện tích
89. đất mà ông C, ông T, ông L đang trồng cây lâm nghiệp vào quản lý theo đúng
90. quy định của pháp luật.
91. Quá trình giải quyết vụ án, tại phiên tòa, bị đơn  ông Hoàng Đình T đồng
92. thời là người đại diện theo ủy quyền của bà Nguyễn Thị Th trình bày: năm 1985,
93. thấy thửa đất 540 của vợ chồng ông C (nay có 1 phần là thửa 53) bỏ hoang, vợ
94. chồng ông đã tận dụng để trồng sắn nhưng ông C không có ý kiến gì. Đến năm
95. 1986,  vợ  chồng  ông  đã  trồng  cây  lâu  năm  trên  đất  là  bạch  đàn,  keo  và  đã  thu
96. hoạch nhiều lần (gần nhất là năm 2005). Sau khi ông bà sử dụng đất, xã cũng sử
97. dụng  một  phần  đất  để  làm  sân  bóng  nên  vợ  chồng  ông  dịch  phần  sử  dụng  lên
98. giáp  đường  liên  xã.  Năm  2005, do  thấy  đất  có  giá  trị,  vợ  chồng  ông  C  đòi  vợ
99. chồng ông trả đất nhưng ông bà không đồng ý vì đất đó thuộc quyền quản lý của
100. UBND xã T S. Hiện tại trên đất chỉ có những mầm cây mọc lên từ các gốc cây
101. có trước năm 2005, một số cây cối do vợ chồng ông trồng mới sau này và khu
102. lăng mộ của cụ Toại do con trai cụ là ông Vương Đình H xây trên đất như phản
103. ánh tại Biên bản xem xét thẩm định tại chỗ ngày 12/6/2017 và biên bản định giá
104. tài sản ngày 15/8/2017.
105. Vì  tranh  chấp  kéo  dài  nên  năm  2013,  UBND  xã  T  S  đã  làm  việc  và  vợ
106. chồng ông cam kết tiếp tục canh tác trên đất cho đến khi nhà nước cần, phải thu
107. hồi và không được bồi thường gì cả vì đây là đất thuộc diện quản lý của UBND
108. xã T S. Đến nay, vợ chồng ông cũng như bất cứ cá nhân nào đều chưa được nhà
109. nước  công  nhận quyền  sử  dụng  thửa  đất  53  (khi  đo  đạc  thửa đất này  vào  năm
110. 2003, phần ông bà không sử dụng nhưng cán bộ đo đạc cũng đo vào nên có diện
111. tích  là  1490m2).  Ông  C  yêu  cầu  vợ  chồng  ông  trả  lại  thửa  đất  53,  diện  tích
112. 1119,5m2 thì ông có ý kiến như sau: ông không mượn đất của ông C nên không
113. trả lại cho ông C mà chỉ trả lại cho nhà nước; nếu nhà nước thu hồi thì  ông bà
114. không yêu cầu bồi thường. Nếu tòa án giao đất cho UBND xã T S để UBND xã
115. bán  cho  tổ  chức,  cá  nhân  nào  không  phải  là  nhà  nước  thì  họ  phải  bồi  thường
116. công sức bảo quản, giữ gìn, cải tạo đất trong suốt 30 năm cho  ông bà theo quy
117. định của pháp luật. Còn riêng gia đình ông C thì ông bà không bao giờ trả lại đất
118. nên ông bà không đặt vấn đề bồi hoàn với gia đình ông Chiến. Về ngôi mộ của
119. cụ  Đào  Thị  Toại  trên  đất  53  thì  ông  bà  thống  nhất  giữ  lại  toàn  bộ  khuôn  viên
120. ngôi mộ như đề nghị của ông H và cụ V.
121. Ông bà không có ý kiến gì về yêu cầu hủy các quyết định hành chính như
122. yêu cầu của ông C.
123. Bị  đơn  ông  Hoàng  Đình  L,  người  có  quyền  lợi  và  nghĩa  vụ  liên  quan  bà
124. Đoàn Thị H trình bày: năm 1986, sau khi vợ chồng cụ Nhị mất, vợ chồng ông
125. bà vào trồng sắn trên phần đất mà cụ Nhị bỏ hoang. Lúc này, vợ chồng ông T
126. cũng đã  canh  tác  trên  đất  của  ông  C  bỏ hoang  nhưng  chính quyền  địa phương
127. cũng như các con của cụ Nhị không có ý kiến gì. Sau đó, ông bà bắt đầu trồng
128. cây lấy gỗ như bạch đàn, keo, xoan để phủ xanh đất trống đồi núi trọc, nhà nước
129. không thu bất  cứ  khoản  nghĩa vụ  nào  cũng như  không  hỗ trợ  gì  cho  vợ  chồng
130. ông bà trồng cây lấy gỗ. Do thấy đất có giá trị nên năm 2005 – 2006, ông C xảy
131. ra tranh chấp mặc dù trước đó chẳng có chuyện gì xảy ra. Vì tranh chấp kéo dài
132. nên năm 2013, UBND xã T S đã làm việc và ông bà đã viết cam kết là được xã
133. cho tiếp tục canh tác trên đất đến khi nhà nước cần phải thu hồi và không được
134. bồi thường gì cả vì đây là đất thuộc diện quản lý của UBND xã T S. Đến nay,
135. ông bà cũng như bất cứ cá nhân nào đều chưa được nhà nước công nhận quyền
136. sử dụng thửa đất 18, diện tích (năm 2003 đo đạc thì diện tích là 1141m2). Trên
137. đất  hiện  nay  có  09  cây  bạch  đàn  lá  nhỏ  của  ông  bà  trồng  nhưng  ông  C  đang
138. tranh chấp và các cây cối như phản ánh tại Biên bản xem xét thẩm  định tại chỗ
139. ngày 12/6/2017 và biên bản định giá tài sản ngày 15/8/2017. Nay vợ chồng ông
140. C yêu cầu ông bà trả lại thửa đất 18, diện tích 1114m2 thì ông bà có ý kiến như
141. sau: ông bà không mượn đất của ông C nên không trả lại cho ông C mà chỉ trả
142. lại  cho  nhà  nước;  nếu  nhà  nước  thu  hồi  thì  ông  bà  không  yêu  cầu  bồi  thường.
143. Nếu tòa án giao đất cho UBND xã T S để UBND xã bán cho tổ chức, cá nhân
144. nào không phải là nhà nước thì họ phải bồi thường công sức bảo quản, giữ gìn,
145. cải tạo đất trong suốt 30 năm cho ông bà theo quy định của pháp luật. Còn riêng
146. vợ chồng ông C thì ông bà không bao giờ trả lại đất nên ông bà không đặt vấn
147. đề bồi hoàn với gia đình ông C.
148. Ông bà không có ý kiến gì về yêu cầu hủy các quyết định hành chính như
149. yêu cầu của ông C.
150. Đại diện người có quyền lợi, nghĩa vụ liên quan UBND xã T S, ông Đoàn
151. Văn L trình bày: Năm 1979, hai thửa đất 53 và 18 (tức thuộc một phần thửa 539
152. và một phần thửa 540 theo Bản đồ 299) do ông Nguyễn Hữu C và cụ Nguyễn
153. Hữu Nhị (cha của ông C) sử dụng để xây nhà ở. Từ khi gia đình ông C, cụ Nhị
154. tự bỏ hoang đất thì ông T, ông L có trồng cây trên đất chứ không có việc ông T,
155. ông L mượn đất ông C. Do đất bị bỏ hoang nên với tư cách là cơ quan quản lý
156. đất  đai  ở  địa  phương,  thời  gian  thực  hiện  Nghị  định  64CP  và  thời  điểm  năm
157. 2003, UBND xã T S đã đưa thửa 18, 53 vào sổ mục kê với diện đất thuộc quản
158. lý  của  UBND  xã  (đất  vô  chủ)  mặc  dù  vẫn  chưa  đề  nghị  UBND  huyện  Đ  L  ra
159. Quyết định thu hồi theo quy định của pháp luật. Hai thửa đất này được đưa vào
160. sử dụng từ năm 1979 với mục đích là đất ở nhưng từ năm 1994 đến nay thì đã
161. được sử dụng vào trồng cây lâm nghiệp và hiện tại mục đích sử dụng đất được
162. xác định là đất trồng cây lâu năm.
163. Gia đình ông C chưa bao giờ thực hiện việc kê khai thửa 53 và thửa 18 để
164. xin  cấp  Giấy  chứng  nhận  theo  Nghị  định  64CP;  không  thực  hiện  nghĩa  vụ  tài
165. chính đối với nhà nước và cũng không lập thủ tục phân chia di sản thừa kế của
166. vợ chồng cụ Nhị - cụ Hường. Bản thân gia đình ông C cũng không có giấy tờ gì
167. chứng minh việc mình được quyền sử dụng đất; quá trình sử dụng đất lại không
168. ổn  định,  liên  tục  từ  khi  hình  thành  thửa  đất  đến  nay.  Mặc  dù  hai  thửa  đất  này
169. đang nằm trong diện quản lý của UBND xã T S nhưng nếu ông C có đủ căn cứ
170. để chứng minh quyền sử dụng đất của mình thì phán quyết của Tòa án thế nào
171. UBND  xã  T  S  sẵn  sàng  thực hiện. Còn  yêu  cầu  của ông  C  thì  đề  nghị  Tòa án
172. giải quyết theo pháp luật. Về ngôi mộ của cụ Đào Thị Toại trên thửa đất 18 thì
173. UBND xã T S thống nhất giữ lại toàn bộ khuôn viên ngôi mộ như đề nghị của
174. ông H và cụ V.
175. Đối với yêu cầu hủy Quyết định 14 và 27: ông L cho rằng, do đất chưa có
176. giấy tờ nên khi nhận được đơn của ông C, UBND xã không tiến hành hòa giải
177. mà phải giải quyết theo trình tự khiếu nại.
178. + Về Quyết định 14: về thẩm quyền giải quyết là chủ tịch xã, tuy nhiên,
179. người ký lại ghi tên là “UBND xã”, mặc dù có sai sót nhưng không phải là sai
180. sót lớn vì dù sao người đứng đầu UBND xã cũng là chủ tịch xã.
181. Thời hạn, thời hiệu giải quyết mặc dù đã có gia hạn nhưng vẫn vi phạm
182. theo  quy  định  của  pháp  luật  nhưng  đó  là  do  nội  dung  vụ  việc  phức  tạp,  ông
183. Chiến thường xuyên bổ sung nội dung khiếu nại nhưng vì sơ suất nên xã không
184. lập văn bản xác thực việc bổ sung.
185. Quá trình thực hiện các thủ tục trình tự giải quyết khiếu nại có một số sai
186. sót  như  không  tổ  chức  đối  thoại  nhưng  cũng  đã  thực  hiện  việc  xác  minh  nội
187. dung khiếu nại theo luật định.
188. Về cơ sở pháp lý: đã áp dụng Luật khiếu nại, tố cáo năm 1998 và các đạo
189. luật sửa đổi bổ sung; Nghị quyết 136/2006 hướng dẫn luật khiếu nại, tố cáo.
190. Sau khi giải quyết xong khiếu nại, UBND xã T S đã thực hiện việc giao
191. các văn bản trong thời hạn pháp luật.
192. + Về quyết định số 27: trên cơ sở văn bản chỉ đạo số 97/UBND-TTr ngày
193. 05/4/2012 của UBND huyện Đô Lương, chủ tịch UBND xã T S đã giải quyết lại
194. khiếu nại của ông C. Thẩm quyền ban hành quyết định, thời hạn, thời hiệu giải
195. quyết, trình tự thủ tục cũng như việc giao nhận các văn bản cho ông C là đúng
196. quy định của pháp luật.
197. Việc ông C cho rằng, Chủ tịch xã không có quyền giải quyết khiếu nại đối
198. với  nội  dung  xin  cấp  giấy  chứng  nhận  quyền  sử  dụng  đất  thì  ủy  ban  xã  thừa
199. nhận, tuy nhiên, do ông C không phải là chủ sử dụng đất nên kể cả việc lập hồ
200. sơ ở UBND xã T S cũng không được thực hiện nên chắc chắn là không được cấp
201. giấy chứng nhận.
202. Về cơ sở pháp lý: đã áp dụng Luật khiếu nại, tố cáo năm 1998 và các đạo
203. luật sửa đổi bổ sung; Nghị quyết 136/2006 hướng dẫn luật khiếu nại, tố cáo.
204. Việc  giải  quyết  và  ban  hành  Quyết  định  14  và  27  là  của  chủ  tịch  tiền
205. nhiệm nên việc xử lý hai quyết định này như thế nào thì đề nghị Tòa án căn cứ
206. vào pháp luật để giải quyết.
207. Trong  bản  khai  ngày  08/6/2017,  người  đại  diện  theo  ủy  quyền  của  Chủ
208. tịch  UBND  huyện  Đ  L,  UBND  huyện  Đ  L,  ông Nguyễn  Trọng H  trình bày  đối
209. với yêu cầu hủy hai quyết định 940 và 310:
210. + Đối với Quyết định 940:
211. Trên cơ sở đơn khiếu nại lần 2 của ông C (nay đơn đã bị thất lạc), đối với
212. Quyết định giải quyết khiếu nại số 14 của UBND xã TS, Chủ tịch UBND huyện
213. Đ  L  giải  quyết  khiếu  nại và ban hành  Quyết  định  là phù hợp thẩm  quyền  theo
214. quy  định  tại  Luật  Tổ  chức  HĐND  và  UBND  ngày  26/11/2003;  Luật  khiếu  nại
215. ngày 11/11/2011;
216. Thời  hạn  giải  quyết  đơn  có  sự  vi  phạm;  cơ  sở  pháp  lý  ban  hành  Quyết
217. định là Luật khiếu nại ngày 11/11/2011 và Nghị định số: 75/2012/NĐ-CP ngày
218. 03/10/2012  của  Chính  phủ;  Luật  đất  đai  ngày  26/11/2003  và  Nghị  định  số:
219. 84/2007/NĐ-CP ngày 29/10/2004 của Chính phủ;
220. Cơ  sở  thực  tế:  qua  kiểm  tra  hồ  sơ  địa  chính  lưu  tại  UBND  xã  T  S,  Văn
221. phòng đăng ký quyền sử dụng đất huyện Đ L và kiểm tra thực tế nguồn gốc, quá
222. trình sử dụng đất của ông C và cụ Nhị thì khẳng định:
223. Hộ ông C và cụ Nhị (bố của ông C) được UBND xã T S giao thửa đất nói
224. trên để xây dựng nhà ở từ năm 1979. Khoảng năm 1980 do bị lốc làm hỏng nhà
225. nên năm 1981 ông C di chuyển nhà sang khu vực đồi Cồn Vạng ở và nay được
226. UBND huyện cấp đổi giấy chứng nhận quyền sử dụng đất ngày 31/12/2005, với
227. diện tích 3.050 m2, thửa đất số 407, tờ bản đồ số 13.
228. Phần diện tích còn lại hộ cụ Nhị tiếp tục sử dụng đến khi các cụ qua đời,
229. khoảng năm 1983 – 1984. Đến năm 1987 – 1988 ông C tiến hành tháo dỡ ngôi
230. nhà do cụ Nhị để lại, từ đó trở đi thửa đất trước đây hộ ông C và hộ cụ Nhị bỏ
231. hoang không ai sử dụng. Do thấy đất bỏ hoang hộ ông T và ông L (nhà liền kề)
232. đã  tiến  hành  trồng  cây  lâm  nghiệp  và  trồng  cây  hàng  năm  khác  trên  một  phần
233. diện tích của 02 thửa đất nói trên. Năm 1994 UBND xã T S đã đồng ý cho Ban
234. cán sự xóm 4 sử dụng một phần diện tích khu đất đó để làm sân bóng của xóm.
235. Năm 2004 UBND xã đã tiến hành quy hoạch lại hệ thống sân bóng các xóm trên
236. địa bàn toàn xã trong đó có sân bóng xóm 4, sau khi hoàn thành việc san lấp mặt
237. bằng  sân  bóng  mới,  thì  phần  diện  tích  sân  bóng  cũ  lại  tiếp  tục  bỏ  hoang,  đến
238. tháng 10/2005 ông Nguyễn Hữu C làm đơn kiến nghị gửi UBND xã T S đề nghị
239. cấp giấy chứng nhận quyền sử dụng đất để trồng cây lâm nghiệp, đồng thời ông
240. C đã tự ý trồng cây lâm nghiệp từ tháng 10/2005 đến nay.
241. Hộ  gia  đình  ông  C  không  thực  hiện  một  khoản  nghĩa  vụ  tài  chính  nào  liên
242. quan đến thửa đất mà hiện nay ông C đề nghị cấp giấy chứng nhận quyền sử dụng
243. đất (từ khoảng năm 1983 – 1984 cụ Nhị qua đời đến nay).
244. Hiện nay trên khu vực đất ông C có đơn kiến nghị cấp giấy chứng nhận có
245. 03 hộ gia đình đang sản xuất  (trồng cây lâm nghiêp); Cụ thể: 1 phần diện tích
246. ông Nguyễn Hữu C trồng cây lâm nghiệp (tràm) từ tháng 10/2005 với diện tích
247. 3.252,5m2, số cây ông C trồng hiện nay đang do ông C quản lý. Một phần diện
248. tích do hộ ông T sử dụng trồng bạch đàn có diện tích 1.103,2 m2 và một phần do
249. hộ ông L sử dụng trồng bạch đàn có diện tích: 1.103,3m2; Như vậy trên thực địa
250. có 03 thửa đất. Hiện nay 02 thửa đất do ông T và ông L sử dụng chỉ còn lại một
251. số cây bạch đàn trồng từ những năm 1989 - 1990 ở xung quanh, phần diện tích
252. còn lại đang bỏ hoang.
253. Căn cứ vào Khoản 1 Điều 46;  Khoản 19 Điều 4; Khoản 1 + khoản 4 Điều
254. 50 Luật Đất đai năm 2003; Điểm a, Khoản 1, Điều 3 Nghị định số 84 thì khẳng định,
255. khiếu nại của ông C đối với Quyết định số 14 là sai vì:
256. Ông C không xuất trình được bất kỳ giấy tờ pháp lý nào chứng minh là đất
257. của ông.
258. Gia đình ông không trực tiếp sử dụng ổn định, liên tục 2 thửa đất 53 + 18 từ
259. năm 1988 đến nay, không thực hiện đăng ký quyền sử dụng đất tại cơ quan có thẩm
260. quyền,  không  thực  hiện  nghĩa  vụ  tài  chính  đối  với  nhà  nước  nên  UBND  xã  T  S
261. không làm thủ tục để đề nghị cấp có thẩm quyền cấp giấy chứng nhận quyền sử
262. dụng đất cho gia đình ông là đúng quy định của pháp luật.
263. + Đối với Quyết định 310: ngày 03/5/2012, ông C gửi đơn kiến nghị yêu
264. cầu giải quyết việc cấp lại quyền sử dụng đất 5419 và bồi thường 77,9m2 và 06
265. cây đường kính 30cm-40cm khi giải tỏa mặt bằng mở đường giao thông liên xã.
266. UBND  huyện  đã  giao  phòng  tài  nguyên  –  môi  trường  kiểm  tra  và  ban  hành
267. Quyết định 310 với nội dung không chấp nhận yêu cầu của ông C cũng vì các lý
268. do được nêu trong nội dung của Quyết định 940.
269. Ông H không chấp nhận yêu cầu hủy Quyết định 940 và Quyết định 310
270. của ông C và đề nghị Tòa án giải quyết theo pháp luật.
271. Người  có  quyền  lợi,  nghĩa  vụ  liên  quan  cụ  Vương  Đình  V,  ông  Vương
272. Đình H trình bày: cụ Đào Thị Toại là vợ cụ V và là mẹ của ông H. Cụ Toại mất
273. năm 1953 và chỉ có ông H là con. Do cụ V, ông H chuyển ra Thái Nguyên sinh
274. sống  nên  sau  này,  khi  tìm  được  mộ  thì  ông  H  đã  tiến  hành  xây  cất  lăng  trên
275. khuôn viên thửa 53 mà các đương sự tranh chấp. Nay ông H, cụ V yêu cầu, nếu
276. ai là người được Tòa án giao quyền sử dụng đất thì giữ nguyên khuôn viên lăng
277. mộ của cụ Toại để gia đình thực hiện việc thờ cúng theo phong tục tập quán và
278. không có yêu cầu gì thêm.
279. Người làm chứng ông Vương Đình Đơủ trình bày: do thời gian dài, tuổi
280. cao nên ông không nhớ rõ sự việc nên đề nghị Tòa án căn cứ vào những thông
281. tin  ông  cung  cấp  cho  UBND  các  cấp  khi  giải  quyết  khiếu  nại  và  cho  Tòa  án
282. trong quá trình giải quyết vụ án để xác định tính khách quan của các sự kiện đã
283. diễn  ra  thời gian ông  đang giữ  chức  vụ  Trưởng  ban quản  lý  ruộng đất  xã  T  S.
284. Tuy nhiên, ông khẳng định, khi xã trưng dụng đất làm sân bóng thì ông T, ông L
285. chưa sử dụng đất như bây giờ.
286. Người làm chứng bà Thìn thừa nhận: cha mẹ bà có để lại di sản là thửa
287. đất  539  mà  hiện  nay,  một  phần  thửa  đất  này  do  vợ  chồng  ông  L  tự  ý  sử  dụng
288. trồng  cây  (ghi  nhận tại thửa  mới  là  18, diện tích 1114m2), hiện vẫn  còn nhiều
289. cây bạch đàn trên đất do cha bà, anh trai và bà trồng từ năm 1980  - 1981. Năm
290. 2009, do bà và ông Thắng ở xa nên anh em đã họp bàn chia di sản của cha mẹ
291. với nội dung giao lại toàn bộ di sản cho ông C sở hữu, quản lý, sử dụng vì ông C
292. là anh cả đồng thời ở tại chỗ làm nhiệm vụ thờ cúng cha mẹ.  Nay bà không có
293. quyền lợi, nghĩa vụ gì liên quan đến vụ án và đề nghị Tòa án bảo vệ quyền sử
294. dụng đất hợp pháp của cha mẹ bà, buộc những người đang chiếm hữu sử dụng di
295. sản của cha mẹ bà phải trả lại cho ông C theo luật định.
296. Người làm chứng ông Thắng vắng mặt tại phiên tòa nhưng trong quá trình
297. thu thập chứng cứ, ông Thắng cũng khẳng định nội dung như trình bày của bà
298. Thìn. Ông Thắng xác định ông không còn quyền lợi, nghĩa vụ gì liên quan đến
299. vụ án và đề nghị Tòa án bảo vệ quyền sử dụng đất hợp pháp của cha mẹ ông,
300. buộc những người đang chiếm hữu sử dụng di sản của cha mẹ ông phải trả lại
301. cho ông C theo luật định (người đại diện theo ủy quyền của ông Thắng – ông G -
302. không bổ sung gì thêm vào trình bày của ông Thắng).
303. Người làm chứng bà Lê Thị Quảng trình bày: bà không nhớ cụ thể về đất
304. của ông C nhưng có sự kiện vào năm 1991 – 1993, cha bà là ông Lê Văn Lĩnh
305. có mượn ông C phần đất mà các đương sự đang tranh chấp để trồng sắn. Năm
306. 1993, sau khi cha bà mất thì bà không biết việc sử dụng đất thuộc về ai nữa.
307. Tại phiên tòa, đại diện Viện kiểm sát nhân dân huyện Đô Lương phát biểu
308. ý kiến theo quy định tại điều 262 Bộ luật tố tụng dân sự như sau:
309. - Về tố tụng: Thẩm phán đã tuân thủ các quy định của Bộ luật tố tụng dân
310. sự trong việc thụ lý vụ án, thông báo thụ lý vụ án, xác định quan hệ tranh chấp,
311. xác minh và thu thập chứng cứ, tổ chức hòa giải cũng như thời hạn giải quyết vụ
312. án.
313. Hội đồng xét xử tuân thủ đúng quy định về thành phần, nguyên tắc xét xử,
314. trình tự tố tụng tại phiên tòa.
315. Thư ký Tòa án thực hiện đúng quy định của Bộ luật tố tụng dân sự.
316. Các đương sự chấp hành nghiêm chỉnh quy định của Bộ luật tố tụng dân
317. sự.
318. -  Về  nội  dung:  sau  khi  phân  tích  các  tình  tiết  của  vụ  án  và  các  tài  liệu,
319. chứng cứ có tại hồ sơ, đại diện Viện kiểm sát đề nghị Hội đồng xét xử áp dụng
320. các quy định tại điều 166, Điều 185, Điều 579 Bộ luật dân sự; Điều 166 Luật đất
321. đai;  Luật  khiếu  nại  tố  cáo  năm  1998;  Luật  khiếu  nại  năm  2011;  Luật  tố  tụng
322. hành  chính:  chấp  nhận  đơn  khởi  kiện  của  ông  C,  buộc  vợ  chồng  ông  T  –  vợ
323. chồng ông L – UBND xã T S trả lại thửa đất 18 và 53 cho gia đình ông C; hủy
324. toàn bộ Quyết định hành chính số 14, số 27, số 940 và một phần Quyết định 310
325. theo quy định của pháp luật.
Considering the following rules: Applicable provisions of Vietnamese law:
1. [BLDS 2015] Điều 175. Ranh giới giữa các bất động sản. 1. Ranh giới giữa các bất động sản liền kề được xác định theo thoả thuận hoặc theo quyết định của cơ quan nhà nước có thẩm quyền. Ranh giới cũng có thể được xác định theo tập quán hoặc theo ranh giới đã tồn tại từ 30 năm trở lên mà không có tranh chấp. Không được lấn, chiếm, thay đổi mốc giới ngăn cách, kể cả trường hợp ranh giới là kênh, mương, hào, rãnh, bờ ruộng. Mọi chủ thể có nghĩa vụ tôn trọng, duy trì ranh giới chung. 2. Người sử dụng đất được sử dụng không gian và lòng đất theo chiều thẳng đứng từ ranh giới của thửa đất phù hợp với quy định của pháp luật và không được làm ảnh hưởng đến việc sử dụng đất của người khác. Người sử dụng đất chỉ được trồng 
2. [BLDS 2015] Điều 155. Không áp dụng thời hiệu khởi kiện. Thời hiệu khởi kiện không áp dụng trong trường hợp sau đây: 1. Yêu cầu bảo vệ quyền nhân thân không gắn với tài sản; 2. Yêu cầu bảo vệ quyền sở hữu, trừ trường hợp Bộ luật này, luật khác có liên quan quy định khác; 3. Tranh chấp về quyền sử dụng đất theo quy định của Luật đất đai; 4. Trường hợp khác do luật quy định
3. [BLDS 2015] Điều 478. Nghĩa vụ bảo đảm quyền sử dụng tài sản cho bên thuê. 1. Bên cho thuê phải bảo đảm quyền sử dụng tài sản ổn định cho bên thuê. 2. Trường hợp có tranh chấp về quyền sở hữu đối với tài sản thuê mà bên thuê không được sử dụng tài sản ổn định thì bên thuê có quyền đơn phương chấm dứt thực hiện hợp đồng và yêu cầu bồi thường thiệt hại
4. [BLDS 2015] Điều 15. Hủy quyết định cá biệt trái pháp luật của cơ quan, tổ chức, người có thẩm quyền. Khi giải quyết yêu cầu bảo vệ quyền dân sự, Tòa án hoặc cơ quan có thẩm quyền khác có quyền hủy quyết định cá biệt trái pháp luật của cơ quan, tổ chức, người có thẩm quyền. Trường hợp quyết định cá biệt bị hủy thì quyền dân sự bị xâm phạm được khôi phục và có thể được bảo vệ bằng các phương thức quy định tại Điều 11 của Bộ luật này. Chương III CÁ NHÂN Mục 1 NĂNG LỰC PHÁP LUẬT DÂN SỰ, NĂNG LỰC HÀNH VI DÂN SỰ CỦA CÁ NHÂN
5. [BLDS 2015] Điều 77. Điều lệ của pháp nhân. 1. Pháp nhân phải có điều lệ trong trường hợp pháp luật có quy định. 2. Điều lệ của pháp nhân có những nội dung chủ yếu sau đây: a) Tên gọi của pháp nhân; b) Mục đích và phạm vi hoạt động của pháp nhân; c) Trụ sở chính; chi nhánh, văn phòng đại diện, nếu có; d) Vốn điều lệ, nếu có; đ) Đại diện theo pháp luật của pháp nhân; e) Cơ cấu tổ chức; thể thức cử, bầu, bổ nhiệm, miễn nhiệm, cách chức, nhiệm vụ và quyền hạn của các chức danh của cơ quan điều hành và các cơ quan khác; g) Điều kiện trở thành thành viên hoặc không còn là thành viên của pháp nhân, nếu là pháp nhân có thành viên; h) Quyền, nghĩa vụ của các thành viên, nếu là pháp nhân có thành viên; i) Thể thức thông 
According to the given rules, please evaluate whether the court accepts the plaintiff's claims in whole or in part.
```
**Response**
```
Dựa trên các quy định được cung cấp, chúng ta sẽ phân tích từng yêu cầu của nguyên đơn:

1. Yêu cầu về việc trả lại thửa đất 18 và thửa 53 cho gia đình ông C:
   - Theo quy định tại Điều 175 BLDS 2015, ranh giới giữa các bất động sản liền kề được xác định theo thoả thuận hoặc quyết định của cơ quan nhà nước có thẩm quyền. Trong trường hợp này, ranh giới giữa thửa đất 18 và thửa 53 đã tồn tại từ 30 năm trở lên mà không có tranh chấp, nên nguyên đơn có quyền yêu cầu trả lại thửa đất này.
   - Tuy nhiên, việc này cần được xác định cụ thể qua quá trình tranh chấp và thẩm định.

2. Yêu cầu về việc trả lại thửa đất 77,9m2 đã thu hồi và 6 cây bạch đàn đã giải tỏa:
   - Theo quy định tại Điều 175 BLDS 2015, việc thu hồi đất và giải tỏa cây cối phải tuân theo quy định của pháp luật. Trong trường hợp này, việc thu hồi và giải tỏa đã được thực hiện, nên yêu cầu này không được chấp nhận.

3. Yêu cầu về việc giữ nguyên khuôn viên lăng mộ của cụ Đào Thị Toại:
   - Theo quy định tại Điều 175 BLDS 2015, quyền sử dụng đất không được thay đổi mốc giới ngăn cách, kể cả trường hợp ranh giới là kênh, mương, hào, rãnh, bờ ruộng. Do đó, yêu cầu này không được chấp nhận.

4. Yêu cầu về việc bồi thường công sức bảo quản, giữ gìn đất:
   - Theo quy định tại Điều 15 BLDS 2015, khi giải quyết yêu cầu bảo vệ quyền dân sự, Tòa án hoặc cơ quan có thẩm quyền khác có quyền hủy quyết định cá biệt trái pháp luật của cơ quan, tổ chức, người có thẩm quyền. Do đó, yêu cầu này có thể được chấp nhận nếu có quyết định trái pháp luật.

Kết luận: Yêu cầu của nguyên đơn được chấp nhận (trong đó yêu cầu về việc trả lại thửa đất 18 và thửa 53 cho gia đình ông C được chấp nhận, còn các yêu cầu khác không được chấp nhận).

Yêu cầu của nguyên đơn được chấp nhận (trong đó yêu cầu về việc trả lại thửa đất 18 và thửa 53 cho gia đình ông C được chấp nhận, còn các yêu cầu khác không được chấp nhận).
```

## A.2#1 — abductive (plaintiff)

**Prompt**
```
Considering the following facts:
1. Trong  đơn  khởi  kiện  ngày  05/01/2016,  quá trình giải quyết  vụ  án  và  tại
2. phiên  tòa,  nguyên  đơn  ông  Nguyễn  Hữu  C,  người  đại  diện  theo  ủy  quyền  của
3. nguyên  đơn  ông  Nguyễn  Văn  G  và  người  có  quyền  lợi  nghĩa  vụ  liên  quan  bà
4. Đàm Thị T trình bày:
5. Cha mẹ ông C là cụ Nguyễn Hữu Nhị và cụ Lê Thị Hường đều mất không
6. để lại di chúc. Di sản của 2 cụ là mảnh đất có diện tích 1845m2 thuộc thửa 539
7. tại xóm 4 xã T S, Đô Lương, Nghệ An được Nhà nước giao theo chính sách di
8. dân từ năm 1979. Hai cụ có 3 người con gồm ông C, ông Nguyễn Hữu Thắng và
9. bà Nguyễn Thị Thìn. Năm 2009, ông C, ông Thắng và bà Thìn đã họp bàn với
10. nhau  và  thống  nhất  giao  toàn  bộ  di  sản  của  2  cụ  cho  ông  C  được  toàn  quyền
11. quản lý, sử dụng.
12. Cũng  năm  1979,  vợ  chồng  ông  C  cũng  được  giao  thửa  đất  540,  diện  tích
13. 2110 m2 để làm nhà ở ngay bên cạnh đất cụ Nhị - cụ Hường. Đến năm 1990, do
14. bão  làm  đổ  nhà  nên vợ  chồng  ông  C tạm  chuyển  đến vị trí  khác  làm  nhà  ở và
15. được nhà nước cấp Giấy chứng nhận quyền sử dụng đất  đối với phần đất mới.
16. Sau khi 2 cụ mất, ông C là người con duy nhất còn sinh sống tại địa phương nên
17. trực tiếp quản lý đất các cụ. Năm 1995, ông C cho ông L, ông T mượn một phần
18. để phơi rơm, trồng sắn và một phần cho xã mượn làm sân bóng cho thiếu niên
19. xóm 4.
20. Ông C, bà T khẳng định không có việc gia đình bỏ hoang thửa 539 + 540 từ
21. năm 1984 và ông C vẫn quản lý đất của cha mẹ, vợ chồng ông thông qua việc
22. cho ông T, ông L và xã mượn tạm sử dụng, các cây cối của gia đình trồng vẫn
23. tồn tại trên đất.
24. Tuy nhiên, quá trình mượn đất, ông T, ông L đã trồng cây lâu năm trên đất
25. rồi không chịu trả nữa. Hiện trạng trên thửa đất 18 (ông L đang sử dụng) có 09
26. cây bạch đàn do anh em ông C trồng từ những năm 1980 và các cây cối trên đất
27. ông L trồng thêm từ sau 1994; trên thửa đất 53 (ông T đang sử dụng) có ngôi mộ
28. của cụ Đào Thị Toại và những cây cối do ông T mới trồng lên trên đất.
29. Sau  khi  họp  bàn  phân  chia  di  sản,  ông  C  làm  đơn  xin  lập  hồ  sơ  cấp  giấy
30. chứng nhận quyền sử dụng đất đối với thửa 539 và 540 (có một phần thuộc thửa
31. 18 và thửa 53 - Bản đồ địa chính) thì UBND xã T S không đồng ý vì cho rằng
32. đó là đất của UBND xã chứ không phải của gia đình ông còn ông T, ông L cũng
33. không  chịu  thu  hoạch  cây  cối  trên  đất  để  trả  lại  cho  ông  bà  nên  đã  phát  sinh
34. tranh chấp từ năm 2005 cho đến nay.
35. Nay ông bà yêu cầu ông T, ông L phải thu hoạch cây cối và trả lại thửa đất
36. 18 và thửa 53, tờ bản đồ 13 thuộc xóm 4 xã T S, Đô Lương, Nghệ An cho vợ chồng  ông  bà  theo  kết  quả  đo  đạc  thẩm  định  tại  chỗ  ngày  12/6/2017;  ông  bà
37. không đồng ý bồi thường tiền cây cối trên đất cũng như công sức bảo quản giữ
38. gìn đất cho ông T và ông L vì họ đã được hưởng lợi từ việc sử dụng đất. Về ngôi
39. mộ của cụ Đào Thị Toại trên thửa đất 53 thì ông bà thống nhất giữ lại toàn bộ
40. khuôn viên ngôi mộ như đề nghị của ông H và cụ V.
41. Ngoài ra, quá trình tranh chấp đất đai với ông T, ông L, ông C có làm đơn
42. yêu  cầu  UBND  xã  T  S,  UBND  huyện  Đ  L  giải  quyết.  Ông  đã  nhận  được  các
43. Quyết định: Quyết định số 310/UBND.TN ngày 26/9/2012 của UBND huyện Đ
44. L; Quyết định số 940/QĐ-UBND ngày 27/5/2013 của Chủ tịch UBND huyện Đ
45. L;  Quyết  định  số  14/QĐ-UBND  ngày  05/3/2012  của  UBND  xã  T  S  và  Quyết
46. định  số  27/QĐ-UBND  ngày  26/4/2012  của  Chủ  tịch  UBND  xã  TS.  Theo  ông,
47. các Quyết định này đều vi phạm pháp luật, làm ảnh hưởng đến quyền và lợi ích
48. hợp pháp của gia đình ông bởi vì:
49. - Đây là đất của bố mẹ ông và vợ chồng ông, đã có trong hồ sơ địa chính từ
50. năm  1983 – 1984 nhưng  UBND xã  T  S, UBND  huyện  Đ  L kết luận  không  có
51. giấy tờ là không đúng.
52. - Gia đình ông không bỏ hoang đất từ năm 1984 mà cho UBND xã, ông T,
53. ông  L  mượn  đất  từ  năm  1995.  Khoảng  thời  gian  từ  1984  đến  1995,  vợ  chồng
54. ông  C vẫn  quản lý sử  dụng bình thường. Đồng  thời, trên đất vẫn  tồn tại nhiều
55. cây bạch đàn do ông C và em trai là ông Thắng trồng từ năm 1980.
56. - Việc chính quyền không thu thuế không phải là lỗi của gia đình ông bà vì
57. thời  gian  1995  –  2005,  ông  C  cho  người  khác  mượn  đất  sử  dụng  chứ  ông  bà
58. không trực tiếp sử dụng, hơn nữa chính quyền cũng không thông báo cho ông bà
59. việc phải thực hiện nghĩa vụ gì cả.
60. - Ông bà không kê khai xin cấp Giấy chứng nhận quyền sử dụng đất khi có
61. Nghị định 64CP vì lúc đó không am hiểu pháp luật và cũng do đang cho người
62. khác mượn đất.
63. - Về hình thức, quy trình giải quyết khiếu nại đều vi phạm pháp luật. Trong
64. đơn ngày 12/12/2011, ông C yêu cầu giải quyết tranh chấp đất giữa ông với ông
65. T – ông L nhưng UBND xã lại giải quyết khiếu nại bằng Quyết định 14 là không
66. đúng vì ông không khiếu nại quyết định hành chính hay hành vi hành chính. Do
67. vậy, chủ tịch UBND huyện giải quyết khiếu nại lần 2 đối với Quyết định 14 là
68. cũng vi phạm pháp luật. Đối với Quyết định 27 thì xã giải quyết việc ông C yêu
69. cầu  cấp  giấy  chứng  nhận  quyền  sử  dụng  đất  là  không  đúng  thẩm  quyền  vì
70. UBND xã chỉ có quyền lập hồ sơ, không có quyền cấp giấy. Quyết định 310 của
71. UBND huyện Đ L vi phạm thẩm quyền vì đáng lẽ là thuộc thẩm quyền của Chủ
72. tịch UBND huyện Đ L.
73. - Riêng nội dung liên quan đến 77,9m2 đất đã thu hồi và 06 cây bạch đàn
74. đã giải tỏa để làm đường liên xã Trung  – Xuân được xem xét trong các Quyết
75. định trên thì ông không đề nghị Tòa án giải quyết vì không liên quan đến vụ án.
76. Cụ thể trong từng Quyết định, ông C yêu cầu Tòa án hủy những phần sau:
77. Quyết  định  14:  yêu  cầu  hủy  toàn  bộ  vì  Quyết  định  căn  cứ  vào  nội  dung
78. phần kết luận gia đình ông C không có nhu cầu sử dụng và phần xác minh đất do
79. UBND xã quản lý là không đúng.
80. Quyết định 27: yêu cầu hủy tòan bộ bởi nội dung kết luận ông khiếu nại sai
81. và đề nghị cấp giấy không có cơ sở.
82. Quyết định 940: hủy toàn bộ bởi các nội dung kết luận đất không phải của
83. ông Chiến là vi phạm.
84. Quyết định 310: chỉ yêu cầu hủy nội dung kết luận việc ông C yêu cầu cấp
85. lại quyền sử dụng đất 5419m2 là không có cơ sở xem xét giải quyết, Quyết định
86. xác  định  “thực  chất  đất  không  thuộc  quyền  sử  dụng  của  gia  đình  ông  C”;  xác
87. định UBND xã T S là chủ sử dụng đất theo sổ mục kê, sơ đồ kỹ thuật thửa đất
88. và phần nội dung giao cho UBND xã T S sớm có kế hoạch đưa phần diện tích
89. đất mà ông C, ông T, ông L đang trồng cây lâm nghiệp vào quản lý theo đúng
90. quy định của pháp luật.
91. Quá trình giải quyết vụ án, tại phiên tòa, bị đơn  ông Hoàng Đình T đồng
92. thời là người đại diện theo ủy quyền của bà Nguyễn Thị Th trình bày: năm 1985,
93. thấy thửa đất 540 của vợ chồng ông C (nay có 1 phần là thửa 53) bỏ hoang, vợ
94. chồng ông đã tận dụng để trồng sắn nhưng ông C không có ý kiến gì. Đến năm
95. 1986,  vợ  chồng  ông  đã  trồng  cây  lâu  năm  trên  đất  là  bạch  đàn,  keo  và  đã  thu
96. hoạch nhiều lần (gần nhất là năm 2005). Sau khi ông bà sử dụng đất, xã cũng sử
97. dụng  một  phần  đất  để  làm  sân  bóng  nên  vợ  chồng  ông  dịch  phần  sử  dụng  lên
98. giáp  đường  liên  xã.  Năm  2005, do  thấy  đất  có  giá  trị,  vợ  chồng  ông  C  đòi  vợ
99. chồng ông trả đất nhưng ông bà không đồng ý vì đất đó thuộc quyền quản lý của
100. UBND xã T S. Hiện tại trên đất chỉ có những mầm cây mọc lên từ các gốc cây
101. có trước năm 2005, một số cây cối do vợ chồng ông trồng mới sau này và khu
102. lăng mộ của cụ Toại do con trai cụ là ông Vương Đình H xây trên đất như phản
103. ánh tại Biên bản xem xét thẩm định tại chỗ ngày 12/6/2017 và biên bản định giá
104. tài sản ngày 15/8/2017.
105. Vì  tranh  chấp  kéo  dài  nên  năm  2013,  UBND  xã  T  S  đã  làm  việc  và  vợ
106. chồng ông cam kết tiếp tục canh tác trên đất cho đến khi nhà nước cần, phải thu
107. hồi và không được bồi thường gì cả vì đây là đất thuộc diện quản lý của UBND
108. xã T S. Đến nay, vợ chồng ông cũng như bất cứ cá nhân nào đều chưa được nhà
109. nước  công  nhận quyền  sử  dụng  thửa  đất  53  (khi  đo  đạc  thửa đất này  vào  năm
110. 2003, phần ông bà không sử dụng nhưng cán bộ đo đạc cũng đo vào nên có diện
111. tích  là  1490m2).  Ông  C  yêu  cầu  vợ  chồng  ông  trả  lại  thửa  đất  53,  diện  tích
112. 1119,5m2 thì ông có ý kiến như sau: ông không mượn đất của ông C nên không
113. trả lại cho ông C mà chỉ trả lại cho nhà nước; nếu nhà nước thu hồi thì  ông bà
114. không yêu cầu bồi thường. Nếu tòa án giao đất cho UBND xã T S để UBND xã
115. bán  cho  tổ  chức,  cá  nhân  nào  không  phải  là  nhà  nước  thì  họ  phải  bồi  thường
116. công sức bảo quản, giữ gìn, cải tạo đất trong suốt 30 năm cho  ông bà theo quy
117. định của pháp luật. Còn riêng gia đình ông C thì ông bà không bao giờ trả lại đất
118. nên ông bà không đặt vấn đề bồi hoàn với gia đình ông Chiến. Về ngôi mộ của
119. cụ  Đào  Thị  Toại  trên  đất  53  thì  ông  bà  thống  nhất  giữ  lại  toàn  bộ  khuôn  viên
120. ngôi mộ như đề nghị của ông H và cụ V.
121. Ông bà không có ý kiến gì về yêu cầu hủy các quyết định hành chính như
122. yêu cầu của ông C.
123. Bị  đơn  ông  Hoàng  Đình  L,  người  có  quyền  lợi  và  nghĩa  vụ  liên  quan  bà
124. Đoàn Thị H trình bày: năm 1986, sau khi vợ chồng cụ Nhị mất, vợ chồng ông
125. bà vào trồng sắn trên phần đất mà cụ Nhị bỏ hoang. Lúc này, vợ chồng ông T
126. cũng đã  canh  tác  trên  đất  của  ông  C  bỏ hoang  nhưng  chính quyền  địa phương
127. cũng như các con của cụ Nhị không có ý kiến gì. Sau đó, ông bà bắt đầu trồng
128. cây lấy gỗ như bạch đàn, keo, xoan để phủ xanh đất trống đồi núi trọc, nhà nước
129. không thu bất  cứ  khoản  nghĩa vụ  nào  cũng như  không  hỗ trợ  gì  cho  vợ  chồng
130. ông bà trồng cây lấy gỗ. Do thấy đất có giá trị nên năm 2005 – 2006, ông C xảy
131. ra tranh chấp mặc dù trước đó chẳng có chuyện gì xảy ra. Vì tranh chấp kéo dài
132. nên năm 2013, UBND xã T S đã làm việc và ông bà đã viết cam kết là được xã
133. cho tiếp tục canh tác trên đất đến khi nhà nước cần phải thu hồi và không được
134. bồi thường gì cả vì đây là đất thuộc diện quản lý của UBND xã T S. Đến nay,
135. ông bà cũng như bất cứ cá nhân nào đều chưa được nhà nước công nhận quyền
136. sử dụng thửa đất 18, diện tích (năm 2003 đo đạc thì diện tích là 1141m2). Trên
137. đất  hiện  nay  có  09  cây  bạch  đàn  lá  nhỏ  của  ông  bà  trồng  nhưng  ông  C  đang
138. tranh chấp và các cây cối như phản ánh tại Biên bản xem xét thẩm  định tại chỗ
139. ngày 12/6/2017 và biên bản định giá tài sản ngày 15/8/2017. Nay vợ chồng ông
140. C yêu cầu ông bà trả lại thửa đất 18, diện tích 1114m2 thì ông bà có ý kiến như
141. sau: ông bà không mượn đất của ông C nên không trả lại cho ông C mà chỉ trả
142. lại  cho  nhà  nước;  nếu  nhà  nước  thu  hồi  thì  ông  bà  không  yêu  cầu  bồi  thường.
143. Nếu tòa án giao đất cho UBND xã T S để UBND xã bán cho tổ chức, cá nhân
144. nào không phải là nhà nước thì họ phải bồi thường công sức bảo quản, giữ gìn,
145. cải tạo đất trong suốt 30 năm cho ông bà theo quy định của pháp luật. Còn riêng
146. vợ chồng ông C thì ông bà không bao giờ trả lại đất nên ông bà không đặt vấn
147. đề bồi hoàn với gia đình ông C.
148. Ông bà không có ý kiến gì về yêu cầu hủy các quyết định hành chính như
149. yêu cầu của ông C.
150. Đại diện người có quyền lợi, nghĩa vụ liên quan UBND xã T S, ông Đoàn
151. Văn L trình bày: Năm 1979, hai thửa đất 53 và 18 (tức thuộc một phần thửa 539
152. và một phần thửa 540 theo Bản đồ 299) do ông Nguyễn Hữu C và cụ Nguyễn
153. Hữu Nhị (cha của ông C) sử dụng để xây nhà ở. Từ khi gia đình ông C, cụ Nhị
154. tự bỏ hoang đất thì ông T, ông L có trồng cây trên đất chứ không có việc ông T,
155. ông L mượn đất ông C. Do đất bị bỏ hoang nên với tư cách là cơ quan quản lý
156. đất  đai  ở  địa  phương,  thời  gian  thực  hiện  Nghị  định  64CP  và  thời  điểm  năm
157. 2003, UBND xã T S đã đưa thửa 18, 53 vào sổ mục kê với diện đất thuộc quản
158. lý  của  UBND  xã  (đất  vô  chủ)  mặc  dù  vẫn  chưa  đề  nghị  UBND  huyện  Đ  L  ra
159. Quyết định thu hồi theo quy định của pháp luật. Hai thửa đất này được đưa vào
160. sử dụng từ năm 1979 với mục đích là đất ở nhưng từ năm 1994 đến nay thì đã
161. được sử dụng vào trồng cây lâm nghiệp và hiện tại mục đích sử dụng đất được
162. xác định là đất trồng cây lâu năm.
163. Gia đình ông C chưa bao giờ thực hiện việc kê khai thửa 53 và thửa 18 để
164. xin  cấp  Giấy  chứng  nhận  theo  Nghị  định  64CP;  không  thực  hiện  nghĩa  vụ  tài
165. chính đối với nhà nước và cũng không lập thủ tục phân chia di sản thừa kế của
166. vợ chồng cụ Nhị - cụ Hường. Bản thân gia đình ông C cũng không có giấy tờ gì
167. chứng minh việc mình được quyền sử dụng đất; quá trình sử dụng đất lại không
168. ổn  định,  liên  tục  từ  khi  hình  thành  thửa  đất  đến  nay.  Mặc  dù  hai  thửa  đất  này
169. đang nằm trong diện quản lý của UBND xã T S nhưng nếu ông C có đủ căn cứ
170. để chứng minh quyền sử dụng đất của mình thì phán quyết của Tòa án thế nào
171. UBND  xã  T  S  sẵn  sàng  thực hiện. Còn  yêu  cầu  của ông  C  thì  đề  nghị  Tòa án
172. giải quyết theo pháp luật. Về ngôi mộ của cụ Đào Thị Toại trên thửa đất 18 thì
173. UBND xã T S thống nhất giữ lại toàn bộ khuôn viên ngôi mộ như đề nghị của
174. ông H và cụ V.
175. Đối với yêu cầu hủy Quyết định 14 và 27: ông L cho rằng, do đất chưa có
176. giấy tờ nên khi nhận được đơn của ông C, UBND xã không tiến hành hòa giải
177. mà phải giải quyết theo trình tự khiếu nại.
178. + Về Quyết định 14: về thẩm quyền giải quyết là chủ tịch xã, tuy nhiên,
179. người ký lại ghi tên là “UBND xã”, mặc dù có sai sót nhưng không phải là sai
180. sót lớn vì dù sao người đứng đầu UBND xã cũng là chủ tịch xã.
181. Thời hạn, thời hiệu giải quyết mặc dù đã có gia hạn nhưng vẫn vi phạm
182. theo  quy  định  của  pháp  luật  nhưng  đó  là  do  nội  dung  vụ  việc  phức  tạp,  ông
183. Chiến thường xuyên bổ sung nội dung khiếu nại nhưng vì sơ suất nên xã không
184. lập văn bản xác thực việc bổ sung.
185. Quá trình thực hiện các thủ tục trình tự giải quyết khiếu nại có một số sai
186. sót  như  không  tổ  chức  đối  thoại  nhưng  cũng  đã  thực  hiện  việc  xác  minh  nội
187. dung khiếu nại theo luật định.
188. Về cơ sở pháp lý: đã áp dụng Luật khiếu nại, tố cáo năm 1998 và các đạo
189. luật sửa đổi bổ sung; Nghị quyết 136/2006 hướng dẫn luật khiếu nại, tố cáo.
190. Sau khi giải quyết xong khiếu nại, UBND xã T S đã thực hiện việc giao
191. các văn bản trong thời hạn pháp luật.
192. + Về quyết định số 27: trên cơ sở văn bản chỉ đạo số 97/UBND-TTr ngày
193. 05/4/2012 của UBND huyện Đô Lương, chủ tịch UBND xã T S đã giải quyết lại
194. khiếu nại của ông C. Thẩm quyền ban hành quyết định, thời hạn, thời hiệu giải
195. quyết, trình tự thủ tục cũng như việc giao nhận các văn bản cho ông C là đúng
196. quy định của pháp luật.
197. Việc ông C cho rằng, Chủ tịch xã không có quyền giải quyết khiếu nại đối
198. với  nội  dung  xin  cấp  giấy  chứng  nhận  quyền  sử  dụng  đất  thì  ủy  ban  xã  thừa
199. nhận, tuy nhiên, do ông C không phải là chủ sử dụng đất nên kể cả việc lập hồ
200. sơ ở UBND xã T S cũng không được thực hiện nên chắc chắn là không được cấp
201. giấy chứng nhận.
202. Về cơ sở pháp lý: đã áp dụng Luật khiếu nại, tố cáo năm 1998 và các đạo
203. luật sửa đổi bổ sung; Nghị quyết 136/2006 hướng dẫn luật khiếu nại, tố cáo.
204. Việc  giải  quyết  và  ban  hành  Quyết  định  14  và  27  là  của  chủ  tịch  tiền
205. nhiệm nên việc xử lý hai quyết định này như thế nào thì đề nghị Tòa án căn cứ
206. vào pháp luật để giải quyết.
207. Trong  bản  khai  ngày  08/6/2017,  người  đại  diện  theo  ủy  quyền  của  Chủ
208. tịch  UBND  huyện  Đ  L,  UBND  huyện  Đ  L,  ông Nguyễn  Trọng H  trình bày  đối
209. với yêu cầu hủy hai quyết định 940 và 310:
210. + Đối với Quyết định 940:
211. Trên cơ sở đơn khiếu nại lần 2 của ông C (nay đơn đã bị thất lạc), đối với
212. Quyết định giải quyết khiếu nại số 14 của UBND xã TS, Chủ tịch UBND huyện
213. Đ  L  giải  quyết  khiếu  nại và ban hành  Quyết  định  là phù hợp thẩm  quyền  theo
214. quy  định  tại  Luật  Tổ  chức  HĐND  và  UBND  ngày  26/11/2003;  Luật  khiếu  nại
215. ngày 11/11/2011;
216. Thời  hạn  giải  quyết  đơn  có  sự  vi  phạm;  cơ  sở  pháp  lý  ban  hành  Quyết
217. định là Luật khiếu nại ngày 11/11/2011 và Nghị định số: 75/2012/NĐ-CP ngày
218. 03/10/2012  của  Chính  phủ;  Luật  đất  đai  ngày  26/11/2003  và  Nghị  định  số:
219. 84/2007/NĐ-CP ngày 29/10/2004 của Chính phủ;
220. Cơ  sở  thực  tế:  qua  kiểm  tra  hồ  sơ  địa  chính  lưu  tại  UBND  xã  T  S,  Văn
221. phòng đăng ký quyền sử dụng đất huyện Đ L và kiểm tra thực tế nguồn gốc, quá
222. trình sử dụng đất của ông C và cụ Nhị thì khẳng định:
223. Hộ ông C và cụ Nhị (bố của ông C) được UBND xã T S giao thửa đất nói
224. trên để xây dựng nhà ở từ năm 1979. Khoảng năm 1980 do bị lốc làm hỏng nhà
225. nên năm 1981 ông C di chuyển nhà sang khu vực đồi Cồn Vạng ở và nay được
226. UBND huyện cấp đổi giấy chứng nhận quyền sử dụng đất ngày 31/12/2005, với
227. diện tích 3.050 m2, thửa đất số 407, tờ bản đồ số 13.
228. Phần diện tích còn lại hộ cụ Nhị tiếp tục sử dụng đến khi các cụ qua đời,
229. khoảng năm 1983 – 1984. Đến năm 1987 – 1988 ông C tiến hành tháo dỡ ngôi
230. nhà do cụ Nhị để lại, từ đó trở đi thửa đất trước đây hộ ông C và hộ cụ Nhị bỏ
231. hoang không ai sử dụng. Do thấy đất bỏ hoang hộ ông T và ông L (nhà liền kề)
232. đã  tiến  hành  trồng  cây  lâm  nghiệp  và  trồng  cây  hàng  năm  khác  trên  một  phần
233. diện tích của 02 thửa đất nói trên. Năm 1994 UBND xã T S đã đồng ý cho Ban
234. cán sự xóm 4 sử dụng một phần diện tích khu đất đó để làm sân bóng của xóm.
235. Năm 2004 UBND xã đã tiến hành quy hoạch lại hệ thống sân bóng các xóm trên
236. địa bàn toàn xã trong đó có sân bóng xóm 4, sau khi hoàn thành việc san lấp mặt
237. bằng  sân  bóng  mới,  thì  phần  diện  tích  sân  bóng  cũ  lại  tiếp  tục  bỏ  hoang,  đến
238. tháng 10/2005 ông Nguyễn Hữu C làm đơn kiến nghị gửi UBND xã T S đề nghị
239. cấp giấy chứng nhận quyền sử dụng đất để trồng cây lâm nghiệp, đồng thời ông
240. C đã tự ý trồng cây lâm nghiệp từ tháng 10/2005 đến nay.
241. Hộ  gia  đình  ông  C  không  thực  hiện  một  khoản  nghĩa  vụ  tài  chính  nào  liên
242. quan đến thửa đất mà hiện nay ông C đề nghị cấp giấy chứng nhận quyền sử dụng
243. đất (từ khoảng năm 1983 – 1984 cụ Nhị qua đời đến nay).
244. Hiện nay trên khu vực đất ông C có đơn kiến nghị cấp giấy chứng nhận có
245. 03 hộ gia đình đang sản xuất  (trồng cây lâm nghiêp); Cụ thể: 1 phần diện tích
246. ông Nguyễn Hữu C trồng cây lâm nghiệp (tràm) từ tháng 10/2005 với diện tích
247. 3.252,5m2, số cây ông C trồng hiện nay đang do ông C quản lý. Một phần diện
248. tích do hộ ông T sử dụng trồng bạch đàn có diện tích 1.103,2 m2 và một phần do
249. hộ ông L sử dụng trồng bạch đàn có diện tích: 1.103,3m2; Như vậy trên thực địa
250. có 03 thửa đất. Hiện nay 02 thửa đất do ông T và ông L sử dụng chỉ còn lại một
251. số cây bạch đàn trồng từ những năm 1989 - 1990 ở xung quanh, phần diện tích
252. còn lại đang bỏ hoang.
253. Căn cứ vào Khoản 1 Điều 46;  Khoản 19 Điều 4; Khoản 1 + khoản 4 Điều
254. 50 Luật Đất đai năm 2003; Điểm a, Khoản 1, Điều 3 Nghị định số 84 thì khẳng định,
255. khiếu nại của ông C đối với Quyết định số 14 là sai vì:
256. Ông C không xuất trình được bất kỳ giấy tờ pháp lý nào chứng minh là đất
257. của ông.
258. Gia đình ông không trực tiếp sử dụng ổn định, liên tục 2 thửa đất 53 + 18 từ
259. năm 1988 đến nay, không thực hiện đăng ký quyền sử dụng đất tại cơ quan có thẩm
260. quyền,  không  thực  hiện  nghĩa  vụ  tài  chính  đối  với  nhà  nước  nên  UBND  xã  T  S
261. không làm thủ tục để đề nghị cấp có thẩm quyền cấp giấy chứng nhận quyền sử
262. dụng đất cho gia đình ông là đúng quy định của pháp luật.
263. + Đối với Quyết định 310: ngày 03/5/2012, ông C gửi đơn kiến nghị yêu
264. cầu giải quyết việc cấp lại quyền sử dụng đất 5419 và bồi thường 77,9m2 và 06
265. cây đường kính 30cm-40cm khi giải tỏa mặt bằng mở đường giao thông liên xã.
266. UBND  huyện  đã  giao  phòng  tài  nguyên  –  môi  trường  kiểm  tra  và  ban  hành
267. Quyết định 310 với nội dung không chấp nhận yêu cầu của ông C cũng vì các lý
268. do được nêu trong nội dung của Quyết định 940.
269. Ông H không chấp nhận yêu cầu hủy Quyết định 940 và Quyết định 310
270. của ông C và đề nghị Tòa án giải quyết theo pháp luật.
271. Người  có  quyền  lợi,  nghĩa  vụ  liên  quan  cụ  Vương  Đình  V,  ông  Vương
272. Đình H trình bày: cụ Đào Thị Toại là vợ cụ V và là mẹ của ông H. Cụ Toại mất
273. năm 1953 và chỉ có ông H là con. Do cụ V, ông H chuyển ra Thái Nguyên sinh
274. sống  nên  sau  này,  khi  tìm  được  mộ  thì  ông  H  đã  tiến  hành  xây  cất  lăng  trên
275. khuôn viên thửa 53 mà các đương sự tranh chấp. Nay ông H, cụ V yêu cầu, nếu
276. ai là người được Tòa án giao quyền sử dụng đất thì giữ nguyên khuôn viên lăng
277. mộ của cụ Toại để gia đình thực hiện việc thờ cúng theo phong tục tập quán và
278. không có yêu cầu gì thêm.
279. Người làm chứng ông Vương Đình Đơủ trình bày: do thời gian dài, tuổi
280. cao nên ông không nhớ rõ sự việc nên đề nghị Tòa án căn cứ vào những thông
281. tin  ông  cung  cấp  cho  UBND  các  cấp  khi  giải  quyết  khiếu  nại  và  cho  Tòa  án
282. trong quá trình giải quyết vụ án để xác định tính khách quan của các sự kiện đã
283. diễn  ra  thời gian ông  đang giữ  chức  vụ  Trưởng  ban quản  lý  ruộng đất  xã  T  S.
284. Tuy nhiên, ông khẳng định, khi xã trưng dụng đất làm sân bóng thì ông T, ông L
285. chưa sử dụng đất như bây giờ.
286. Người làm chứng bà Thìn thừa nhận: cha mẹ bà có để lại di sản là thửa
287. đất  539  mà  hiện  nay,  một  phần  thửa  đất  này  do  vợ  chồng  ông  L  tự  ý  sử  dụng
288. trồng  cây  (ghi  nhận tại thửa  mới  là  18, diện tích 1114m2), hiện vẫn  còn nhiều
289. cây bạch đàn trên đất do cha bà, anh trai và bà trồng từ năm 1980  - 1981. Năm
290. 2009, do bà và ông Thắng ở xa nên anh em đã họp bàn chia di sản của cha mẹ
291. với nội dung giao lại toàn bộ di sản cho ông C sở hữu, quản lý, sử dụng vì ông C
292. là anh cả đồng thời ở tại chỗ làm nhiệm vụ thờ cúng cha mẹ.  Nay bà không có
293. quyền lợi, nghĩa vụ gì liên quan đến vụ án và đề nghị Tòa án bảo vệ quyền sử
294. dụng đất hợp pháp của cha mẹ bà, buộc những người đang chiếm hữu sử dụng di
295. sản của cha mẹ bà phải trả lại cho ông C theo luật định.
296. Người làm chứng ông Thắng vắng mặt tại phiên tòa nhưng trong quá trình
297. thu thập chứng cứ, ông Thắng cũng khẳng định nội dung như trình bày của bà
298. Thìn. Ông Thắng xác định ông không còn quyền lợi, nghĩa vụ gì liên quan đến
299. vụ án và đề nghị Tòa án bảo vệ quyền sử dụng đất hợp pháp của cha mẹ ông,
300. buộc những người đang chiếm hữu sử dụng di sản của cha mẹ ông phải trả lại
301. cho ông C theo luật định (người đại diện theo ủy quyền của ông Thắng – ông G -
302. không bổ sung gì thêm vào trình bày của ông Thắng).
303. Người làm chứng bà Lê Thị Quảng trình bày: bà không nhớ cụ thể về đất
304. của ông C nhưng có sự kiện vào năm 1991 – 1993, cha bà là ông Lê Văn Lĩnh
305. có mượn ông C phần đất mà các đương sự đang tranh chấp để trồng sắn. Năm
306. 1993, sau khi cha bà mất thì bà không biết việc sử dụng đất thuộc về ai nữa.
307. Tại phiên tòa, đại diện Viện kiểm sát nhân dân huyện Đô Lương phát biểu
308. ý kiến theo quy định tại điều 262 Bộ luật tố tụng dân sự như sau:
309. - Về tố tụng: Thẩm phán đã tuân thủ các quy định của Bộ luật tố tụng dân
310. sự trong việc thụ lý vụ án, thông báo thụ lý vụ án, xác định quan hệ tranh chấp,
311. xác minh và thu thập chứng cứ, tổ chức hòa giải cũng như thời hạn giải quyết vụ
312. án.
313. Hội đồng xét xử tuân thủ đúng quy định về thành phần, nguyên tắc xét xử,
314. trình tự tố tụng tại phiên tòa.
315. Thư ký Tòa án thực hiện đúng quy định của Bộ luật tố tụng dân sự.
316. Các đương sự chấp hành nghiêm chỉnh quy định của Bộ luật tố tụng dân
317. sự.
318. -  Về  nội  dung:  sau  khi  phân  tích  các  tình  tiết  của  vụ  án  và  các  tài  liệu,
319. chứng cứ có tại hồ sơ, đại diện Viện kiểm sát đề nghị Hội đồng xét xử áp dụng
320. các quy định tại điều 166, Điều 185, Điều 579 Bộ luật dân sự; Điều 166 Luật đất
321. đai;  Luật  khiếu  nại  tố  cáo  năm  1998;  Luật  khiếu  nại  năm  2011;  Luật  tố  tụng
322. hành  chính:  chấp  nhận  đơn  khởi  kiện  của  ông  C,  buộc  vợ  chồng  ông  T  –  vợ
323. chồng ông L – UBND xã T S trả lại thửa đất 18 và 53 cho gia đình ông C; hủy
324. toàn bộ Quyết định hành chính số 14, số 27, số 940 và một phần Quyết định 310
325. theo quy định của pháp luật.
Considering the following rules: Applicable provisions of Vietnamese law:
1. [BLDS 2015] Điều 175. Ranh giới giữa các bất động sản. 1. Ranh giới giữa các bất động sản liền kề được xác định theo thoả thuận hoặc theo quyết định của cơ quan nhà nước có thẩm quyền. Ranh giới cũng có thể được xác định theo tập quán hoặc theo ranh giới đã tồn tại từ 30 năm trở lên mà không có tranh chấp. Không được lấn, chiếm, thay đổi mốc giới ngăn cách, kể cả trường hợp ranh giới là kênh, mương, hào, rãnh, bờ ruộng. Mọi chủ thể có nghĩa vụ tôn trọng, duy trì ranh giới chung. 2. Người sử dụng đất được sử dụng không gian và lòng đất theo chiều thẳng đứng từ ranh giới của thửa đất phù hợp với quy định của pháp luật và không được làm ảnh hưởng đến việc sử dụng đất của người khác. Người sử dụng đất chỉ được trồng 
2. [BLDS 2015] Điều 155. Không áp dụng thời hiệu khởi kiện. Thời hiệu khởi kiện không áp dụng trong trường hợp sau đây: 1. Yêu cầu bảo vệ quyền nhân thân không gắn với tài sản; 2. Yêu cầu bảo vệ quyền sở hữu, trừ trường hợp Bộ luật này, luật khác có liên quan quy định khác; 3. Tranh chấp về quyền sử dụng đất theo quy định của Luật đất đai; 4. Trường hợp khác do luật quy định
3. [BLDS 2015] Điều 478. Nghĩa vụ bảo đảm quyền sử dụng tài sản cho bên thuê. 1. Bên cho thuê phải bảo đảm quyền sử dụng tài sản ổn định cho bên thuê. 2. Trường hợp có tranh chấp về quyền sở hữu đối với tài sản thuê mà bên thuê không được sử dụng tài sản ổn định thì bên thuê có quyền đơn phương chấm dứt thực hiện hợp đồng và yêu cầu bồi thường thiệt hại
4. [BLDS 2015] Điều 15. Hủy quyết định cá biệt trái pháp luật của cơ quan, tổ chức, người có thẩm quyền. Khi giải quyết yêu cầu bảo vệ quyền dân sự, Tòa án hoặc cơ quan có thẩm quyền khác có quyền hủy quyết định cá biệt trái pháp luật của cơ quan, tổ chức, người có thẩm quyền. Trường hợp quyết định cá biệt bị hủy thì quyền dân sự bị xâm phạm được khôi phục và có thể được bảo vệ bằng các phương thức quy định tại Điều 11 của Bộ luật này. Chương III CÁ NHÂN Mục 1 NĂNG LỰC PHÁP LUẬT DÂN SỰ, NĂNG LỰC HÀNH VI DÂN SỰ CỦA CÁ NHÂN
5. [BLDS 2015] Điều 77. Điều lệ của pháp nhân. 1. Pháp nhân phải có điều lệ trong trường hợp pháp luật có quy định. 2. Điều lệ của pháp nhân có những nội dung chủ yếu sau đây: a) Tên gọi của pháp nhân; b) Mục đích và phạm vi hoạt động của pháp nhân; c) Trụ sở chính; chi nhánh, văn phòng đại diện, nếu có; d) Vốn điều lệ, nếu có; đ) Đại diện theo pháp luật của pháp nhân; e) Cơ cấu tổ chức; thể thức cử, bầu, bổ nhiệm, miễn nhiệm, cách chức, nhiệm vụ và quyền hạn của các chức danh của cơ quan điều hành và các cơ quan khác; g) Điều kiện trở thành thành viên hoặc không còn là thành viên của pháp nhân, nếu là pháp nhân có thành viên; h) Quyền, nghĩa vụ của các thành viên, nếu là pháp nhân có thành viên; i) Thể thức thông 
Please suggest hypotheses to support why the outcome of the case might be the court accepts the plaintiff's claims in whole or in part.
```
**Response**
```
Để xác định liệu yêu cầu của nguyên đơn có được chấp nhận (toàn bộ/một phần) hay không, chúng ta cần phân tích từng yếu tố trong vụ kiện dựa trên các quy định pháp luật Việt Nam. Dựa trên các thông tin cung cấp, tôi sẽ đưa ra một số giả thuyết để hỗ trợ cho kết luận:

1. **Ranh giới đất**: Theo Điều 175 BLDS 2015, ranh giới giữa các bất động sản liền kề được xác định theo thoả thuận hoặc quyết định của cơ quan nhà nước có thẩm quyền. Trong vụ kiện này, ranh giới giữa thửa đất 18 và 53 đã được xác định qua các quyết định hành chính và thỏa thuận giữa các bên. Điều này cho thấy ranh giới đất đã được xác định rõ ràng.

2. **Quyền sử dụng đất**: Theo Điều 155 BLDS 2015, thời hiệu khởi kiện không áp dụng trong trường hợp tranh chấp về quyền sử dụng đất. Do đó, yêu cầu của nguyên đơn về việc đòi lại thửa đất 18 và 53 không bị hạn chế bởi thời hiệu khởi kiện.

3. **Điều lệ pháp nhân**: Theo Điều 77 BLDS 2015, pháp nhân có thể có điều lệ quy định về quyền và nghĩa vụ của các thành viên. Trong vụ kiện này, thửa đất 53 đã được giao cho ông C quản lý và sử dụng, và hiện tại ông C là người duy nhất còn sống tại địa phương. Điều này cho thấy ông C có quyền sử dụng đất hợp pháp.

4. **Quyền sử dụng đất của ông C**: Theo Điều 155 BLDS 2015, không áp dụng thời hiệu khởi kiện trong trường hợp tranh chấp về quyền sử dụng đất. Do đó, yêu cầu của ông C về việc đòi lại thửa đất 53 và yêu cầu bồi thường công sức bảo quản đất cho ông C là hợp pháp.

5. **Quyền sử dụng đất của ông T và ông L**: Theo Điều 155 BLDS 2015, không áp dụng thời hiệu khởi kiện trong trường hợp tranh chấp về quyền sử dụng đất. Tuy nhiên, họ đã trồng cây lâu năm trên đất và không chịu trả lại cho ông C. Điều này cho thấy họ có quyền sử dụng đất hợp pháp nhưng không ổn định.

6. **Quyền sử dụng đất của bà Thìn**: Bà Thìn là người có quyền lợi, nghĩa vụ liên quan và đã giao toàn bộ di sản của cha mẹ cho ông C. Do đó, bà Thìn không có quyền lợi, nghĩa vụ gì liên quan đến vụ án và đề nghị Tòa án bảo vệ quyền sử dụng đất hợp pháp của cha mẹ bà.
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
- outcome: **the court rejects all of the plaintiff's claims**
- converged: True
- accepted hypotheses: