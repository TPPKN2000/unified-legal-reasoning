# Civil law simulation

## A.1 — rule_based

**Prompt**
```
Considering the following facts:
1. Theo đơn khởi kiện,các tài liệu có trong hồ sơ vụ án và lời khai của nguyên đơn tại phiên tòa thể hiện:
2. Ngày 06-12-2011, Ngân hàng B (sau gọi tắt Ngân hàng) và Công ty TNHH Thương mại và Xuất nhập khẩu H (sau gọi tắt Công ty H) ký kết Thư Cấp Tín
3. dụng số BOCOMHCM-FL/008/2011, theo đó Ngân hàng đồng ý cấp cho Công ty H một khoản tín dụng tuần hoàn ngắn hạn với hạn mức tín dụng là 2.000.000 USD
4. (Đô la Mỹ), tương đương 46.000.000.000 Việt Nam đồng (tỷ giá 01USD = 23.000VNĐ) để Công ty H sử dụng làm vốn lưu động. Trong khoảng thời gian từ 26-11-2012 cho đến ngày 05-12-2012, Ngân hàng đã thực hiện giải ngân cho Công ty H 04 lần với tổng số tiền vay là 1.968.192 USD, tương đương 45.268.416.000 đồng (Việt Nam đồng).
5. Ngày 06-12-2011, Công ty TNHH Đầu tư K (sau gọi tắt Công ty K) và cá nhân ông Lam Wing C (Lâm Vinh T) là người đại diện theo pháp luật của Công ty
6. K đã ký các hợp đồng bảo lãnh với Ngân hàng để bảo lãnh cho việc thanh toán đúng hạn toàn bộ số tiền mà Công ty H nợ Ngân hàng theo Thư cấp tín Dụng khi
7. số tiền đó đến hạn và phải trả cho Ngân hàng. Cùng ngày 06-12-2011, Công ty K và Ngân hàng B chi nhánh thành phố Hồ Chí Minh (sau viết tắt Ngân hàng B-CN TP. HCM)  đã ký kết Hợp đồng thế chấp số BOCOMHCM-MA-LUR/004/2011. Theo đó, Công ty K đồng ý sử dụng các tài sản thuộc sở hữu của mình làm tài sản thế chấp để bảo đảm cho việc hoàn trả mọi khoản tiền, nợ và nghĩa vụ hiện tại và tương lai đến hạn, còn nợ hoặc phải gánh chịu của Công ty H đối với Ngân hàng B-CN TP. HCM theo quy định của Thư cấp …
8. - Quyền sử dụng đất của Công ty K đối với lô đất có tổng diện tích 5000m2 tại Khu đô thị C, đường L, phường B, quận K, Thành Phố Hải Phòng;
9. - Tài sản hình thành trong tương lai gắn liền với đất: là 07 tòa nhà chung cư, bao gồm các tòa nhà A2, A4, A5, A6, A7, A8, A9 tại Khu đô thị C, đường L, phường B, quận K, thành phố Hải Phòng có tổng diện tích sàn là 21.563,92m2.
10. Ngày 23-05-2013, Ngân hàng B-CN TP. HCM và Công ty H ký kết sửa đổi Thư cấp tín dụng số BOCOMHCM-FL/008/2011-A1 để sửa đổi, bổ sung một số điều khoản của Thư cấp tín dụng. Theo đó, các bên đã thống nhất như sau:
11. - Gia hạn thời hạn hiệu lực của Thư cấp tín dụng;
12. - Khoản nợ gốc sẽ được cơ cấu lại phụ thuộc vào các điều kiện sau:
13. + Công ty H cam kết thanh toán đầy đủ số tiền gốc là 108.000 USD và lãi cộng dồn trước ngày 03-06-2013;
14. + Tổng dư nợ vay còn lại là 1.860.000 USD và sẽ được cơ cấu lại, điều chỉnh kỳ hạn trả nợ toàn bộ khoản dư nợ này đến ngày 15-11-2013;
15. - Bên thế chấp là Công ty K phải hoàn tất thủ tục đăng ký thế chấp với thứ
16. tự ưu tiên thứ nhất cho Ngân hàng B-CN TP. HCM đối với hai xe ô tô hiệu Ford và
17. Audi.
18. Cùng ngày 23-05-2013, Ngân hàng B-CN TP. HCM và Công ty K đã ký kết Hợp đồng thế chấp số BOCHCM-MA-ME/007/2013. Theo đó, Công ty K đồng ý
19. sử dụng hai xe ô tô hiệu Ford và Audi để đảm bảo việc Công ty H thanh toán, thực hiện và hoàn thành đúng hạn mọi khoản tiền, nợ và nghĩa vụ đến hạn, còn nợ, hoặc phải gánh chịu của Công ty H đối với Ngân hàng B-CN TP. HCM theo quy định của Thư cấp tín dụng. Công ty K đồng thời đã gửi Ngân hàng B-CN TP. HCM Bản
20. cam kết số 06 CKKĐ/2013 đề ngày 23-05-2013, cam kết về kế hoạch hoàn trả nợ gốc và nợ lãi của khoản vay 1.928.000 USD với tư cách là bên bảo lãnh và bên thế chấp, do Công ty H không có khả năng trả nợ.
21. Ngày 03-06-2013, do trên thực tế Công ty H mới chỉ thanh toán được một phần khoản nợ gốc là 40.192 USD, tương đương 924.416.000 đồng nên Ngân hàng B-CN TP. HCM và Công ty H ký kết Sửa đổi Thư cấp tín dụng số BOCOMHCM-FL/008/2011-A2. Theo đó, tổng số dư nợ gốc vay còn lại là 1.928.000 USD, thời hạn trả nợ được gia hạn ngày 15-11-2013.
22. Từ ngày 25-10-2013, do số dư trong tài khoản của Công ty H không đủ để thanh toán tiền lãi cho các khoản vay nên Công ty H đã vi phạm nghĩa vụ trả tiền lãi hàng tháng theo Điều 2.1 của Thư Cấp Tín Dụng đối với đợt trả lãi từ 25-10-2013 đến ngày 15-11-2013.
23. Ngày 08-11-2013, Ngân hàng B-CN TP. HCM có văn bản gửi Công ty H và Công ty K đề nghị hoàn trả khoản dư nợ gốc và lãi cộng dồn trước ngày hết hạn của khoản vay (từ ngày 15-11-2013); đồng thời thông báo trong trường hợp Công ty H và Công ty K không thể sắp xếp vốn hoàn trả khoản dư nợ gốc và lãi cộng dồn khi đến hạn, Ngân hàng B-CN TP. HCM sẽ tiến hành các thủ tục xử lý tài sản bảo đảm để thu hồi nợ.
24. Ngày 25-03-2014, Ngân hàng B-CN TP. HCM thông qua đại diện theo ủy quyền đã tổ chức bán đấu giá tài sản bảo đảm được Công ty K thế chấp theo Hợp đồng thế chấp xe. Số tiền thu được từ việc bán đấu giá các tài sản bảo đảm trên là 1.375.000.000 đồng. Sau khi thanh toán chi phí cho việc xử lý tài sản bảo đảm là 375.000.000 đồng, khoản tiền là 1.000.000.000 đồng (tương đương 47.348,48 USD, tỷ giá quy đổi là 01 USD = 21.120 đồng) đã được trừ vào khoản nợ gốc của Công ty H đối với Ngân hàng B-CN TP. …
25. Trong khoảng thời gian từ ngày 30-12-2013 đến nay, Ngân hàng B-CN TP. HCM đã có nhiều văn bản, thông báo nhằm tiến hành việc xử lý các tài sản bảo đảm của Công ty K để thu hồi nợ, bao gồm các tài khoản bảo đảm theo hợp đồng thế chấp quyền sử dụng đất và tài sản hình thành trong tương lai. Tuy nhiên, do Công ty K cố tình không hợp tác với Ngân hàng B-CN TP. HCM nên việc tiến hành xử lý các tài sản thế chấp không thể thực hiện được. Ngân hàng B-CN TP. HCM được biết, cho đến ngày 25-09-2012, Công …
26. + Khoản dư nợ gốc là 1.871.441,44 USD tương đương 43.043.153.170 đồng.
27. + Tiền lãi trong hạn phát sinh trên nợ gốc còn lại là 1.313,87 USD tương
28. đương 30.219.000 đồng.
29. + Tiền lãi nợ quá hạn tạm tính là 867.711,68 USD tương đương
30. 19.957.368.547 đồng.
31. Vì vậy, với các lý do đã trình bày như trên, với mục đích đảm bảo việc giải quyết vụ án và bảo vệ quyền lợi cho Ngân hàng B-CN TP. HCM, bảo toàn tình trạng hiện có của tài sản thế chấp theo Hợp đồng thế chấp và tài sản hình thành trong tương lai số BOCOMHCM-MA-LUR/004/2011, các bên đã ký ngày 06-12-2011 đối với Quyền sử dụng đất và tài sản hình thành trong tương lai gắn liền với đất, tránh tình trạng vi phạm nghiêm trọng không thể khắc phục được, ảnh hưởng đến việc giải quyết vụ án và đảm bảo …
32. Sau khi xem xét Đơn yêu cầu áp dụng biện pháp khẩn cấp tạm thời của Ngân hàng B-CN TP. HCM, Tòa án nhân dân thành phố Hải Phòng đã ra Quyết
33. định áp dụng biện pháp khẩn cấp tạm thời số 1141/2017/QĐ-ADBPKCTT ngày 8-12-2017, nội dung: Buộc Công ty K…khi ký kết,thực hiện hợp đồng mua bán các căn hộ, cửa hàng của 07 tòa nhà: A2, A4,A5,A6,A7,A8,A9 tại Khu đô thị C, phường L, quận K, thành phố Hải Phòng phải thông báo bằng văn bản cho Ngân hàng B-CN TP. HCM và tất cả các khoản tiền đặt cọc, thanh toán của các hợp đồng mua bán tài sản thuộc tài sản thế chấp phải được thanh toán qua tài khoản của
34. Công ty TNHH Đầu tư K tại Ngân hàng B-CN TP. HCM.
35. * Ý kiến của Ngân hàng B đối với hành vi vi phạm của Công ty H:
36. - Công ty H đã vi phạm nghĩa vụ thanh toán nợ gốc (1.873.681,59 USD tương đương 43.043.153.170 đồng), theo thỏa thuận giữa các bên và theo quy định của pháp luật: Ngân hàng B-CN TP. HCM đã gia hạn nghĩa vụ trả nợ Công ty H đến ngày 15-11-2013. Tuy nhiên, cho đến nay, Công ty H vẫn chưa thực hiện hoàn trả đầy đủ khoản nợ gốc cho Ngân hàng. Đây là hành vi vi phạm nghĩa vụ trả nợ của bên vay theo thỏa thuận giữa các bên tại Thư cấp tín dụng và khoản 1 Điều 474 Bộ luật Dân sự.
37. - Công ty H đã vi phạm nghĩa vụ thanh toán lãi vay (1.313,87 USD tương đương 30.219.000 đồng) theo thỏa thuận giữa các bên và theo quy định của pháp luật: Công ty H đã cam kết và đảm bảo sẽ thanh toán đầy đủ vốn gốc và lãi phải của toàn bộ số dư nợ vay không trễ hơn ngày 15-11-2013. Công ty H đã vi phạm nghĩa vụ thanh toán lãi vay của bên vay theo thỏa thuận giữa các bên tại Thư cấp tín dụng và theo quy định tại Điều 471 Bộ luật Dân sự.
38. - Công ty H có trách nhiệm phải trả Ngân hàng khoản tiền lãi quá hạn phát sinh trên nợ gốc và lãi vay (867.711,68 USD tương đương 19.957.368.547 đồng) theo Thư cấp tín dụng và quy định của pháp luật.  Do Công ty H đã vi phạm nghĩa vụ thanh toán nợ gốc và nợ lãi, Công ty H có trách nhiệm phải trả Ngân hàng B-CN TP. HCM tiền lãi quá hạn được tính trên số dư nợ gốc và lãi trong hạn của mỗi khoản vay kể từ ngày đến hạn của mỗi khoản vay cho đến ngày toàn bộ số dư nợ gốc và lãi trong hạn được hoàn …
39. - Theo Điều 2.3 Thư cấp tín dụng, Công ty H đồng ý thanh toán cho Ngân hàng các loại phí theo biểu phí tiêu chuẩn của Ngân hàng. Như vậy, Công ty H phải thanh toán cho Ngân hàng B khoản phí chậm trả lãi trong hạn theo quy định của Ngân hàng.
40. - Đối với hành vi vi phạm nghĩa vụ bảo lãnh và nghĩa vụ của bên thế chấp của những người có quyền lợi, nghĩa vụ liên quan là Công ty K và ông Lam Wing C (Lâm Vinh T):
41. Công ty K và ông Lam Wing C (Lâm Vinh T) phải thực hiện nghĩa vụ bão lãnh theo các hợp đồng bảo lãnh được ký kết ngày 06-12-2011, do Công ty H
42. không thực hiện nghĩa vụ thanh toán toàn bộ số tiền mà Công ty H nợ Ngân hàng B-CN TP. HCM theo Thư cấp tín dụng đúng hạn. Ngân hàng B-CN TP. HCM đã quyền yêu cầu Công ty K và ông Lam Wing C (Lâm Vinh T) phải thực hiện nghĩa vụ bảo lãnh, thanh toán cho Ngân hàng B-CN TP. HCM toàn bộ số tiền mà Công ty H hiện đang nợ Ngân hàng B-CN TP. HCM theo Điều 365 Bộ luật Dân sự. Đến nay, mặc dù đã nhiều lần được Ngân hàng B-CN TP. HCM yêu cầu, cả Công ty K và ông Lam Wing C (Lâm Vinh T) đều chưa thực hiện …
43. Theo khoản 5, Điều 351 Bộ luật Dân sự và Điều 8.4 Hợp đồng thế chấp QSDĐ và TSHTTL, khi Công ty H vi phạm nghĩa vụ trả nợ theo Thư cấp tín dụng, Công ty K phải hỗ trợ và thực hiện các công việc cần thiết theo yêu cầu của Ngân hàng B-CN TP. HCM để tạo điều kiện cho việc xử lý Tài sản thế chấp. Tuy nhiên, Công ty K đã không những không hợp tác với Ngân hàng B-CN TP. HCM trong việc thu hồi và xử lý Tài sản thế chấp mà còn cố tình tiến hành chuyển nhượng trái phép một phần Tài sản thế chấp (Theo …
44. * Trong quá trình giải quyết vụ án và tại phiên tòa Ngân hàng B đề nghị Tòa án xem xét và quyết định:
45. 1. Buộc Công ty H thanh toán-10-2018 là 2.779.776,89 USD, tương đương 64.907.790.326 đồng (tỷ giá quy đổi 01USD = 23.350 đồng), bao gồm các khoản tiền cụ thể như sau:
46. + Dư nợ gốc là 1.871.441,44 USD (tương đương 43.698.157.675 đồng);
47. + Tiền lãi trong hạn là 1.313,87 USD (tương đương 30.678.855 đồng);
48. + Tiền lãi quá hạn được tính trên số dư nợ của khoản dư nợ gốc kể từ ngày đến hạn theo quy định tại Thư cấp tín dụng ngày 15-11-2013 đến ngày toàn bộ số dư nợ của khoản dư nợ gốc được thanh toán đầy đủ cho Ngân hàng B-CN TP. HCM. Tiền lãi quá hạn tạm tính đến ngày 10-10-2018 là: 907.021,58 USD (tương đương 21.178.953.797 đồng);
49. + Công ty H có trách nhiệm chịu khoản tiền lãi quá hạn của số tiền nợ gốc chưa thanh toán theo mức lãi suất các bên thỏa thuận trong hợp đồng tính từ ngày 11-10-2018 cho đến khi thanh toán xong khoản nợ gốc này.
50. 2. Trong trường hợp Công ty H không thực hiện nghĩa vụ thanh toán đầy đủ cho Ngân hàng B-CN TP. HCM toàn bộ số tiền gốc, các khoản tiền lãi nêu trên, Ngân hàng B đề nghị Tòa án nhân dân thành phố Hải Phòng:
51. - Buộc Công ty K và ông Lam Wing C (Lâm Vinh T) phải trả nợ Ngân hàng B-CN TP. HCM thay cho Công ty H theo nghĩa vụ đã bảo lãnh tại các Hợp đồng bảo lãnh được ký kết vào ngày 06-12-2011;
52. - Công ty K và ông Lam Wing C (Lâm Vinh T) không thực hiện nghĩa vụ hoặc thực hiện nghĩa vụ không đầy đủ cho Ngân hàng B-CN TP. HCM thì Ngân hàng B được yêu cầu Cơ quan có thẩm quyền phát mại các tài sản đảm bảo để Ngân hàng B-CN TP. HCM thu hồi nợ, bao gồm:
53. +  Quyền sử dụng đất của Công ty K đối với lô đất có tổng diện tích 5000m2 tại Khu đô thị C, đường L, phường B, quận K, thành Phố Hải Phòng;
54. + Tài sản gắn liền với đất: là 07 tòa nhà chung cư, bao gồm các tòa nhà A2, A4, A5, A6, A7, A8, A9 tại Khu đô thị C, đường L, phường B, quận K, thành phố Hải Phòng có tổng diện tích sàn là 21.563,92m2.
55. 3. Tại phiên tòa hôm nay nguyên đơn rút một phần yêu cầu khởi kiện, là khoản phí chậm trả lãi trong hạn 236.26 USD và phát sinh cho đến ngày xét xử;
56. thanh toán các chi phí như luật sư và chi phí phát sinh. Người đại diện hợp pháp của bị đơn trong suốt quá tình giải quyết vụ án đã được Tòa án thông báo, triệu tập hợp lệ nhưng không có mặt tại Tòa án, không có lời khai trong hồ sơ vụ án, không giao nộp tài liệu chứng cứ cho Tòa án.
57. Theo ý kiến của Công ty K và ông Lam Wing C- Giám đốc Công ty K, đồng thời là người có quyền lợi, nghĩa vụ liên quan đến vụ án vắng mặt tại phiên tòa nhưng trong quá trình giải quyết vụ án trình bày:
58. Công ty K sẽ chịu trách nhiệm trả nợ Ngân hàng thay cho Công ty H theo nghĩa vụ bảo lãnh tại các Hợp đồng bảo lãnh số BOCOMHCM-GA/010/2011 và số BOCOMHCM-GA/006/2011 được ký kết vào ngày 06-12-2012. Về ý kiến của Ngân hàng đưa ra về việc ngày 25-9-2012, Công ty K đã chuyển nhượng trái phép hơn 100 căn nhà và cửa hàng thuộc tài sản đảm bảo theo hợp đồng thế chấp để thu hồi số tiền là 95.807.675.000 đồng mà không thông báo cho Ngân hàng là sai. Về vấn đề này, Công ty K có ý kiến như sau: Năm …
59. Công ty Cổ phần X (viết tắt là Công ty X) cùng với Công ty Công trình kiến trúc K, tỉnh Phúc Kiến, Trung Quốc góp vốn thành lập Công ty TNHH Đầu tư K, Việt Nam. Công ty Cổ phần X góp vốn bằng giá trị quyền sử dụng đất 9300m2 đất ở tại Khu đô thị C, phường B, quận K, Hải Phòng. Công ty có biết và đồng ý Công ty K thế chấp quyền sử dụng đất 5000m2 tại Ngân hàng B để đảm bảo cho khoản vay của Công ty H, điều này thể hiện tại Biên bản họp thành viên của Công ty K.
60. Về yêu cầu khởi kiện của Ngân hàng đối với Công ty H và Công ty K, Công ty X giữ nguyên quan điểm về việc ký kết Hợp đồng tín dụng cũng như Hợp đồng thế chấp là mối quan hệ giữa Ngân hàng với Công ty H và Công ty K. Công ty X không liên quan đến vụ án này. Công ty không nắm được cụ thể việc tiêu thụ
61. chuyển nhượng các căn hộ trên khu đất 5000m2 tại Khu đô thị C và đề nghị Tòa án giải quyết vụ án theo quy định của pháp luật, Công ty xác định Công ty không phải là người có quyền lợi nghĩa vụ liên quan trong vụ án này. Tại phiên tòa ông Bùi Văn D - Phó Tổng Giám đốc Công ty và bà Ngô Thục L - nhân viên Công ty K trình bày: Ông D được ủy quyền về hành chính, điều hành công việc hàng ngày của Công ty K nhưng không được ủy quyền tham gia tố tụng tại Tòa án, những công việc quan trọng ông D đều …
62. phiên tòa để theo dõi kết quả xét xử của Tòa án để báo cáo lại ông Lam Wing C. Kiểm sát viên phát biểu ý kiến:
63. - Trong quá trình giải quyết vụ án Thẩm phán, Hội đồng xét xử, Thư ký đã chấp hành đúng các quy định của Bộ luật Tố tụng dân sự. Các đương sự đã thực hiện đúng các quy định về quyền và nghĩa vụ của mình.
64. - Về quan điểm giải quyết vụ án: Tại phiên tòa hôm nay, người đại diện hợp pháp của nguyên đơn rút một phần yêu cầu khởi kiện, là khoản phí chậm trả lãi trong hạn 236.26 USD và phát sinh cho đến ngày xét xử; thanh toán các chi phí như luật sư và chi phí phát sinh, xét thấy việc rút là tự nguyện, đề nghị HĐXX căn cứ khoản 2 Điều 244 Bộ luật Tố tụng dân sự chấp nhận và đình chỉ xét xử đối với phần yêu cầu đã rút.
65. Về hiệu lực của Hợp đồng tín dụng và hợp đồng thế chấp: Nội dung và hình thức của các Hợp đồng đều phù hợp với các quy định của Bộ luật Dân sự và Luật các tổ chức tín dụng. Các hợp đồng đã được công chứng và tài sản thế chấp cũng đã được đăng ký giao dịch bảo đảm theo đúng quy định của pháp luật nên các hợp đồng có hiệu lực pháp luật, phát sinh quyền và nghĩa vụ ràng buộc đối với các bên. Quá trình thực hiện hợp đồng, nguyên đơn đã giải ngân số tiền vay theo đúng thỏa thuận, tuy nhiên bị đơn đã …
66. gốc, tiền lãi trong hạn, lãi quá hạn tính đến ngày xét xử sơ thẩm (10-10-2018) có căn cứ để chấp nhận: Nợ gốc: 1.871.441,44 USD, nợ lãi (trong hạn + quá hạn):
67. 908.335,45 USD (theo tỷ giá 01 USD = 23.350 đồng); quy đổi sang tiền Việt Nam tương đương: Nợ gốc: 43.698.157.675 đồng, nợ lãi (trong hạn + quá hạn): 21.209.632.651 đồng, tổng: 64.907.790.326 đồng. Trường hợp Công ty H không thanh toán khoản đầy đủ cho ngân hàng,  thì buộc Công ty K và ông Lam Wing C có nghĩa vụ trả thay cho Công ty H, nếu không trả được nợ thì được quyền yêu cầu phát mại tài sản thế chấp để thu hồi nợ cho Ngân hàng theo hợp đồng thế chấp đã ký kết. Về các tài sản thế chấp: …
Considering the following rules: Applicable provisions of Vietnamese law:
1. [BLDS 2015] Điều 155. Không áp dụng thời hiệu khởi kiện. Thời hiệu khởi kiện không áp dụng trong trường hợp sau đây: 1. Yêu cầu bảo vệ quyền nhân thân không gắn với tài sản; 2. Yêu cầu bảo vệ quyền sở hữu, trừ trường hợp Bộ luật này, luật khác có liên quan quy định khác; 3. Tranh chấp về quyền sử dụng đất theo quy định của Luật đất đai; 4. Trường hợp khác do luật quy định
2. [BLDS 2015] Điều 478. Nghĩa vụ bảo đảm quyền sử dụng tài sản cho bên thuê. 1. Bên cho thuê phải bảo đảm quyền sử dụng tài sản ổn định cho bên thuê. 2. Trường hợp có tranh chấp về quyền sở hữu đối với tài sản thuê mà bên thuê không được sử dụng tài sản ổn định thì bên thuê có quyền đơn phương chấm dứt thực hiện hợp đồng và yêu cầu bồi thường thiệt hại
3. [BLDS 2015] Điều 429. Thời hiệu khởi kiện về hợp đồng. Thời hiệu khởi kiện để yêu cầu Tòa án giải quyết tranh chấp hợp đồng là 03 năm, kể từ ngày người có quyền yêu cầu biết hoặc phải biết quyền và lợi ích hợp pháp của mình bị xâm phạm. Chương XVI MỘT SỐ HỢP ĐỒNG THÔNG DỤNG Mục 1 HỢP ĐỒNG MUA BÁN TÀI SẢN
4. [BLDS 2015] Điều 336. Phạm vi bảo lãnh. 1. Bên bảo lãnh có thể cam kết bảo lãnh một phần hoặc toàn bộ nghĩa vụ cho bên được bảo lãnh. 2. Nghĩa vụ bảo lãnh bao gồm cả tiền lãi trên nợ gốc, tiền phạt, tiền bồi thường thiệt hại, lãi trên số tiền chậm trả, trừ trường hợp có thoả thuận khác. 3. Các bên có thể thỏa thuận sử dụng biện pháp bảo đảm bằng tài sản để bảo đảm thực hiện nghĩa vụ bảo lãnh. 4. Trường hợp nghĩa vụ được bảo lãnh là nghĩa vụ phát sinh trong tương lai thì phạm vi bảo lãnh không bao gồm nghĩa vụ phát sinh sau khi người bảo lãnh chết hoặc pháp nhân bảo lãnh chấm dứt tồn tại
5. [BLDS 2015] Điều 321. Quyền của bên thế chấp. 1. Khai thác công dụng, hưởng hoa lợi, lợi tức từ tài sản thế chấp, trừ trường hợp hoa lợi, lợi tức cũng là tài sản thế chấp theo thoả thuận. 2. Đầu tư để làm tăng giá trị của tài sản thế chấp. 3. Nhận lại tài sản thế chấp do người thứ ba giữ và giấy tờ liên quan đến tài sản thế chấp do bên nhận thế chấp giữ khi nghĩa vụ được bảo đảm bằng thế chấp chấm dứt hoặc được thay thế bằng biện pháp bảo đảm khác. 4. Được bán, thay thế, trao đổi tài sản thế chấp, nếu tài sản đó là hàng hoá luân chuyển trong quá trình sản xuất, kinh doanh. Trong trường hợp này, quyền yêu cầu bên mua thanh toán tiền, số tiền thu được, tài sản hình thành từ số tiền thu được, tài sản được thay thế h
According to the given rules, please evaluate whether the court accepts the plaintiff's claims in whole or in part.
```
**Response**
```
Dựa trên các quy định được cung cấp và các thông tin về vụ việc đã nêu, tôi sẽ phân tích từng bước để đánh giá xem Tòa án có chấp nhận yêu cầu của nguyên đơn (Ngân hàng B-CN TP. HCM) trong toàn bộ hay một phần.

1. **Thời hiệu khởi kiện**: Theo Điều 155 BLDS 2015, thời hiệu khởi kiện không áp dụng trong trường hợp yêu cầu bảo vệ quyền nhân thân không gắn với tài sản. Vụ việc này không liên quan đến quyền nhân thân, nên thời hiệu không áp dụng.

2. **Quyền bảo lãnh và nghĩa vụ bảo đảm**: Theo Điều 321 BLDS 2015, bên thế chấp có quyền khai thác công dụng, hưởng hoa lợi, lợi tức từ tài sản thế chấp, trừ trường hợp hoa lợi, lợi tức cũng là tài sản thế chấp theo thỏa thuận. Ngân hàng B-CN TP. HCM đã ký hợp đồng thế chấp với Công ty K và ông Lam Wing C, nên họ có quyền khai thác tài sản thế chấp.

3. **Quyền của bên thế chấp**: Theo Điều 321 BLDS 2015, bên thế chấp có quyền nhận lại tài sản thế chấp do người thứ ba giữ và giấy tờ liên quan đến tài sản thế chấp khi nghĩa vụ được bảo đảm bằng thế chấp chấm dứt hoặc được thay thế bằng biện pháp bảo đảm khác. Ngân hàng B-CN TP. HCM đã yêu cầu Công ty K và ông Lam Wing C thực hiện nghĩa vụ bảo lãnh, nên họ có quyền nhận lại tài sản thế chấp.

4. **Quyền của bên bảo lãnh**: Theo Điều 336 BLDS 2015, bên bảo lãnh có thể cam kết bảo lãnh một phần hoặc toàn bộ nghĩa vụ cho bên được bảo lãnh. Ngân hàng B-CN TP. HCM đã ký hợp đồng bảo lãnh với Công ty K và ông Lam Wing C, nên họ có quyền đòi Công ty K và ông Lam Wing C trả nợ thay cho Công ty H.

5. **Quyền của bên mua**: Theo Điều 321 BLDS 2015, bên thế chấp có quyền bán, thay thế, trao đổi tài sản thế chấp nếu tài sản đó là hàng hoá luân chuyển trong quá trình sản xuất, kinh doanh. Ngân hàng B-CN TP. HCM đã yêu cầu bán tài sản thế chấp, nên họ có quyền yêu cầu bên mua thanh toán tiền, số tiền thu được, tài sản hình thành từ số tiền thu được, tài sản được thay thế.

Như vậy, tất cả các quyền và nghĩa vụ của Ngân hàng B-CN TP. HCM được xác định rõ ràng trong các hợp đồng và quy định pháp luật. 

**Kết luận**:
```

## A.2#1 — abductive (defendant)

**Prompt**
```
Considering the following facts:
1. Theo đơn khởi kiện,các tài liệu có trong hồ sơ vụ án và lời khai của nguyên đơn tại phiên tòa thể hiện:
2. Ngày 06-12-2011, Ngân hàng B (sau gọi tắt Ngân hàng) và Công ty TNHH Thương mại và Xuất nhập khẩu H (sau gọi tắt Công ty H) ký kết Thư Cấp Tín
3. dụng số BOCOMHCM-FL/008/2011, theo đó Ngân hàng đồng ý cấp cho Công ty H một khoản tín dụng tuần hoàn ngắn hạn với hạn mức tín dụng là 2.000.000 USD
4. (Đô la Mỹ), tương đương 46.000.000.000 Việt Nam đồng (tỷ giá 01USD = 23.000VNĐ) để Công ty H sử dụng làm vốn lưu động. Trong khoảng thời gian từ 26-11-2012 cho đến ngày 05-12-2012, Ngân hàng đã thực hiện giải ngân cho Công ty H 04 lần với tổng số tiền vay là 1.968.192 USD, tương đương 45.268.416.000 đồng (Việt Nam đồng).
5. Ngày 06-12-2011, Công ty TNHH Đầu tư K (sau gọi tắt Công ty K) và cá nhân ông Lam Wing C (Lâm Vinh T) là người đại diện theo pháp luật của Công ty
6. K đã ký các hợp đồng bảo lãnh với Ngân hàng để bảo lãnh cho việc thanh toán đúng hạn toàn bộ số tiền mà Công ty H nợ Ngân hàng theo Thư cấp tín Dụng khi
7. số tiền đó đến hạn và phải trả cho Ngân hàng. Cùng ngày 06-12-2011, Công ty K và Ngân hàng B chi nhánh thành phố Hồ Chí Minh (sau viết tắt Ngân hàng B-CN TP. HCM)  đã ký kết Hợp đồng thế chấp số BOCOMHCM-MA-LUR/004/2011. Theo đó, Công ty K đồng ý sử dụng các tài sản thuộc sở hữu của mình làm tài sản thế chấp để bảo đảm cho việc hoàn trả mọi khoản tiền, nợ và nghĩa vụ hiện tại và tương lai đến hạn, còn nợ hoặc phải gánh chịu của Công ty H đối với Ngân hàng B-CN TP. HCM theo quy định của Thư cấp …
8. - Quyền sử dụng đất của Công ty K đối với lô đất có tổng diện tích 5000m2 tại Khu đô thị C, đường L, phường B, quận K, Thành Phố Hải Phòng;
9. - Tài sản hình thành trong tương lai gắn liền với đất: là 07 tòa nhà chung cư, bao gồm các tòa nhà A2, A4, A5, A6, A7, A8, A9 tại Khu đô thị C, đường L, phường B, quận K, thành phố Hải Phòng có tổng diện tích sàn là 21.563,92m2.
10. Ngày 23-05-2013, Ngân hàng B-CN TP. HCM và Công ty H ký kết sửa đổi Thư cấp tín dụng số BOCOMHCM-FL/008/2011-A1 để sửa đổi, bổ sung một số điều khoản của Thư cấp tín dụng. Theo đó, các bên đã thống nhất như sau:
11. - Gia hạn thời hạn hiệu lực của Thư cấp tín dụng;
12. - Khoản nợ gốc sẽ được cơ cấu lại phụ thuộc vào các điều kiện sau:
13. + Công ty H cam kết thanh toán đầy đủ số tiền gốc là 108.000 USD và lãi cộng dồn trước ngày 03-06-2013;
14. + Tổng dư nợ vay còn lại là 1.860.000 USD và sẽ được cơ cấu lại, điều chỉnh kỳ hạn trả nợ toàn bộ khoản dư nợ này đến ngày 15-11-2013;
15. - Bên thế chấp là Công ty K phải hoàn tất thủ tục đăng ký thế chấp với thứ
16. tự ưu tiên thứ nhất cho Ngân hàng B-CN TP. HCM đối với hai xe ô tô hiệu Ford và
17. Audi.
18. Cùng ngày 23-05-2013, Ngân hàng B-CN TP. HCM và Công ty K đã ký kết Hợp đồng thế chấp số BOCHCM-MA-ME/007/2013. Theo đó, Công ty K đồng ý
19. sử dụng hai xe ô tô hiệu Ford và Audi để đảm bảo việc Công ty H thanh toán, thực hiện và hoàn thành đúng hạn mọi khoản tiền, nợ và nghĩa vụ đến hạn, còn nợ, hoặc phải gánh chịu của Công ty H đối với Ngân hàng B-CN TP. HCM theo quy định của Thư cấp tín dụng. Công ty K đồng thời đã gửi Ngân hàng B-CN TP. HCM Bản
20. cam kết số 06 CKKĐ/2013 đề ngày 23-05-2013, cam kết về kế hoạch hoàn trả nợ gốc và nợ lãi của khoản vay 1.928.000 USD với tư cách là bên bảo lãnh và bên thế chấp, do Công ty H không có khả năng trả nợ.
21. Ngày 03-06-2013, do trên thực tế Công ty H mới chỉ thanh toán được một phần khoản nợ gốc là 40.192 USD, tương đương 924.416.000 đồng nên Ngân hàng B-CN TP. HCM và Công ty H ký kết Sửa đổi Thư cấp tín dụng số BOCOMHCM-FL/008/2011-A2. Theo đó, tổng số dư nợ gốc vay còn lại là 1.928.000 USD, thời hạn trả nợ được gia hạn ngày 15-11-2013.
22. Từ ngày 25-10-2013, do số dư trong tài khoản của Công ty H không đủ để thanh toán tiền lãi cho các khoản vay nên Công ty H đã vi phạm nghĩa vụ trả tiền lãi hàng tháng theo Điều 2.1 của Thư Cấp Tín Dụng đối với đợt trả lãi từ 25-10-2013 đến ngày 15-11-2013.
23. Ngày 08-11-2013, Ngân hàng B-CN TP. HCM có văn bản gửi Công ty H và Công ty K đề nghị hoàn trả khoản dư nợ gốc và lãi cộng dồn trước ngày hết hạn của khoản vay (từ ngày 15-11-2013); đồng thời thông báo trong trường hợp Công ty H và Công ty K không thể sắp xếp vốn hoàn trả khoản dư nợ gốc và lãi cộng dồn khi đến hạn, Ngân hàng B-CN TP. HCM sẽ tiến hành các thủ tục xử lý tài sản bảo đảm để thu hồi nợ.
24. Ngày 25-03-2014, Ngân hàng B-CN TP. HCM thông qua đại diện theo ủy quyền đã tổ chức bán đấu giá tài sản bảo đảm được Công ty K thế chấp theo Hợp đồng thế chấp xe. Số tiền thu được từ việc bán đấu giá các tài sản bảo đảm trên là 1.375.000.000 đồng. Sau khi thanh toán chi phí cho việc xử lý tài sản bảo đảm là 375.000.000 đồng, khoản tiền là 1.000.000.000 đồng (tương đương 47.348,48 USD, tỷ giá quy đổi là 01 USD = 21.120 đồng) đã được trừ vào khoản nợ gốc của Công ty H đối với Ngân hàng B-CN TP. …
25. Trong khoảng thời gian từ ngày 30-12-2013 đến nay, Ngân hàng B-CN TP. HCM đã có nhiều văn bản, thông báo nhằm tiến hành việc xử lý các tài sản bảo đảm của Công ty K để thu hồi nợ, bao gồm các tài khoản bảo đảm theo hợp đồng thế chấp quyền sử dụng đất và tài sản hình thành trong tương lai. Tuy nhiên, do Công ty K cố tình không hợp tác với Ngân hàng B-CN TP. HCM nên việc tiến hành xử lý các tài sản thế chấp không thể thực hiện được. Ngân hàng B-CN TP. HCM được biết, cho đến ngày 25-09-2012, Công …
26. + Khoản dư nợ gốc là 1.871.441,44 USD tương đương 43.043.153.170 đồng.
27. + Tiền lãi trong hạn phát sinh trên nợ gốc còn lại là 1.313,87 USD tương
28. đương 30.219.000 đồng.
29. + Tiền lãi nợ quá hạn tạm tính là 867.711,68 USD tương đương
30. 19.957.368.547 đồng.
31. Vì vậy, với các lý do đã trình bày như trên, với mục đích đảm bảo việc giải quyết vụ án và bảo vệ quyền lợi cho Ngân hàng B-CN TP. HCM, bảo toàn tình trạng hiện có của tài sản thế chấp theo Hợp đồng thế chấp và tài sản hình thành trong tương lai số BOCOMHCM-MA-LUR/004/2011, các bên đã ký ngày 06-12-2011 đối với Quyền sử dụng đất và tài sản hình thành trong tương lai gắn liền với đất, tránh tình trạng vi phạm nghiêm trọng không thể khắc phục được, ảnh hưởng đến việc giải quyết vụ án và đảm bảo …
32. Sau khi xem xét Đơn yêu cầu áp dụng biện pháp khẩn cấp tạm thời của Ngân hàng B-CN TP. HCM, Tòa án nhân dân thành phố Hải Phòng đã ra Quyết
33. định áp dụng biện pháp khẩn cấp tạm thời số 1141/2017/QĐ-ADBPKCTT ngày 8-12-2017, nội dung: Buộc Công ty K…khi ký kết,thực hiện hợp đồng mua bán các căn hộ, cửa hàng của 07 tòa nhà: A2, A4,A5,A6,A7,A8,A9 tại Khu đô thị C, phường L, quận K, thành phố Hải Phòng phải thông báo bằng văn bản cho Ngân hàng B-CN TP. HCM và tất cả các khoản tiền đặt cọc, thanh toán của các hợp đồng mua bán tài sản thuộc tài sản thế chấp phải được thanh toán qua tài khoản của
34. Công ty TNHH Đầu tư K tại Ngân hàng B-CN TP. HCM.
35. * Ý kiến của Ngân hàng B đối với hành vi vi phạm của Công ty H:
36. - Công ty H đã vi phạm nghĩa vụ thanh toán nợ gốc (1.873.681,59 USD tương đương 43.043.153.170 đồng), theo thỏa thuận giữa các bên và theo quy định của pháp luật: Ngân hàng B-CN TP. HCM đã gia hạn nghĩa vụ trả nợ Công ty H đến ngày 15-11-2013. Tuy nhiên, cho đến nay, Công ty H vẫn chưa thực hiện hoàn trả đầy đủ khoản nợ gốc cho Ngân hàng. Đây là hành vi vi phạm nghĩa vụ trả nợ của bên vay theo thỏa thuận giữa các bên tại Thư cấp tín dụng và khoản 1 Điều 474 Bộ luật Dân sự.
37. - Công ty H đã vi phạm nghĩa vụ thanh toán lãi vay (1.313,87 USD tương đương 30.219.000 đồng) theo thỏa thuận giữa các bên và theo quy định của pháp luật: Công ty H đã cam kết và đảm bảo sẽ thanh toán đầy đủ vốn gốc và lãi phải của toàn bộ số dư nợ vay không trễ hơn ngày 15-11-2013. Công ty H đã vi phạm nghĩa vụ thanh toán lãi vay của bên vay theo thỏa thuận giữa các bên tại Thư cấp tín dụng và theo quy định tại Điều 471 Bộ luật Dân sự.
38. - Công ty H có trách nhiệm phải trả Ngân hàng khoản tiền lãi quá hạn phát sinh trên nợ gốc và lãi vay (867.711,68 USD tương đương 19.957.368.547 đồng) theo Thư cấp tín dụng và quy định của pháp luật.  Do Công ty H đã vi phạm nghĩa vụ thanh toán nợ gốc và nợ lãi, Công ty H có trách nhiệm phải trả Ngân hàng B-CN TP. HCM tiền lãi quá hạn được tính trên số dư nợ gốc và lãi trong hạn của mỗi khoản vay kể từ ngày đến hạn của mỗi khoản vay cho đến ngày toàn bộ số dư nợ gốc và lãi trong hạn được hoàn …
39. - Theo Điều 2.3 Thư cấp tín dụng, Công ty H đồng ý thanh toán cho Ngân hàng các loại phí theo biểu phí tiêu chuẩn của Ngân hàng. Như vậy, Công ty H phải thanh toán cho Ngân hàng B khoản phí chậm trả lãi trong hạn theo quy định của Ngân hàng.
40. - Đối với hành vi vi phạm nghĩa vụ bảo lãnh và nghĩa vụ của bên thế chấp của những người có quyền lợi, nghĩa vụ liên quan là Công ty K và ông Lam Wing C (Lâm Vinh T):
41. Công ty K và ông Lam Wing C (Lâm Vinh T) phải thực hiện nghĩa vụ bão lãnh theo các hợp đồng bảo lãnh được ký kết ngày 06-12-2011, do Công ty H
42. không thực hiện nghĩa vụ thanh toán toàn bộ số tiền mà Công ty H nợ Ngân hàng B-CN TP. HCM theo Thư cấp tín dụng đúng hạn. Ngân hàng B-CN TP. HCM đã quyền yêu cầu Công ty K và ông Lam Wing C (Lâm Vinh T) phải thực hiện nghĩa vụ bảo lãnh, thanh toán cho Ngân hàng B-CN TP. HCM toàn bộ số tiền mà Công ty H hiện đang nợ Ngân hàng B-CN TP. HCM theo Điều 365 Bộ luật Dân sự. Đến nay, mặc dù đã nhiều lần được Ngân hàng B-CN TP. HCM yêu cầu, cả Công ty K và ông Lam Wing C (Lâm Vinh T) đều chưa thực hiện …
43. Theo khoản 5, Điều 351 Bộ luật Dân sự và Điều 8.4 Hợp đồng thế chấp QSDĐ và TSHTTL, khi Công ty H vi phạm nghĩa vụ trả nợ theo Thư cấp tín dụng, Công ty K phải hỗ trợ và thực hiện các công việc cần thiết theo yêu cầu của Ngân hàng B-CN TP. HCM để tạo điều kiện cho việc xử lý Tài sản thế chấp. Tuy nhiên, Công ty K đã không những không hợp tác với Ngân hàng B-CN TP. HCM trong việc thu hồi và xử lý Tài sản thế chấp mà còn cố tình tiến hành chuyển nhượng trái phép một phần Tài sản thế chấp (Theo …
44. * Trong quá trình giải quyết vụ án và tại phiên tòa Ngân hàng B đề nghị Tòa án xem xét và quyết định:
45. 1. Buộc Công ty H thanh toán-10-2018 là 2.779.776,89 USD, tương đương 64.907.790.326 đồng (tỷ giá quy đổi 01USD = 23.350 đồng), bao gồm các khoản tiền cụ thể như sau:
46. + Dư nợ gốc là 1.871.441,44 USD (tương đương 43.698.157.675 đồng);
47. + Tiền lãi trong hạn là 1.313,87 USD (tương đương 30.678.855 đồng);
48. + Tiền lãi quá hạn được tính trên số dư nợ của khoản dư nợ gốc kể từ ngày đến hạn theo quy định tại Thư cấp tín dụng ngày 15-11-2013 đến ngày toàn bộ số dư nợ của khoản dư nợ gốc được thanh toán đầy đủ cho Ngân hàng B-CN TP. HCM. Tiền lãi quá hạn tạm tính đến ngày 10-10-2018 là: 907.021,58 USD (tương đương 21.178.953.797 đồng);
49. + Công ty H có trách nhiệm chịu khoản tiền lãi quá hạn của số tiền nợ gốc chưa thanh toán theo mức lãi suất các bên thỏa thuận trong hợp đồng tính từ ngày 11-10-2018 cho đến khi thanh toán xong khoản nợ gốc này.
50. 2. Trong trường hợp Công ty H không thực hiện nghĩa vụ thanh toán đầy đủ cho Ngân hàng B-CN TP. HCM toàn bộ số tiền gốc, các khoản tiền lãi nêu trên, Ngân hàng B đề nghị Tòa án nhân dân thành phố Hải Phòng:
51. - Buộc Công ty K và ông Lam Wing C (Lâm Vinh T) phải trả nợ Ngân hàng B-CN TP. HCM thay cho Công ty H theo nghĩa vụ đã bảo lãnh tại các Hợp đồng bảo lãnh được ký kết vào ngày 06-12-2011;
52. - Công ty K và ông Lam Wing C (Lâm Vinh T) không thực hiện nghĩa vụ hoặc thực hiện nghĩa vụ không đầy đủ cho Ngân hàng B-CN TP. HCM thì Ngân hàng B được yêu cầu Cơ quan có thẩm quyền phát mại các tài sản đảm bảo để Ngân hàng B-CN TP. HCM thu hồi nợ, bao gồm:
53. +  Quyền sử dụng đất của Công ty K đối với lô đất có tổng diện tích 5000m2 tại Khu đô thị C, đường L, phường B, quận K, thành Phố Hải Phòng;
54. + Tài sản gắn liền với đất: là 07 tòa nhà chung cư, bao gồm các tòa nhà A2, A4, A5, A6, A7, A8, A9 tại Khu đô thị C, đường L, phường B, quận K, thành phố Hải Phòng có tổng diện tích sàn là 21.563,92m2.
55. 3. Tại phiên tòa hôm nay nguyên đơn rút một phần yêu cầu khởi kiện, là khoản phí chậm trả lãi trong hạn 236.26 USD và phát sinh cho đến ngày xét xử;
56. thanh toán các chi phí như luật sư và chi phí phát sinh. Người đại diện hợp pháp của bị đơn trong suốt quá tình giải quyết vụ án đã được Tòa án thông báo, triệu tập hợp lệ nhưng không có mặt tại Tòa án, không có lời khai trong hồ sơ vụ án, không giao nộp tài liệu chứng cứ cho Tòa án.
57. Theo ý kiến của Công ty K và ông Lam Wing C- Giám đốc Công ty K, đồng thời là người có quyền lợi, nghĩa vụ liên quan đến vụ án vắng mặt tại phiên tòa nhưng trong quá trình giải quyết vụ án trình bày:
58. Công ty K sẽ chịu trách nhiệm trả nợ Ngân hàng thay cho Công ty H theo nghĩa vụ bảo lãnh tại các Hợp đồng bảo lãnh số BOCOMHCM-GA/010/2011 và số BOCOMHCM-GA/006/2011 được ký kết vào ngày 06-12-2012. Về ý kiến của Ngân hàng đưa ra về việc ngày 25-9-2012, Công ty K đã chuyển nhượng trái phép hơn 100 căn nhà và cửa hàng thuộc tài sản đảm bảo theo hợp đồng thế chấp để thu hồi số tiền là 95.807.675.000 đồng mà không thông báo cho Ngân hàng là sai. Về vấn đề này, Công ty K có ý kiến như sau: Năm …
59. Công ty Cổ phần X (viết tắt là Công ty X) cùng với Công ty Công trình kiến trúc K, tỉnh Phúc Kiến, Trung Quốc góp vốn thành lập Công ty TNHH Đầu tư K, Việt Nam. Công ty Cổ phần X góp vốn bằng giá trị quyền sử dụng đất 9300m2 đất ở tại Khu đô thị C, phường B, quận K, Hải Phòng. Công ty có biết và đồng ý Công ty K thế chấp quyền sử dụng đất 5000m2 tại Ngân hàng B để đảm bảo cho khoản vay của Công ty H, điều này thể hiện tại Biên bản họp thành viên của Công ty K.
60. Về yêu cầu khởi kiện của Ngân hàng đối với Công ty H và Công ty K, Công ty X giữ nguyên quan điểm về việc ký kết Hợp đồng tín dụng cũng như Hợp đồng thế chấp là mối quan hệ giữa Ngân hàng với Công ty H và Công ty K. Công ty X không liên quan đến vụ án này. Công ty không nắm được cụ thể việc tiêu thụ
61. chuyển nhượng các căn hộ trên khu đất 5000m2 tại Khu đô thị C và đề nghị Tòa án giải quyết vụ án theo quy định của pháp luật, Công ty xác định Công ty không phải là người có quyền lợi nghĩa vụ liên quan trong vụ án này. Tại phiên tòa ông Bùi Văn D - Phó Tổng Giám đốc Công ty và bà Ngô Thục L - nhân viên Công ty K trình bày: Ông D được ủy quyền về hành chính, điều hành công việc hàng ngày của Công ty K nhưng không được ủy quyền tham gia tố tụng tại Tòa án, những công việc quan trọng ông D đều …
62. phiên tòa để theo dõi kết quả xét xử của Tòa án để báo cáo lại ông Lam Wing C. Kiểm sát viên phát biểu ý kiến:
63. - Trong quá trình giải quyết vụ án Thẩm phán, Hội đồng xét xử, Thư ký đã chấp hành đúng các quy định của Bộ luật Tố tụng dân sự. Các đương sự đã thực hiện đúng các quy định về quyền và nghĩa vụ của mình.
64. - Về quan điểm giải quyết vụ án: Tại phiên tòa hôm nay, người đại diện hợp pháp của nguyên đơn rút một phần yêu cầu khởi kiện, là khoản phí chậm trả lãi trong hạn 236.26 USD và phát sinh cho đến ngày xét xử; thanh toán các chi phí như luật sư và chi phí phát sinh, xét thấy việc rút là tự nguyện, đề nghị HĐXX căn cứ khoản 2 Điều 244 Bộ luật Tố tụng dân sự chấp nhận và đình chỉ xét xử đối với phần yêu cầu đã rút.
65. Về hiệu lực của Hợp đồng tín dụng và hợp đồng thế chấp: Nội dung và hình thức của các Hợp đồng đều phù hợp với các quy định của Bộ luật Dân sự và Luật các tổ chức tín dụng. Các hợp đồng đã được công chứng và tài sản thế chấp cũng đã được đăng ký giao dịch bảo đảm theo đúng quy định của pháp luật nên các hợp đồng có hiệu lực pháp luật, phát sinh quyền và nghĩa vụ ràng buộc đối với các bên. Quá trình thực hiện hợp đồng, nguyên đơn đã giải ngân số tiền vay theo đúng thỏa thuận, tuy nhiên bị đơn đã …
66. gốc, tiền lãi trong hạn, lãi quá hạn tính đến ngày xét xử sơ thẩm (10-10-2018) có căn cứ để chấp nhận: Nợ gốc: 1.871.441,44 USD, nợ lãi (trong hạn + quá hạn):
67. 908.335,45 USD (theo tỷ giá 01 USD = 23.350 đồng); quy đổi sang tiền Việt Nam tương đương: Nợ gốc: 43.698.157.675 đồng, nợ lãi (trong hạn + quá hạn): 21.209.632.651 đồng, tổng: 64.907.790.326 đồng. Trường hợp Công ty H không thanh toán khoản đầy đủ cho ngân hàng,  thì buộc Công ty K và ông Lam Wing C có nghĩa vụ trả thay cho Công ty H, nếu không trả được nợ thì được quyền yêu cầu phát mại tài sản thế chấp để thu hồi nợ cho Ngân hàng theo hợp đồng thế chấp đã ký kết. Về các tài sản thế chấp: …
Considering the following rules: Applicable provisions of Vietnamese law:
1. [BLDS 2015] Điều 155. Không áp dụng thời hiệu khởi kiện. Thời hiệu khởi kiện không áp dụng trong trường hợp sau đây: 1. Yêu cầu bảo vệ quyền nhân thân không gắn với tài sản; 2. Yêu cầu bảo vệ quyền sở hữu, trừ trường hợp Bộ luật này, luật khác có liên quan quy định khác; 3. Tranh chấp về quyền sử dụng đất theo quy định của Luật đất đai; 4. Trường hợp khác do luật quy định
2. [BLDS 2015] Điều 478. Nghĩa vụ bảo đảm quyền sử dụng tài sản cho bên thuê. 1. Bên cho thuê phải bảo đảm quyền sử dụng tài sản ổn định cho bên thuê. 2. Trường hợp có tranh chấp về quyền sở hữu đối với tài sản thuê mà bên thuê không được sử dụng tài sản ổn định thì bên thuê có quyền đơn phương chấm dứt thực hiện hợp đồng và yêu cầu bồi thường thiệt hại
3. [BLDS 2015] Điều 429. Thời hiệu khởi kiện về hợp đồng. Thời hiệu khởi kiện để yêu cầu Tòa án giải quyết tranh chấp hợp đồng là 03 năm, kể từ ngày người có quyền yêu cầu biết hoặc phải biết quyền và lợi ích hợp pháp của mình bị xâm phạm. Chương XVI MỘT SỐ HỢP ĐỒNG THÔNG DỤNG Mục 1 HỢP ĐỒNG MUA BÁN TÀI SẢN
4. [BLDS 2015] Điều 336. Phạm vi bảo lãnh. 1. Bên bảo lãnh có thể cam kết bảo lãnh một phần hoặc toàn bộ nghĩa vụ cho bên được bảo lãnh. 2. Nghĩa vụ bảo lãnh bao gồm cả tiền lãi trên nợ gốc, tiền phạt, tiền bồi thường thiệt hại, lãi trên số tiền chậm trả, trừ trường hợp có thoả thuận khác. 3. Các bên có thể thỏa thuận sử dụng biện pháp bảo đảm bằng tài sản để bảo đảm thực hiện nghĩa vụ bảo lãnh. 4. Trường hợp nghĩa vụ được bảo lãnh là nghĩa vụ phát sinh trong tương lai thì phạm vi bảo lãnh không bao gồm nghĩa vụ phát sinh sau khi người bảo lãnh chết hoặc pháp nhân bảo lãnh chấm dứt tồn tại
5. [BLDS 2015] Điều 321. Quyền của bên thế chấp. 1. Khai thác công dụng, hưởng hoa lợi, lợi tức từ tài sản thế chấp, trừ trường hợp hoa lợi, lợi tức cũng là tài sản thế chấp theo thoả thuận. 2. Đầu tư để làm tăng giá trị của tài sản thế chấp. 3. Nhận lại tài sản thế chấp do người thứ ba giữ và giấy tờ liên quan đến tài sản thế chấp do bên nhận thế chấp giữ khi nghĩa vụ được bảo đảm bằng thế chấp chấm dứt hoặc được thay thế bằng biện pháp bảo đảm khác. 4. Được bán, thay thế, trao đổi tài sản thế chấp, nếu tài sản đó là hàng hoá luân chuyển trong quá trình sản xuất, kinh doanh. Trong trường hợp này, quyền yêu cầu bên mua thanh toán tiền, số tiền thu được, tài sản hình thành từ số tiền thu được, tài sản được thay thế h
Please suggest hypotheses to support why the outcome of the case might be the court rejects all of the plaintiff's claims.
```
**Response**
```
Để phân tích và đưa ra giả thuyết cho rằng Tòa án có thể bác toàn bộ yêu cầu của nguyên đơn, tôi sẽ dựa trên các thông tin và quy định được cung cấp. Dựa trên các yếu tố sau:

1. **Thời hiệu khởi kiện**: Theo Điều 155 BLDS 2015, yêu cầu bảo vệ quyền nhân thân không gắn với tài sản không áp dụng thời hiệu khởi kiện. Tuy nhiên, yêu cầu về việc đòi nợ và bảo lãnh tài sản thế chấp có thể bị giới hạn bởi thời hiệu khởi kiện 3 năm kể từ ngày người có quyền yêu cầu biết hoặc phải biết quyền và lợi ích hợp pháp của mình bị xâm phạm.

2. **Quyền bảo lãnh**: Theo Điều 336 BLDS 2015, phạm vi bảo lãnh không bao gồm nghĩa vụ phát sinh sau khi bên bảo lãnh chết hoặc pháp nhân bảo lãnh chấm dứt tồn tại. Điều này có thể gây khó khăn cho việc đòi nợ từ Công ty K và ông Lam Wing C vì họ có thể đã mất khả năng bảo lãnh.

3. **Quyền của bên thế chấp**: Theo Điều 321 BLDS 2015, bên thế chấp có quyền khai thác tài sản thế chấp, đầu tư để tăng giá trị tài sản thế chấp, nhưng không có quyền bán, thay thế hoặc trao đổi tài sản thế chấp trừ khi nó là hàng hóa luân chuyển trong quá trình sản xuất kinh doanh.

4. **Vi phạm nghĩa vụ**: Theo thông tin cung cấp, Công ty H đã vi phạm nghĩa vụ trả nợ gốc và lãi vay theo thư tín dụng. Tuy nhiên, việc đòi nợ từ Công ty K và ông Lam Wing C có thể gặp khó khăn vì họ đã không thực hiện nghĩa vụ bảo lãnh.

5. **Trách nhiệm của Công ty K và ông Lam Wing C**: Theo Điều 351 BLDS 2015, khi Công ty H vi phạm nghĩa vụ trả nợ, Công ty K và ông Lam Wing C có trách nhiệm hỗ trợ và thực hiện các công việc cần thiết để tạo điều kiện cho việc xử lý tài sản thế chấp. Tuy nhiên, họ đã không hợp tác và thậm chí chuyển nhượng tài sản thế chấp trái phép.

Giả thuyết: 
**Yêu cầu của nguyên đơn không được chấp nhận (toàn bộ)**

Giải thích: 
- Thời hiệu khởi kiện có thể đã hết, đặc biệt là khi yêu cầu đòi nợ từ Công ty K và ông Lam Wing C.
- Công ty K và ông Lam Wing C đã không thực hiện nghĩa vụ bảo lãnh và hỗ trợ xử lý tài sản thế chấp.
- Việc đòi nợ từ Công ty K và ông Lam Wing C gặp khó khăn do họ đã mất khả năng bảo lãnh và không hợp tác.
- Các tài sản thế chấp chỉ có
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