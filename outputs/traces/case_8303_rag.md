# Civil law simulation

## A.1 — rule_based

**Prompt**
```
Considering the following facts:
1. Người có quyền lợi và nghĩa vụ liên quan:
2. - Ông Đỗ Văn T, sinh năm 1960;
3. - Bà Hoàng Thị X, sinh năm 1959;
4. - Anh Đỗ Thanh P, sinh năm 1987;
5. - Chị Chu Thị T, sinh năm 1991;
6. - Cháu Đỗ Minh Đ, sinh năm 2011;
7. - Cháu Đỗ Minh H, sinh năm 2014;
8. Anh P và chị T là bố mẹ đẻ của cháu Đ và H nên anh chị là người đại diện hợp pháp của cháu Đ và cháu H.
9. Cùng địa chỉ: Thôn N, xã P, huyện T, thành phố H.
10. Nguyên đơn trình bày:
11. Ngân hàng QT(gọi tắt là VIB) và vợ chồng bà Đỗ Thị T và ông Chu Văn A có ký kết hợp đồng tín dụng số 020/HĐTD1-VIB038/11 ngày 26/08/2011, số tiền vay hạn mức là 2.200.000.000 đồng (Hai tỷ hai trăm triệu đồng); số tiền đã giải ngân là 2.200.000.000 đồng (Hai tỷ hai trăm triệu đồng) theo Khế ước nhận nợ số 020.01/KUNN1-VIB038/11 ngày 26/08/2011; thời hạn vay: 06 tháng kể từ ngày 26/08/2011; Lãi suất cho vay: 22.5%/năm, điều chỉnh 03 tháng/lần, bằng lãi suất điều chuyển vốn kinh doanh VND kỳ hạn …
12. Về lãi suất: Quá trình thực hiện Hợp đồng Ngân hàng có điều chỉnh lãi suất theo Quyết định điều chỉnh của Ngân hàng VIB. Kể từ ngày khoản vay của bà T, ông A chuyển sang nợ quá hạn là 06/02/2012 thì Ngân hàng áp dụng mức lãi suất là 32.25%/năm cho đến nay.
13. Để đảm bảo nghĩa vụ trả nợ cho khoản vay của bà T và ông A thì ông Đỗ Văn T và bà Hoàng Thị X đã thế chấp tài sản là bất động sản tọa lạc tại thửa đất số 342, tờ bản đồ số 00, diện tích 113.9m2 tại địa chỉ: Khu Đ, xã P, huyện T, thành phố H. Theo Giấy chứng nhận quyền sử dụng đất số AQ 083681, số vào sổ cấp Giấy chứng nhận quyền sử dụng đất: H.02876/QSDĐ/3570/QĐ-UB do UBND huyện T, thành phố H cấp cho ông Đỗ Văn T và bà Hoàng Thị X ngày 29/09/2009. Tài sản này được thế chấp theo Hợp đồng thế …
14. Trong quá trình thực hiện hợp đồng, bà Đỗ Thị T và ông Chu Văn A đã trả 192.458.930 đồng vào tiền lãi, kể từ ngày 06/02/2012 bà T, ông A không trả nợ lãi. Do bà T, ông A vi phạm nghĩa vụ hợp đồng tín dụng nên khoản vay này đã bị chuyển quá hạn từ ngày 06/02/2012.
15. Theo yêu cầu công tác xử lý nợ quá hạn, ngày 19/12/2014, Ngân hàng TMCP phần Quốc tế Việt Nam (VIB) đã bán khoản nợ vay của bà Đỗ Thị T, ông Chu Văn A cho Công ty QLTS (gọi tắt là VAMC). Đến ngày 30/7/2018 Ngân hàng VIB đã mua lại khoản nợ của bà T và ông A từ Công ty VAMC theo hợp đồng mua bán nợ số 2175/2018.BN.VAMC1-VIB.
16. Dư nợ tính đến ngày 06/8/2018, bà T và ông A còn nợ Ngân hàng VIB số tiền là 7.037.902.060đồng, trong đó:
17. Nợ gốc: 2.200.000.000đồng;
18. Nợ lãi trong hạn: 64.757.736đồng;
19. Lãi quá hạn: 4.773.144.324đồng.
20. Ngân hàng VIB yêu cầu bà Đỗ Thị T và ông Chu Văn A thanh toán tổng số tiền 7.037.902.060đ (Bảy tỷ không trăm ba mươi bảy triệu chín trăm linh hai nghìn không trăm sáu mươi đồng) cho Ngân hàng.
21. Bà Đỗ Thị T và ông Chu Văn A tiếp tục trả lãi cho Ngân hàng VIB các khoản lãi, lãi phạt quá hạn phát sinh theo quy định tại Hợp đồng tín dụng đã ký và theo quy định của pháp luật kể từ ngày 07/8/2018 cho đến ngày bà Đỗ Thị T và ông Chu Văn A thanh toán toàn bộ khoản vay.
22. Trường hợp bà Đỗ Thị T và ông Chu Văn A không trả hết nợ hoặc ông Đỗ Văn T và bà Hoàng Thị X không tự nguyện bàn giao tài sản bảo đảm thì Ngân hàng VIB có quyền yêu cầu Cơ quan thi hành án dân sự phát mại khối tài sản mà ông Đỗ Văn T và bà Hoàng Thị X đã thế chấp để thu hồi toàn bộ khoản nợ theo quy định của pháp luật là: Quyền sử dụng 113,9m2 đất cùng các tài sản gắn liền với đất, các quyền và lợi ích phát sinh đối với thửa đất số 342, tờ bản đồ số 00 tại địa chỉ: Khu Đ, xã P, huyện T, thành …
23. Trường hợp toàn bộ khối tài sản thế chấp sau khi xử lý phát mại mà không đủ để trả nợ cho Ngân hàng thì bà Đỗ Thị T và ông Chu Văn A tiếp tục thực hiện nghĩa vụ trả nợ cho Ngân hàng VIB cho đến khi tất toán khoản vay.
24. Án phí: Đề nghị Tòa án buộc bà Đỗ Thị T và ông Chu Văn A phải chịu toàn bộ án phí Kinh doanh thương mại theo quy định của pháp luật.
25. Bị đơn là bà Đỗ Thị T và ông Chu Văn A trình bày:
26. Ngày 26/08/2011, vợ chồng bà Đỗ Thị T và ông Chu Văn A và ngân hàng VIB có ký kết Hợp đồng tín dụng số 020/HĐTD1-VIB038/11 ngày 26/08/2011, số tiền vay hạn mức là 2.200.000.000 đồng (Hai tỷ hai trăm triệu đồng); số tiền đã giải ngân là 2.200.000.000 đồng (Hai tỷ hai trăm triệu đồng). Về nội dung của Hợp đồng như nguyên đơn trình bày là đúng.
27. Để đảm bảo nghĩa vụ trả nợ của vợ chồng bà Đỗ Thị T và ông Chu Văn A, bố mẹ của bà Đỗ Thị T là ông Đỗ Văn T và bà Hoàng Thị X đã thế chấp tài sản của mình là: Quyền sử dụng đất cùng các tài sản gắn liền với đất, các quyền và lợi ích phát sinh đối với 113.9m2 đất, thửa đất số 342, tờ bản đồ số 00 tại địa chỉ: Khu Đ, C, xã P, huyện T, thành phố H. Theo Giấy chứng nhận quyền sử dụng đất số AQ 083681, số vào sổ cấp Giấy chứng nhận quyền sử dụng đất: H.02876/QSDĐ/3570/QĐ-UB do UBND huyện T, thành …
28. Quá trình thực hiện hợp đồng, vợ chồng bà Đỗ Thị T và ông Chu Văn A đã trả được một phần nợ lãi. Do kinh tế suy thoái làm ăn kinh doanh thua lỗ nên không có tiền để tiếp tục trả lãi cho Ngân hàng như đã thỏa thuận.
29. Bà Đỗ Thị T và ông Chu Văn A xác nhận số nợ tính đến ngày 06/8/2018 là 7.037.902.060đồng, trong đó:
30. Nợ gốc: 2.200.000.000đồng;
31. Nợ lãi trong hạn: 64.757.736đồng;
32. Lãi quá hạn: 4.773.144.324đồng.
33. Quá trình thực hiện hợp đồng Ngân hàng đã điều chỉnh lãi suất theo đúng thỏa thuận tại Hợp đồng tín dụng đã ký nên về số tiền gốc và tiền lãi trong hạn, lãi quá hạn Ngân hàng yêu cầu bà Đỗ Thị T và ông Chu Văn A không có ý kiến gì.Hiện tại ngân hàng khởi kiện, bà Đỗ Thị T và ông Chu Văn A đồng ý trả số nợ gốc và xin miễn toàn bộ khoản nợ lãi.Nếu trong trường hợp bà Đỗ Thị T và ông Chu Văn A không trả được nợ thì bà Đỗ Thị T và ông Chu Văn A đồng ý trả lãi phát sinh theo yêu cầu của Ngân hàng và …
34. Người có quyền lợi và nghĩa vụ liên quan ông Đỗ Văn T và bà Hoàng Thị X trình bày trong bản tự khai như sau:
35. Ngày 26/11/2011 ông Đỗ Văn T và bà Hoàng Thị X có ký Hợp đồng thế chấp với Ngân hàng VIB với nội dung: ông Đỗ Văn T và bà Hoàng Thị X thế chấp toàn bộ quyền sử dụng 113,9m2 đất, thửa đất số 342, tờ bản đồ số 00, địa chỉ: Khu Đ, C, xã P, huyện T, thành phố H theo Giấy chứng nhận quyền sử dụng đất số: AQ 083681, số vào sổ cấp giấy chứng nhận quyền sử dụng đất H.02876/QSDĐ/3570/QĐ – UB do UBND huyện Thạch Thất cấp cho ông Chu Văn Tiến và bà Hoàng Thị X ngày 29/9/2009 để bảo lãnh cho khoản vay của …
36. Tại thời điểm thế chấp thì thửa đất không có tài sản trên đất.
37. Đến năm 2012 ông Đỗ Văn T và bà Hoàng Thị X cho vợ chồng con trai là Đỗ Thanh P, sinh năm 1987 và con dâu là Chu Thị T, sinh năm 1991 ra ở riêng, anh chị đã xây nhà 03 tầng trên thửa đất thế chấp.
38. Hiện nay toàn bộ nhà và đất là do gia đình anh Đỗ Thanh P quản lý sử dụng gồm: Đỗ Thanh P, Chu Thị T, cháu Đỗ Minh Đ và cháu Đỗ Minh H.
39. Ngân hàng khởi kiện yêu cầu chị Tân, anh Anh trả nợ nhưng do các con hiện nay kinh tế khó khăn, không có khả năng trả nợ nên ông Đỗ Văn T và bà Hoàng Thị X đồng ý để Ngân hàng kê biên phát mại tài sản thế chấp để trả nợ cho Ngân hàng.
40. Trong trường hợp Ngân hàng phát mại tài sản thế chấp thì ông Đỗ Văn T và bà Hoàng Thị X đề nghị Ngân hàng thanh toán trả con trai giá trị ngôi nhà và các công trình xây trên đất.
41. Người có quyền lợi và nghĩa vụ liên quan anh Đỗ Thanh P và chị Chu Thị T trình bày trong bản tự khai như sau:
42. Ngày 30/5/2011 bố mẹ của anh Đỗ Thanh P và chị Chu Thị T là Đỗ Văn T và Hoàng Thị X có thế chấp cho Ngân hàng VIB thửa đất số 342, tờ bản đồ số 00, diện tích 113,9m2, địa chỉ: Khu Đ, C, xã P, huyện T, thành phố H theo Giấy chứng nhận quyền sử dụng đất số: AQ 083681, số vào sổ cấp giấy chứng nhận quyền sử dụng đất H.02876/QSDĐ/3570/QĐ – UB do UBND huyện Thạch Thất cấp cho ông Chu Văn Tiến và bà Hoàng Thị X ngày 29/9/2009 để bảo lãnh cho khoản vay chị là Đỗ Thị T và anh Chu Văn A tại Ngân hàng …
43. Tại thời điểm thế chấp thì thửa đất không có tài sản trên đất.
44. Năm 2012 anh Đỗ Thanh P và chị Chu Thị T được bố mẹ cho ra ở riêng trên thửa đất đó. Vợ chồng anh Đỗ Thanh P và chị Chu Thị T đã xây nhà 02 tầng 01 tum.
45. Hiện nay toàn bộ tài sản thế chấp là do gia đình anh Đỗ Thanh P quản lý.
46. Ngân hàng khởi kiện yêu cầu sử lý tài sản thế chấp để trả nợ cho anh Anh và chị Tân, anh Đỗ Thanh P và chị Chu Thị T cũng đồng ý.
47. Đối với tài sản trên đất là ngôi nhà hai tầng một tum do vợ chồng anh Đỗ Thanh P và chị Chu Thị T xây dựng, anh Đỗ Thanh P và chị Chu Thị T cũng đồng ý để Ngân hàng phát mại.
48. Trong trường hợp bán tài sản thế chấp thì anh Đỗ Thanh P và chị Chu Thị T sẽ tự thỏa thuận với Ngân hàng về giá trị tài sản trên đất.
49. Về tài liệu Tòa thu thập:
50. Theo biên bản thẩm định tại chỗ ngày 27/6/2018, tài sản thế chấp thuộc quyền sở hữu của ông Đỗ Văn T và bà Hoàng Thị X trên đất gồm: 01 nhà hai tầng và 01 tum lợp mái tôn xây dựng năm 2011 bê tông cốt thép kiên cố diện tích 50m2/tầng, nhà chưa sơn; 01 lán lợp tôn, tường gạch diện tích 50m2 xây dựng năm 2011. Hiện tại sinh sống trên đất gồm: Anh Đỗ Thanh P, chị Chu Thị T, cháu Đỗ Minh Đ và cháu Đỗ Minh H.
51. Theo bảng tính lãi ngày 06/8/2018 do Ngân hàng cung cấp thì từ ngày 26/8/2011 đến ngày 06/2/2012, Ngân hàng có điều chỉnh lãi suất và số tiền lãi trong hạn là 64.757.736đ theo đúng thỏa thuận tại Hợp đồng tín dụng.
52. Kể từ ngày 06/02/2012 bà T và ông A không trả gốc và lãi, Ngân hàng đã chuyển sang nợ lãi quá hạn thì Ngân hàng không điều chỉnh lãi suất và áp dụng mức lãi suất quá hạn là 32,25%/năm với số tiền 4.773.144.324 đồng (trong đó lãi trên dư nợ gốc là: 4.635.400.000, lãi trên dư nợ lãi chậm trả là 137.744.324 đồng).
Considering the following rules: Applicable provisions of Vietnamese law:
1. [BLDS 2015] Điều 307. Thanh toán số tiền có được từ việc xử lý tài sản cầm cố, thế chấp. 1. Số tiền có được từ việc xử lý tài sản cầm cố, thế chấp sau khi thanh toán chi phí bảo quản, thu giữ và xử lý tài sản cầm cố, thế chấp được thanh toán theo thứ tự ưu tiên quy định tại Điều 308 của Bộ luật này. 2. Trường hợp số tiền có được từ việc xử lý tài sản cầm cố, thế chấp sau khi thanh toán chi phí bảo quản, thu giữ và xử lý tài sản cầm cố, thế chấp lớn hơn giá trị nghĩa vụ được bảo đảm thì số tiền chênh lệch phải được trả cho bên bảo đảm. 3. Trường hợp số tiền có được từ việc xử lý tài sản cầm cố, thế chấp sau khi thanh toán chi phí bảo quản, thu giữ và xử lý tài sản cầm cố, thế chấp nhỏ hơn giá trị nghĩa vụ được bảo
2. [BLDS 2015] Điều 325. Thế chấp quyền sử dụng đất mà không thế chấp tài sản gắn liền với đất. 1. Trường hợp thế chấp quyền sử dụng đất mà không thế chấp tài sản gắn liền với đất và người sử dụng đất đồng thời là chủ sở hữu tài sản gắn liền với đất thì tài sản được xử lý bao gồm cả tài sản gắn liền với đất, trừ trường hợp có thỏa thuận khác. 2. Trường hợp thế chấp quyền sử dụng đất mà người sử dụng đất không đồng thời là chủ sở hữu tài sản gắn liền với đất thì khi xử lý quyền sử dụng đất, chủ sở hữu tài sản gắn liền với đất được tiếp tục sử dụng đất trong phạm vi quyền, nghĩa vụ của mình; quyền và nghĩa vụ của bên thế chấp trong mối quan hệ với chủ sở hữu tài sản gắn liền với đất được chuyển giao cho người nhận chu
3. [BLDS 2015] Điều 326. Thế chấp tài sản gắn liền với đất mà không thế chấp quyền sử dụng đất. 1. Trường hợp chỉ thế chấp tài sản gắn liền với đất mà không thế chấp quyền sử dụng đất và chủ sở hữu tài sản gắn liền với đất đồng thời là người sử dụng đất thì tài sản được xử lý bao gồm cả quyền sử dụng đất, trừ trường hợp có thỏa thuận khác. 2. Trường hợp chỉ thế chấp tài sản gắn liền với đất mà không thế chấp quyền sử dụng đất và chủ sở hữu tài sản gắn liền với đất không đồng thời là người sử dụng đất thì khi xử lý tài sản gắn liền với đất, người nhận chuyển quyền sở hữu tài sản gắn liền với đất được tiếp tục sử dụng đất trong phạm vi quyền, nghĩa vụ của chủ sở hữu tài sản gắn liền với đất được chuyển giao, trừ trườn
4. [BLDS 2015] Điều 320. Nghĩa vụ của bên thế chấp. 1. Giao giấy tờ liên quan đến tài sản thế chấp trong trường hợp các bên có thỏa thuận, trừ trường hợp luật có quy định khác. 2. Bảo quản, giữ gìn tài sản thế chấp. 3. Áp dụng các biện pháp cần thiết để khắc phục, kể cả phải ngừng việc khai thác công dụng tài sản thế chấp nếu do việc khai thác đó mà tài sản thế chấp có nguy cơ mất giá trị hoặc giảm sút giá trị. 4. Khi tài sản thế chấp bị hư hỏng thì trong một thời gian hợp lý bên thế chấp phải sửa chữa hoặc thay thế bằng tài sản khác có giá trị tương đương, trừ trường hợp có thoả thuận khác. 5. Cung cấp thông tin về thực trạng tài sản thế chấp cho bên nhận thế chấp. 6. Giao tài sản thế chấp cho bên nhận thế chấp để 
5. [BLDS 2015] Điều 318. Tài sản thế chấp. 1. Trường hợp thế chấp toàn bộ bất động sản, động sản có vật phụ thì vật phụ của bất động sản, động sản đó cũng thuộc tài sản thế chấp, trừ trường hợp có thỏa thuận khác. 2. Trường hợp thế chấp một phần bất động sản, động sản có vật phụ thì vật phụ gắn với tài sản đó thuộc tài sản thế chấp, trừ trường hợp có thoả thuận khác. 3. Trường hợp thế chấp quyền sử dụng đất mà tài sản gắn liền với đất thuộc quyền sở hữu của bên thế chấp thì tài sản gắn liền với đất cũng thuộc tài sản thế chấp, trừ trường hợp có thỏa thuận khác. 4. Trường hợp tài sản thế chấp được bảo hiểm thì bên nhận thế chấp phải thông báo cho tổ chức bảo hiểm biết về việc tài sản bảo hiểm đang được dùng để thế ch
According to the given rules, please evaluate whether the court accepts the plaintiff's claims in whole or in part.
```
**Response**
```
Để đánh giá yêu cầu của nguyên đơn, chúng ta cần phân tích từng yếu tố:

1. **Thực hiện nghĩa vụ thế chấp**: Theo hợp đồng tín dụng, ông Đỗ Văn T và bà Hoàng Thị X đã thế chấp tài sản là bất động sản tọa lạc tại thửa đất số 342, tờ bản đồ số 00, diện tích 113.9m2 tại địa chỉ: Khu Đ, xã P, huyện T, thành phố H.

2. **Nguyên đơn yêu cầu thu hồi tài sản thế chấp**: Ngân hàng VIB yêu cầu ông Đỗ Văn T và bà Hoàng Thị X bàn giao tài sản thế chấp để thu hồi toàn bộ khoản nợ.

3. **Nguyên đơn yêu cầu miễn lãi**: Ngân hàng VIB yêu cầu bà Đỗ Thị T và ông Chu Văn A thanh toán tổng số tiền 7.037.902.060đồng, trong đó bao gồm cả nợ lãi quá hạn.

4. **Nguyên đơn yêu cầu phát mại tài sản thế chấp**: Trường hợp tài sản thế chấp sau khi xử lý phát mại không đủ để trả nợ, Ngân hàng VIB có quyền yêu cầu Cơ quan thi hành án dân sự phát mại tài sản thế chấp để thu hồi toàn bộ khoản nợ.

5. **Nguyên đơn yêu cầu miễn hoàn toàn khoản nợ lãi quá hạn**: Ngân hàng VIB yêu cầu miễn toàn bộ khoản nợ lãi quá hạn.

6. **Nguyên đơn yêu cầu miễn hoàn toàn khoản nợ gốc**: Ngân hàng VIB yêu cầu trả toàn bộ nợ gốc 2.200.000.000đồng.

7. **Nguyên đơn yêu cầu miễn hoàn toàn khoản nợ lãi trong hạn**: Ngân hàng VIB yêu cầu trả toàn bộ nợ lãi trong hạn 64.757.736đồng.

8. **Nguyên đơn yêu cầu miễn hoàn toàn khoản nợ lãi quá hạn**: Ngân hàng VIB yêu cầu trả toàn bộ lãi quá hạn 4.773.144.324đồng.

Từ các quy định pháp luật về thế chấp và tài sản thế chấp, chúng ta thấy rằng:

- Theo Điều 325 BLDS 2015, khi thế chấp quyền sử dụng đất mà không thế chấp tài sản gắn liền với đất, tài sản được xử lý bao gồm cả tài sản gắn liền với đất, trừ trường hợp có thỏa thuận khác. Đây là trường hợp phù hợp với tình hình thế chấp của ông Đỗ Văn T và bà Hoàng Thị X.
  
- Theo Điều 307 BLDS 2015, số tiền có được từ việc xử lý tài sản cầm cố, thế chấp sau khi thanh toán chi phí bảo quản, thu giữ và xử lý tài sản cầm cố, thế chấp được thanh toán theo
```

## A.2#1 — abductive (defendant)

**Prompt**
```
Considering the following facts:
1. Người có quyền lợi và nghĩa vụ liên quan:
2. - Ông Đỗ Văn T, sinh năm 1960;
3. - Bà Hoàng Thị X, sinh năm 1959;
4. - Anh Đỗ Thanh P, sinh năm 1987;
5. - Chị Chu Thị T, sinh năm 1991;
6. - Cháu Đỗ Minh Đ, sinh năm 2011;
7. - Cháu Đỗ Minh H, sinh năm 2014;
8. Anh P và chị T là bố mẹ đẻ của cháu Đ và H nên anh chị là người đại diện hợp pháp của cháu Đ và cháu H.
9. Cùng địa chỉ: Thôn N, xã P, huyện T, thành phố H.
10. Nguyên đơn trình bày:
11. Ngân hàng QT(gọi tắt là VIB) và vợ chồng bà Đỗ Thị T và ông Chu Văn A có ký kết hợp đồng tín dụng số 020/HĐTD1-VIB038/11 ngày 26/08/2011, số tiền vay hạn mức là 2.200.000.000 đồng (Hai tỷ hai trăm triệu đồng); số tiền đã giải ngân là 2.200.000.000 đồng (Hai tỷ hai trăm triệu đồng) theo Khế ước nhận nợ số 020.01/KUNN1-VIB038/11 ngày 26/08/2011; thời hạn vay: 06 tháng kể từ ngày 26/08/2011; Lãi suất cho vay: 22.5%/năm, điều chỉnh 03 tháng/lần, bằng lãi suất điều chuyển vốn kinh doanh VND kỳ hạn …
12. Về lãi suất: Quá trình thực hiện Hợp đồng Ngân hàng có điều chỉnh lãi suất theo Quyết định điều chỉnh của Ngân hàng VIB. Kể từ ngày khoản vay của bà T, ông A chuyển sang nợ quá hạn là 06/02/2012 thì Ngân hàng áp dụng mức lãi suất là 32.25%/năm cho đến nay.
13. Để đảm bảo nghĩa vụ trả nợ cho khoản vay của bà T và ông A thì ông Đỗ Văn T và bà Hoàng Thị X đã thế chấp tài sản là bất động sản tọa lạc tại thửa đất số 342, tờ bản đồ số 00, diện tích 113.9m2 tại địa chỉ: Khu Đ, xã P, huyện T, thành phố H. Theo Giấy chứng nhận quyền sử dụng đất số AQ 083681, số vào sổ cấp Giấy chứng nhận quyền sử dụng đất: H.02876/QSDĐ/3570/QĐ-UB do UBND huyện T, thành phố H cấp cho ông Đỗ Văn T và bà Hoàng Thị X ngày 29/09/2009. Tài sản này được thế chấp theo Hợp đồng thế …
14. Trong quá trình thực hiện hợp đồng, bà Đỗ Thị T và ông Chu Văn A đã trả 192.458.930 đồng vào tiền lãi, kể từ ngày 06/02/2012 bà T, ông A không trả nợ lãi. Do bà T, ông A vi phạm nghĩa vụ hợp đồng tín dụng nên khoản vay này đã bị chuyển quá hạn từ ngày 06/02/2012.
15. Theo yêu cầu công tác xử lý nợ quá hạn, ngày 19/12/2014, Ngân hàng TMCP phần Quốc tế Việt Nam (VIB) đã bán khoản nợ vay của bà Đỗ Thị T, ông Chu Văn A cho Công ty QLTS (gọi tắt là VAMC). Đến ngày 30/7/2018 Ngân hàng VIB đã mua lại khoản nợ của bà T và ông A từ Công ty VAMC theo hợp đồng mua bán nợ số 2175/2018.BN.VAMC1-VIB.
16. Dư nợ tính đến ngày 06/8/2018, bà T và ông A còn nợ Ngân hàng VIB số tiền là 7.037.902.060đồng, trong đó:
17. Nợ gốc: 2.200.000.000đồng;
18. Nợ lãi trong hạn: 64.757.736đồng;
19. Lãi quá hạn: 4.773.144.324đồng.
20. Ngân hàng VIB yêu cầu bà Đỗ Thị T và ông Chu Văn A thanh toán tổng số tiền 7.037.902.060đ (Bảy tỷ không trăm ba mươi bảy triệu chín trăm linh hai nghìn không trăm sáu mươi đồng) cho Ngân hàng.
21. Bà Đỗ Thị T và ông Chu Văn A tiếp tục trả lãi cho Ngân hàng VIB các khoản lãi, lãi phạt quá hạn phát sinh theo quy định tại Hợp đồng tín dụng đã ký và theo quy định của pháp luật kể từ ngày 07/8/2018 cho đến ngày bà Đỗ Thị T và ông Chu Văn A thanh toán toàn bộ khoản vay.
22. Trường hợp bà Đỗ Thị T và ông Chu Văn A không trả hết nợ hoặc ông Đỗ Văn T và bà Hoàng Thị X không tự nguyện bàn giao tài sản bảo đảm thì Ngân hàng VIB có quyền yêu cầu Cơ quan thi hành án dân sự phát mại khối tài sản mà ông Đỗ Văn T và bà Hoàng Thị X đã thế chấp để thu hồi toàn bộ khoản nợ theo quy định của pháp luật là: Quyền sử dụng 113,9m2 đất cùng các tài sản gắn liền với đất, các quyền và lợi ích phát sinh đối với thửa đất số 342, tờ bản đồ số 00 tại địa chỉ: Khu Đ, xã P, huyện T, thành …
23. Trường hợp toàn bộ khối tài sản thế chấp sau khi xử lý phát mại mà không đủ để trả nợ cho Ngân hàng thì bà Đỗ Thị T và ông Chu Văn A tiếp tục thực hiện nghĩa vụ trả nợ cho Ngân hàng VIB cho đến khi tất toán khoản vay.
24. Án phí: Đề nghị Tòa án buộc bà Đỗ Thị T và ông Chu Văn A phải chịu toàn bộ án phí Kinh doanh thương mại theo quy định của pháp luật.
25. Bị đơn là bà Đỗ Thị T và ông Chu Văn A trình bày:
26. Ngày 26/08/2011, vợ chồng bà Đỗ Thị T và ông Chu Văn A và ngân hàng VIB có ký kết Hợp đồng tín dụng số 020/HĐTD1-VIB038/11 ngày 26/08/2011, số tiền vay hạn mức là 2.200.000.000 đồng (Hai tỷ hai trăm triệu đồng); số tiền đã giải ngân là 2.200.000.000 đồng (Hai tỷ hai trăm triệu đồng). Về nội dung của Hợp đồng như nguyên đơn trình bày là đúng.
27. Để đảm bảo nghĩa vụ trả nợ của vợ chồng bà Đỗ Thị T và ông Chu Văn A, bố mẹ của bà Đỗ Thị T là ông Đỗ Văn T và bà Hoàng Thị X đã thế chấp tài sản của mình là: Quyền sử dụng đất cùng các tài sản gắn liền với đất, các quyền và lợi ích phát sinh đối với 113.9m2 đất, thửa đất số 342, tờ bản đồ số 00 tại địa chỉ: Khu Đ, C, xã P, huyện T, thành phố H. Theo Giấy chứng nhận quyền sử dụng đất số AQ 083681, số vào sổ cấp Giấy chứng nhận quyền sử dụng đất: H.02876/QSDĐ/3570/QĐ-UB do UBND huyện T, thành …
28. Quá trình thực hiện hợp đồng, vợ chồng bà Đỗ Thị T và ông Chu Văn A đã trả được một phần nợ lãi. Do kinh tế suy thoái làm ăn kinh doanh thua lỗ nên không có tiền để tiếp tục trả lãi cho Ngân hàng như đã thỏa thuận.
29. Bà Đỗ Thị T và ông Chu Văn A xác nhận số nợ tính đến ngày 06/8/2018 là 7.037.902.060đồng, trong đó:
30. Nợ gốc: 2.200.000.000đồng;
31. Nợ lãi trong hạn: 64.757.736đồng;
32. Lãi quá hạn: 4.773.144.324đồng.
33. Quá trình thực hiện hợp đồng Ngân hàng đã điều chỉnh lãi suất theo đúng thỏa thuận tại Hợp đồng tín dụng đã ký nên về số tiền gốc và tiền lãi trong hạn, lãi quá hạn Ngân hàng yêu cầu bà Đỗ Thị T và ông Chu Văn A không có ý kiến gì.Hiện tại ngân hàng khởi kiện, bà Đỗ Thị T và ông Chu Văn A đồng ý trả số nợ gốc và xin miễn toàn bộ khoản nợ lãi.Nếu trong trường hợp bà Đỗ Thị T và ông Chu Văn A không trả được nợ thì bà Đỗ Thị T và ông Chu Văn A đồng ý trả lãi phát sinh theo yêu cầu của Ngân hàng và …
34. Người có quyền lợi và nghĩa vụ liên quan ông Đỗ Văn T và bà Hoàng Thị X trình bày trong bản tự khai như sau:
35. Ngày 26/11/2011 ông Đỗ Văn T và bà Hoàng Thị X có ký Hợp đồng thế chấp với Ngân hàng VIB với nội dung: ông Đỗ Văn T và bà Hoàng Thị X thế chấp toàn bộ quyền sử dụng 113,9m2 đất, thửa đất số 342, tờ bản đồ số 00, địa chỉ: Khu Đ, C, xã P, huyện T, thành phố H theo Giấy chứng nhận quyền sử dụng đất số: AQ 083681, số vào sổ cấp giấy chứng nhận quyền sử dụng đất H.02876/QSDĐ/3570/QĐ – UB do UBND huyện Thạch Thất cấp cho ông Chu Văn Tiến và bà Hoàng Thị X ngày 29/9/2009 để bảo lãnh cho khoản vay của …
36. Tại thời điểm thế chấp thì thửa đất không có tài sản trên đất.
37. Đến năm 2012 ông Đỗ Văn T và bà Hoàng Thị X cho vợ chồng con trai là Đỗ Thanh P, sinh năm 1987 và con dâu là Chu Thị T, sinh năm 1991 ra ở riêng, anh chị đã xây nhà 03 tầng trên thửa đất thế chấp.
38. Hiện nay toàn bộ nhà và đất là do gia đình anh Đỗ Thanh P quản lý sử dụng gồm: Đỗ Thanh P, Chu Thị T, cháu Đỗ Minh Đ và cháu Đỗ Minh H.
39. Ngân hàng khởi kiện yêu cầu chị Tân, anh Anh trả nợ nhưng do các con hiện nay kinh tế khó khăn, không có khả năng trả nợ nên ông Đỗ Văn T và bà Hoàng Thị X đồng ý để Ngân hàng kê biên phát mại tài sản thế chấp để trả nợ cho Ngân hàng.
40. Trong trường hợp Ngân hàng phát mại tài sản thế chấp thì ông Đỗ Văn T và bà Hoàng Thị X đề nghị Ngân hàng thanh toán trả con trai giá trị ngôi nhà và các công trình xây trên đất.
41. Người có quyền lợi và nghĩa vụ liên quan anh Đỗ Thanh P và chị Chu Thị T trình bày trong bản tự khai như sau:
42. Ngày 30/5/2011 bố mẹ của anh Đỗ Thanh P và chị Chu Thị T là Đỗ Văn T và Hoàng Thị X có thế chấp cho Ngân hàng VIB thửa đất số 342, tờ bản đồ số 00, diện tích 113,9m2, địa chỉ: Khu Đ, C, xã P, huyện T, thành phố H theo Giấy chứng nhận quyền sử dụng đất số: AQ 083681, số vào sổ cấp giấy chứng nhận quyền sử dụng đất H.02876/QSDĐ/3570/QĐ – UB do UBND huyện Thạch Thất cấp cho ông Chu Văn Tiến và bà Hoàng Thị X ngày 29/9/2009 để bảo lãnh cho khoản vay chị là Đỗ Thị T và anh Chu Văn A tại Ngân hàng …
43. Tại thời điểm thế chấp thì thửa đất không có tài sản trên đất.
44. Năm 2012 anh Đỗ Thanh P và chị Chu Thị T được bố mẹ cho ra ở riêng trên thửa đất đó. Vợ chồng anh Đỗ Thanh P và chị Chu Thị T đã xây nhà 02 tầng 01 tum.
45. Hiện nay toàn bộ tài sản thế chấp là do gia đình anh Đỗ Thanh P quản lý.
46. Ngân hàng khởi kiện yêu cầu sử lý tài sản thế chấp để trả nợ cho anh Anh và chị Tân, anh Đỗ Thanh P và chị Chu Thị T cũng đồng ý.
47. Đối với tài sản trên đất là ngôi nhà hai tầng một tum do vợ chồng anh Đỗ Thanh P và chị Chu Thị T xây dựng, anh Đỗ Thanh P và chị Chu Thị T cũng đồng ý để Ngân hàng phát mại.
48. Trong trường hợp bán tài sản thế chấp thì anh Đỗ Thanh P và chị Chu Thị T sẽ tự thỏa thuận với Ngân hàng về giá trị tài sản trên đất.
49. Về tài liệu Tòa thu thập:
50. Theo biên bản thẩm định tại chỗ ngày 27/6/2018, tài sản thế chấp thuộc quyền sở hữu của ông Đỗ Văn T và bà Hoàng Thị X trên đất gồm: 01 nhà hai tầng và 01 tum lợp mái tôn xây dựng năm 2011 bê tông cốt thép kiên cố diện tích 50m2/tầng, nhà chưa sơn; 01 lán lợp tôn, tường gạch diện tích 50m2 xây dựng năm 2011. Hiện tại sinh sống trên đất gồm: Anh Đỗ Thanh P, chị Chu Thị T, cháu Đỗ Minh Đ và cháu Đỗ Minh H.
51. Theo bảng tính lãi ngày 06/8/2018 do Ngân hàng cung cấp thì từ ngày 26/8/2011 đến ngày 06/2/2012, Ngân hàng có điều chỉnh lãi suất và số tiền lãi trong hạn là 64.757.736đ theo đúng thỏa thuận tại Hợp đồng tín dụng.
52. Kể từ ngày 06/02/2012 bà T và ông A không trả gốc và lãi, Ngân hàng đã chuyển sang nợ lãi quá hạn thì Ngân hàng không điều chỉnh lãi suất và áp dụng mức lãi suất quá hạn là 32,25%/năm với số tiền 4.773.144.324 đồng (trong đó lãi trên dư nợ gốc là: 4.635.400.000, lãi trên dư nợ lãi chậm trả là 137.744.324 đồng).
Considering the following rules: Applicable provisions of Vietnamese law:
1. [BLDS 2015] Điều 307. Thanh toán số tiền có được từ việc xử lý tài sản cầm cố, thế chấp. 1. Số tiền có được từ việc xử lý tài sản cầm cố, thế chấp sau khi thanh toán chi phí bảo quản, thu giữ và xử lý tài sản cầm cố, thế chấp được thanh toán theo thứ tự ưu tiên quy định tại Điều 308 của Bộ luật này. 2. Trường hợp số tiền có được từ việc xử lý tài sản cầm cố, thế chấp sau khi thanh toán chi phí bảo quản, thu giữ và xử lý tài sản cầm cố, thế chấp lớn hơn giá trị nghĩa vụ được bảo đảm thì số tiền chênh lệch phải được trả cho bên bảo đảm. 3. Trường hợp số tiền có được từ việc xử lý tài sản cầm cố, thế chấp sau khi thanh toán chi phí bảo quản, thu giữ và xử lý tài sản cầm cố, thế chấp nhỏ hơn giá trị nghĩa vụ được bảo
2. [BLDS 2015] Điều 325. Thế chấp quyền sử dụng đất mà không thế chấp tài sản gắn liền với đất. 1. Trường hợp thế chấp quyền sử dụng đất mà không thế chấp tài sản gắn liền với đất và người sử dụng đất đồng thời là chủ sở hữu tài sản gắn liền với đất thì tài sản được xử lý bao gồm cả tài sản gắn liền với đất, trừ trường hợp có thỏa thuận khác. 2. Trường hợp thế chấp quyền sử dụng đất mà người sử dụng đất không đồng thời là chủ sở hữu tài sản gắn liền với đất thì khi xử lý quyền sử dụng đất, chủ sở hữu tài sản gắn liền với đất được tiếp tục sử dụng đất trong phạm vi quyền, nghĩa vụ của mình; quyền và nghĩa vụ của bên thế chấp trong mối quan hệ với chủ sở hữu tài sản gắn liền với đất được chuyển giao cho người nhận chu
3. [BLDS 2015] Điều 326. Thế chấp tài sản gắn liền với đất mà không thế chấp quyền sử dụng đất. 1. Trường hợp chỉ thế chấp tài sản gắn liền với đất mà không thế chấp quyền sử dụng đất và chủ sở hữu tài sản gắn liền với đất đồng thời là người sử dụng đất thì tài sản được xử lý bao gồm cả quyền sử dụng đất, trừ trường hợp có thỏa thuận khác. 2. Trường hợp chỉ thế chấp tài sản gắn liền với đất mà không thế chấp quyền sử dụng đất và chủ sở hữu tài sản gắn liền với đất không đồng thời là người sử dụng đất thì khi xử lý tài sản gắn liền với đất, người nhận chuyển quyền sở hữu tài sản gắn liền với đất được tiếp tục sử dụng đất trong phạm vi quyền, nghĩa vụ của chủ sở hữu tài sản gắn liền với đất được chuyển giao, trừ trườn
4. [BLDS 2015] Điều 320. Nghĩa vụ của bên thế chấp. 1. Giao giấy tờ liên quan đến tài sản thế chấp trong trường hợp các bên có thỏa thuận, trừ trường hợp luật có quy định khác. 2. Bảo quản, giữ gìn tài sản thế chấp. 3. Áp dụng các biện pháp cần thiết để khắc phục, kể cả phải ngừng việc khai thác công dụng tài sản thế chấp nếu do việc khai thác đó mà tài sản thế chấp có nguy cơ mất giá trị hoặc giảm sút giá trị. 4. Khi tài sản thế chấp bị hư hỏng thì trong một thời gian hợp lý bên thế chấp phải sửa chữa hoặc thay thế bằng tài sản khác có giá trị tương đương, trừ trường hợp có thoả thuận khác. 5. Cung cấp thông tin về thực trạng tài sản thế chấp cho bên nhận thế chấp. 6. Giao tài sản thế chấp cho bên nhận thế chấp để 
5. [BLDS 2015] Điều 318. Tài sản thế chấp. 1. Trường hợp thế chấp toàn bộ bất động sản, động sản có vật phụ thì vật phụ của bất động sản, động sản đó cũng thuộc tài sản thế chấp, trừ trường hợp có thỏa thuận khác. 2. Trường hợp thế chấp một phần bất động sản, động sản có vật phụ thì vật phụ gắn với tài sản đó thuộc tài sản thế chấp, trừ trường hợp có thoả thuận khác. 3. Trường hợp thế chấp quyền sử dụng đất mà tài sản gắn liền với đất thuộc quyền sở hữu của bên thế chấp thì tài sản gắn liền với đất cũng thuộc tài sản thế chấp, trừ trường hợp có thỏa thuận khác. 4. Trường hợp tài sản thế chấp được bảo hiểm thì bên nhận thế chấp phải thông báo cho tổ chức bảo hiểm biết về việc tài sản bảo hiểm đang được dùng để thế ch
Please suggest hypotheses to support why the outcome of the case might be the court rejects all of the plaintiff's claims.
```
**Response**
```
Để xác định liệu yêu cầu của nguyên đơn có được chấp nhận hay không, chúng ta cần phân tích từng yếu tố trong hồ sơ:

1. **Thành phần của tài sản thế chấp**: Theo tài liệu, tài sản thế chấp là quyền sử dụng đất cùng các tài sản gắn liền với đất, cụ thể là ngôi nhà 2 tầng 1 tum. 

2. **Quyền sở hữu của các bên liên quan**: Ông Đỗ Văn T và bà Hoàng Thị X là người thế chấp tài sản, nhưng họ không phải là chủ sở hữu của tài sản gắn liền với đất (nhà và lán lợp tôn). 

3. **Điều khoản thế chấp**: Theo Điều 325 BLDS 2015, khi thế chấp quyền sử dụng đất mà không thế chấp tài sản gắn liền với đất, tài sản được xử lý bao gồm cả tài sản gắn liền với đất, trừ trường hợp có thỏa thuận khác. 

4. **Thỏa thuận khác**: Trong hồ sơ không có thông tin về bất kỳ thỏa thuận nào giữa bên thế chấp và bên nhận thế chấp về việc xử lý tài sản gắn liền với đất.

Từ những phân tích trên, có thể đưa ra giả thuyết rằng:

**Giả thuyết 1:** 
Ông Đỗ Văn T và bà Hoàng Thị X đã thỏa thuận với Ngân hàng VIB rằng tài sản gắn liền với đất (nhà và lán lợp tôn) sẽ không được xử lý khi tài sản thế chấp (quyền sử dụng đất) bị phát mại. Nếu giả thuyết này đúng, thì tài sản gắn liền với đất (nhà và lán lợp tôn) sẽ không thuộc tài sản thế chấp và không nằm trong phạm vi xử lý khi phát mại tài sản thế chấp.

**Giả thuyết 2:** 
Nếu không có thỏa thuận khác, tài sản gắn liền với đất (nhà và lán lợp tôn) sẽ thuộc tài sản thế chấp và có thể bị phát mại. Tuy nhiên, theo Điều 307 BLDS 2015, số tiền có được từ việc xử lý tài sản thế chấp sẽ được thanh toán theo thứ tự ưu tiên, và nếu số tiền thu được nhỏ hơn giá trị nghĩa vụ được bảo đảm, số tiền chênh lệch phải được trả cho bên bảo đảm (Ngân hàng VIB).

Theo giả thuyết 1, yêu cầu của nguyên đơn (Ngân hàng VIB) về việc thu hồi toàn bộ tài sản thế chấp để trả nợ cho Ngân hàng sẽ không được chấp nhận vì tài sản gắn liền với đất (nhà và lán lợp tôn) không thuộc tài sản thế chấp.

Theo giả thuyết 2, yêu cầu của nguyên đơn vẫn có thể được chấp nhận, nhưng số tiền thu được từ việc phát mại tài sản thế chấp sẽ không đủ
```

## judge#1 — judge

**Prompt**
```

```
**Response**
```
llm judge
```

## A.3#1 — rule_based (defendant)

**Prompt**
```
Considering the following facts:
1. Người có quyền lợi và nghĩa vụ liên quan:
2. - Ông Đỗ Văn T, sinh năm 1960;
3. - Bà Hoàng Thị X, sinh năm 1959;
4. - Anh Đỗ Thanh P, sinh năm 1987;
5. - Chị Chu Thị T, sinh năm 1991;
6. - Cháu Đỗ Minh Đ, sinh năm 2011;
7. - Cháu Đỗ Minh H, sinh năm 2014;
8. Anh P và chị T là bố mẹ đẻ của cháu Đ và H nên anh chị là người đại diện hợp pháp của cháu Đ và cháu H.
9. Cùng địa chỉ: Thôn N, xã P, huyện T, thành phố H.
10. Nguyên đơn trình bày:
11. Ngân hàng QT(gọi tắt là VIB) và vợ chồng bà Đỗ Thị T và ông Chu Văn A có ký kết hợp đồng tín dụng số 020/HĐTD1-VIB038/11 ngày 26/08/2011, số tiền vay hạn mức là 2.200.000.000 đồng (Hai tỷ hai trăm triệu đồng); số tiền đã giải ngân là 2.200.000.000 đồng (Hai tỷ hai trăm triệu đồng) theo Khế ước nhận nợ số 020.01/KUNN1-VIB038/11 ngày 26/08/2011; thời hạn vay: 06 tháng kể từ ngày 26/08/2011; Lãi suất cho vay: 22.5%/năm, điều chỉnh 03 tháng/lần, bằng lãi suất điều chuyển vốn kinh doanh VND kỳ hạn …
12. Về lãi suất: Quá trình thực hiện Hợp đồng Ngân hàng có điều chỉnh lãi suất theo Quyết định điều chỉnh của Ngân hàng VIB. Kể từ ngày khoản vay của bà T, ông A chuyển sang nợ quá hạn là 06/02/2012 thì Ngân hàng áp dụng mức lãi suất là 32.25%/năm cho đến nay.
13. Để đảm bảo nghĩa vụ trả nợ cho khoản vay của bà T và ông A thì ông Đỗ Văn T và bà Hoàng Thị X đã thế chấp tài sản là bất động sản tọa lạc tại thửa đất số 342, tờ bản đồ số 00, diện tích 113.9m2 tại địa chỉ: Khu Đ, xã P, huyện T, thành phố H. Theo Giấy chứng nhận quyền sử dụng đất số AQ 083681, số vào sổ cấp Giấy chứng nhận quyền sử dụng đất: H.02876/QSDĐ/3570/QĐ-UB do UBND huyện T, thành phố H cấp cho ông Đỗ Văn T và bà Hoàng Thị X ngày 29/09/2009. Tài sản này được thế chấp theo Hợp đồng thế …
14. Trong quá trình thực hiện hợp đồng, bà Đỗ Thị T và ông Chu Văn A đã trả 192.458.930 đồng vào tiền lãi, kể từ ngày 06/02/2012 bà T, ông A không trả nợ lãi. Do bà T, ông A vi phạm nghĩa vụ hợp đồng tín dụng nên khoản vay này đã bị chuyển quá hạn từ ngày 06/02/2012.
15. Theo yêu cầu công tác xử lý nợ quá hạn, ngày 19/12/2014, Ngân hàng TMCP phần Quốc tế Việt Nam (VIB) đã bán khoản nợ vay của bà Đỗ Thị T, ông Chu Văn A cho Công ty QLTS (gọi tắt là VAMC). Đến ngày 30/7/2018 Ngân hàng VIB đã mua lại khoản nợ của bà T và ông A từ Công ty VAMC theo hợp đồng mua bán nợ số 2175/2018.BN.VAMC1-VIB.
16. Dư nợ tính đến ngày 06/8/2018, bà T và ông A còn nợ Ngân hàng VIB số tiền là 7.037.902.060đồng, trong đó:
17. Nợ gốc: 2.200.000.000đồng;
18. Nợ lãi trong hạn: 64.757.736đồng;
19. Lãi quá hạn: 4.773.144.324đồng.
20. Ngân hàng VIB yêu cầu bà Đỗ Thị T và ông Chu Văn A thanh toán tổng số tiền 7.037.902.060đ (Bảy tỷ không trăm ba mươi bảy triệu chín trăm linh hai nghìn không trăm sáu mươi đồng) cho Ngân hàng.
21. Bà Đỗ Thị T và ông Chu Văn A tiếp tục trả lãi cho Ngân hàng VIB các khoản lãi, lãi phạt quá hạn phát sinh theo quy định tại Hợp đồng tín dụng đã ký và theo quy định của pháp luật kể từ ngày 07/8/2018 cho đến ngày bà Đỗ Thị T và ông Chu Văn A thanh toán toàn bộ khoản vay.
22. Trường hợp bà Đỗ Thị T và ông Chu Văn A không trả hết nợ hoặc ông Đỗ Văn T và bà Hoàng Thị X không tự nguyện bàn giao tài sản bảo đảm thì Ngân hàng VIB có quyền yêu cầu Cơ quan thi hành án dân sự phát mại khối tài sản mà ông Đỗ Văn T và bà Hoàng Thị X đã thế chấp để thu hồi toàn bộ khoản nợ theo quy định của pháp luật là: Quyền sử dụng 113,9m2 đất cùng các tài sản gắn liền với đất, các quyền và lợi ích phát sinh đối với thửa đất số 342, tờ bản đồ số 00 tại địa chỉ: Khu Đ, xã P, huyện T, thành …
23. Trường hợp toàn bộ khối tài sản thế chấp sau khi xử lý phát mại mà không đủ để trả nợ cho Ngân hàng thì bà Đỗ Thị T và ông Chu Văn A tiếp tục thực hiện nghĩa vụ trả nợ cho Ngân hàng VIB cho đến khi tất toán khoản vay.
24. Án phí: Đề nghị Tòa án buộc bà Đỗ Thị T và ông Chu Văn A phải chịu toàn bộ án phí Kinh doanh thương mại theo quy định của pháp luật.
25. Bị đơn là bà Đỗ Thị T và ông Chu Văn A trình bày:
26. Ngày 26/08/2011, vợ chồng bà Đỗ Thị T và ông Chu Văn A và ngân hàng VIB có ký kết Hợp đồng tín dụng số 020/HĐTD1-VIB038/11 ngày 26/08/2011, số tiền vay hạn mức là 2.200.000.000 đồng (Hai tỷ hai trăm triệu đồng); số tiền đã giải ngân là 2.200.000.000 đồng (Hai tỷ hai trăm triệu đồng). Về nội dung của Hợp đồng như nguyên đơn trình bày là đúng.
27. Để đảm bảo nghĩa vụ trả nợ của vợ chồng bà Đỗ Thị T và ông Chu Văn A, bố mẹ của bà Đỗ Thị T là ông Đỗ Văn T và bà Hoàng Thị X đã thế chấp tài sản của mình là: Quyền sử dụng đất cùng các tài sản gắn liền với đất, các quyền và lợi ích phát sinh đối với 113.9m2 đất, thửa đất số 342, tờ bản đồ số 00 tại địa chỉ: Khu Đ, C, xã P, huyện T, thành phố H. Theo Giấy chứng nhận quyền sử dụng đất số AQ 083681, số vào sổ cấp Giấy chứng nhận quyền sử dụng đất: H.02876/QSDĐ/3570/QĐ-UB do UBND huyện T, thành …
28. Quá trình thực hiện hợp đồng, vợ chồng bà Đỗ Thị T và ông Chu Văn A đã trả được một phần nợ lãi. Do kinh tế suy thoái làm ăn kinh doanh thua lỗ nên không có tiền để tiếp tục trả lãi cho Ngân hàng như đã thỏa thuận.
29. Bà Đỗ Thị T và ông Chu Văn A xác nhận số nợ tính đến ngày 06/8/2018 là 7.037.902.060đồng, trong đó:
30. Nợ gốc: 2.200.000.000đồng;
31. Nợ lãi trong hạn: 64.757.736đồng;
32. Lãi quá hạn: 4.773.144.324đồng.
33. Quá trình thực hiện hợp đồng Ngân hàng đã điều chỉnh lãi suất theo đúng thỏa thuận tại Hợp đồng tín dụng đã ký nên về số tiền gốc và tiền lãi trong hạn, lãi quá hạn Ngân hàng yêu cầu bà Đỗ Thị T và ông Chu Văn A không có ý kiến gì.Hiện tại ngân hàng khởi kiện, bà Đỗ Thị T và ông Chu Văn A đồng ý trả số nợ gốc và xin miễn toàn bộ khoản nợ lãi.Nếu trong trường hợp bà Đỗ Thị T và ông Chu Văn A không trả được nợ thì bà Đỗ Thị T và ông Chu Văn A đồng ý trả lãi phát sinh theo yêu cầu của Ngân hàng và …
34. Người có quyền lợi và nghĩa vụ liên quan ông Đỗ Văn T và bà Hoàng Thị X trình bày trong bản tự khai như sau:
35. Ngày 26/11/2011 ông Đỗ Văn T và bà Hoàng Thị X có ký Hợp đồng thế chấp với Ngân hàng VIB với nội dung: ông Đỗ Văn T và bà Hoàng Thị X thế chấp toàn bộ quyền sử dụng 113,9m2 đất, thửa đất số 342, tờ bản đồ số 00, địa chỉ: Khu Đ, C, xã P, huyện T, thành phố H theo Giấy chứng nhận quyền sử dụng đất số: AQ 083681, số vào sổ cấp giấy chứng nhận quyền sử dụng đất H.02876/QSDĐ/3570/QĐ – UB do UBND huyện Thạch Thất cấp cho ông Chu Văn Tiến và bà Hoàng Thị X ngày 29/9/2009 để bảo lãnh cho khoản vay của …
36. Tại thời điểm thế chấp thì thửa đất không có tài sản trên đất.
37. Đến năm 2012 ông Đỗ Văn T và bà Hoàng Thị X cho vợ chồng con trai là Đỗ Thanh P, sinh năm 1987 và con dâu là Chu Thị T, sinh năm 1991 ra ở riêng, anh chị đã xây nhà 03 tầng trên thửa đất thế chấp.
38. Hiện nay toàn bộ nhà và đất là do gia đình anh Đỗ Thanh P quản lý sử dụng gồm: Đỗ Thanh P, Chu Thị T, cháu Đỗ Minh Đ và cháu Đỗ Minh H.
39. Ngân hàng khởi kiện yêu cầu chị Tân, anh Anh trả nợ nhưng do các con hiện nay kinh tế khó khăn, không có khả năng trả nợ nên ông Đỗ Văn T và bà Hoàng Thị X đồng ý để Ngân hàng kê biên phát mại tài sản thế chấp để trả nợ cho Ngân hàng.
40. Trong trường hợp Ngân hàng phát mại tài sản thế chấp thì ông Đỗ Văn T và bà Hoàng Thị X đề nghị Ngân hàng thanh toán trả con trai giá trị ngôi nhà và các công trình xây trên đất.
41. Người có quyền lợi và nghĩa vụ liên quan anh Đỗ Thanh P và chị Chu Thị T trình bày trong bản tự khai như sau:
42. Ngày 30/5/2011 bố mẹ của anh Đỗ Thanh P và chị Chu Thị T là Đỗ Văn T và Hoàng Thị X có thế chấp cho Ngân hàng VIB thửa đất số 342, tờ bản đồ số 00, diện tích 113,9m2, địa chỉ: Khu Đ, C, xã P, huyện T, thành phố H theo Giấy chứng nhận quyền sử dụng đất số: AQ 083681, số vào sổ cấp giấy chứng nhận quyền sử dụng đất H.02876/QSDĐ/3570/QĐ – UB do UBND huyện Thạch Thất cấp cho ông Chu Văn Tiến và bà Hoàng Thị X ngày 29/9/2009 để bảo lãnh cho khoản vay chị là Đỗ Thị T và anh Chu Văn A tại Ngân hàng …
43. Tại thời điểm thế chấp thì thửa đất không có tài sản trên đất.
44. Năm 2012 anh Đỗ Thanh P và chị Chu Thị T được bố mẹ cho ra ở riêng trên thửa đất đó. Vợ chồng anh Đỗ Thanh P và chị Chu Thị T đã xây nhà 02 tầng 01 tum.
45. Hiện nay toàn bộ tài sản thế chấp là do gia đình anh Đỗ Thanh P quản lý.
46. Ngân hàng khởi kiện yêu cầu sử lý tài sản thế chấp để trả nợ cho anh Anh và chị Tân, anh Đỗ Thanh P và chị Chu Thị T cũng đồng ý.
47. Đối với tài sản trên đất là ngôi nhà hai tầng một tum do vợ chồng anh Đỗ Thanh P và chị Chu Thị T xây dựng, anh Đỗ Thanh P và chị Chu Thị T cũng đồng ý để Ngân hàng phát mại.
48. Trong trường hợp bán tài sản thế chấp thì anh Đỗ Thanh P và chị Chu Thị T sẽ tự thỏa thuận với Ngân hàng về giá trị tài sản trên đất.
49. Về tài liệu Tòa thu thập:
50. Theo biên bản thẩm định tại chỗ ngày 27/6/2018, tài sản thế chấp thuộc quyền sở hữu của ông Đỗ Văn T và bà Hoàng Thị X trên đất gồm: 01 nhà hai tầng và 01 tum lợp mái tôn xây dựng năm 2011 bê tông cốt thép kiên cố diện tích 50m2/tầng, nhà chưa sơn; 01 lán lợp tôn, tường gạch diện tích 50m2 xây dựng năm 2011. Hiện tại sinh sống trên đất gồm: Anh Đỗ Thanh P, chị Chu Thị T, cháu Đỗ Minh Đ và cháu Đỗ Minh H.
51. Theo bảng tính lãi ngày 06/8/2018 do Ngân hàng cung cấp thì từ ngày 26/8/2011 đến ngày 06/2/2012, Ngân hàng có điều chỉnh lãi suất và số tiền lãi trong hạn là 64.757.736đ theo đúng thỏa thuận tại Hợp đồng tín dụng.
52. Kể từ ngày 06/02/2012 bà T và ông A không trả gốc và lãi, Ngân hàng đã chuyển sang nợ lãi quá hạn thì Ngân hàng không điều chỉnh lãi suất và áp dụng mức lãi suất quá hạn là 32,25%/năm với số tiền 4.773.144.324 đồng (trong đó lãi trên dư nợ gốc là: 4.635.400.000, lãi trên dư nợ lãi chậm trả là 137.744.324 đồng).
Considering the following rules: Applicable provisions of Vietnamese law:
1. [BLDS 2015] Điều 307. Thanh toán số tiền có được từ việc xử lý tài sản cầm cố, thế chấp. 1. Số tiền có được từ việc xử lý tài sản cầm cố, thế chấp sau khi thanh toán chi phí bảo quản, thu giữ và xử lý tài sản cầm cố, thế chấp được thanh toán theo thứ tự ưu tiên quy định tại Điều 308 của Bộ luật này. 2. Trường hợp số tiền có được từ việc xử lý tài sản cầm cố, thế chấp sau khi thanh toán chi phí bảo quản, thu giữ và xử lý tài sản cầm cố, thế chấp lớn hơn giá trị nghĩa vụ được bảo đảm thì số tiền chênh lệch phải được trả cho bên bảo đảm. 3. Trường hợp số tiền có được từ việc xử lý tài sản cầm cố, thế chấp sau khi thanh toán chi phí bảo quản, thu giữ và xử lý tài sản cầm cố, thế chấp nhỏ hơn giá trị nghĩa vụ được bảo
2. [BLDS 2015] Điều 325. Thế chấp quyền sử dụng đất mà không thế chấp tài sản gắn liền với đất. 1. Trường hợp thế chấp quyền sử dụng đất mà không thế chấp tài sản gắn liền với đất và người sử dụng đất đồng thời là chủ sở hữu tài sản gắn liền với đất thì tài sản được xử lý bao gồm cả tài sản gắn liền với đất, trừ trường hợp có thỏa thuận khác. 2. Trường hợp thế chấp quyền sử dụng đất mà người sử dụng đất không đồng thời là chủ sở hữu tài sản gắn liền với đất thì khi xử lý quyền sử dụng đất, chủ sở hữu tài sản gắn liền với đất được tiếp tục sử dụng đất trong phạm vi quyền, nghĩa vụ của mình; quyền và nghĩa vụ của bên thế chấp trong mối quan hệ với chủ sở hữu tài sản gắn liền với đất được chuyển giao cho người nhận chu
3. [BLDS 2015] Điều 326. Thế chấp tài sản gắn liền với đất mà không thế chấp quyền sử dụng đất. 1. Trường hợp chỉ thế chấp tài sản gắn liền với đất mà không thế chấp quyền sử dụng đất và chủ sở hữu tài sản gắn liền với đất đồng thời là người sử dụng đất thì tài sản được xử lý bao gồm cả quyền sử dụng đất, trừ trường hợp có thỏa thuận khác. 2. Trường hợp chỉ thế chấp tài sản gắn liền với đất mà không thế chấp quyền sử dụng đất và chủ sở hữu tài sản gắn liền với đất không đồng thời là người sử dụng đất thì khi xử lý tài sản gắn liền với đất, người nhận chuyển quyền sở hữu tài sản gắn liền với đất được tiếp tục sử dụng đất trong phạm vi quyền, nghĩa vụ của chủ sở hữu tài sản gắn liền với đất được chuyển giao, trừ trườn
4. [BLDS 2015] Điều 320. Nghĩa vụ của bên thế chấp. 1. Giao giấy tờ liên quan đến tài sản thế chấp trong trường hợp các bên có thỏa thuận, trừ trường hợp luật có quy định khác. 2. Bảo quản, giữ gìn tài sản thế chấp. 3. Áp dụng các biện pháp cần thiết để khắc phục, kể cả phải ngừng việc khai thác công dụng tài sản thế chấp nếu do việc khai thác đó mà tài sản thế chấp có nguy cơ mất giá trị hoặc giảm sút giá trị. 4. Khi tài sản thế chấp bị hư hỏng thì trong một thời gian hợp lý bên thế chấp phải sửa chữa hoặc thay thế bằng tài sản khác có giá trị tương đương, trừ trường hợp có thoả thuận khác. 5. Cung cấp thông tin về thực trạng tài sản thế chấp cho bên nhận thế chấp. 6. Giao tài sản thế chấp cho bên nhận thế chấp để 
5. [BLDS 2015] Điều 318. Tài sản thế chấp. 1. Trường hợp thế chấp toàn bộ bất động sản, động sản có vật phụ thì vật phụ của bất động sản, động sản đó cũng thuộc tài sản thế chấp, trừ trường hợp có thỏa thuận khác. 2. Trường hợp thế chấp một phần bất động sản, động sản có vật phụ thì vật phụ gắn với tài sản đó thuộc tài sản thế chấp, trừ trường hợp có thoả thuận khác. 3. Trường hợp thế chấp quyền sử dụng đất mà tài sản gắn liền với đất thuộc quyền sở hữu của bên thế chấp thì tài sản gắn liền với đất cũng thuộc tài sản thế chấp, trừ trường hợp có thỏa thuận khác. 4. Trường hợp tài sản thế chấp được bảo hiểm thì bên nhận thế chấp phải thông báo cho tổ chức bảo hiểm biết về việc tài sản bảo hiểm đang được dùng để thế ch
Assuming these hypotheses are true in this case:
Điều khoản thế chấp: Theo Điều 325 BLDS 2015, khi thế chấp quyền sử dụng đất mà không thế chấp tài sản gắn liền với đất, tài sản được xử lý bao gồm cả tài sản gắn liền với đất, trừ trường hợp có thỏa thuận khác.
According to the given rules and hypotheses, please evaluate whether the court accepts the plaintiff's claims in whole or in part.
```
**Response**
```
The plaintiff's claim includes the demand for repayment of the debt amounting to 7.037.902.060 đồng (Bảy tỷ không trăm ba mươi bảy triệu chín trăm linh hai nghìn không trăm sáu mươi đồng) from the defendants, as well as the request for the court to order the defendants to pay all litigation costs.

Given the context provided, we need to analyze if the court would accept the plaintiff's claims based on the applicable legal provisions:

1. **Claim for Repayment of Debt**: The plaintiff demands that the defendants repay the total debt amount. According to the given facts, the defendants have acknowledged their debt and agreed to pay the full amount. Therefore, the court is likely to accept this part of the claim.

2. **Litigation Costs**: The plaintiff also requests the court to order the defendants to pay all litigation costs. This is a common practice where the losing party is required to cover the legal fees incurred by the winning party. Since the defendants have acknowledged their debt and agreed to pay it, they should be responsible for covering the litigation costs.

Based on the above analysis, the court is likely to accept both parts of the plaintiff's claims.

Yêu cầu của nguyên đơn được chấp nhận (toàn bộ/một phần): Yêu cầu của nguyên đơn được chấp nhận (toàn bộ)
```

## Result
- outcome: **the court accepts the plaintiff's claims in whole or in part**
- converged: True
- accepted hypotheses:
  - Điều khoản thế chấp: Theo Điều 325 BLDS 2015, khi thế chấp quyền sử dụng đất mà không thế chấp tài sản gắn liền với đất, tài sản được xử lý bao gồm cả tài sản gắn liền với đất, trừ trường hợp có thỏa thuận khác.