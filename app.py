import streamlit as st
# 设置页面标题和配置
st.set_page_config(
    page_title="以海尔公司为例进行数据治理分析",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 自定义CSS样式
st.markdown("""
<style>
    /* 主色调 - 海尔蓝 */
    :root {
        --haier-blue: #0066CC;
        --haier-light-blue: #E6F2FF;
        --haier-dark-blue: #004C99;
        --haier-gradient: linear-gradient(135deg, var(--haier-blue), var(--haier-dark-blue));
        --haier-gradient-light: linear-gradient(135deg, var(--haier-light-blue), white);
        --shadow-sm: 0 1px 3px rgba(0,0,0,0.12);
        --shadow-md: 0 4px 6px rgba(0,0,0,0.1);
        --shadow-lg: 0 10px 15px rgba(0,0,0,0.1);
        --haier-gradient-card: linear-gradient(135deg, rgba(0,102,204,0.1), rgba(0,76,153,0.1));
        --haier-gradient-header: linear-gradient(135deg, rgba(0,102,204,0.8), rgba(0,76,153,0.8));
    }
    
    /* 全局样式 */
    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        color: #333;
        background: var(--haier-gradient-light);
        background-attachment: fixed;
    }

    .main {
        background-color: rgba(255,255,255,0.9);
        padding: 2rem;
        border-radius: 12px;
        box-shadow: var(--shadow-sm);
        margin: 1rem auto;
        max-width: 1200px;
    }
    
    /* 标题样式 */
    h1 {
        color: var(--haier-blue);
        border-bottom: 2px solid var(--haier-blue);
        padding-bottom: 0.8rem;
        margin-bottom: 1.5rem;
        font-weight: 600;
    }
    
    h2, h3 {
        color: var(--haier-blue);
        margin-top: 1.5rem;
        margin-bottom: 1rem;
        font-weight: 500;
    }
    
    /* 侧边栏样式 */
    .sidebar .sidebar-content {
        background: var(--haier-gradient) !important;
        color: white !important;
    }
    
    .sidebar .stRadio > div > label {
        color: white !important;
        font-weight: 500;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        margin: 0.2rem 0;
        transition: all 0.3s ease;
    }
    
    .sidebar .stRadio > div > label:hover {
        background: rgba(255,255,255,0.2) !important;
    }
    
    .sidebar .stRadio > div > label[data-baseweb="radio"] {
        background: rgba(255,255,255,0.1) !important;
    }
    
    /* 卡片样式 */
    .stContainer, .stExpander > div {
        border-radius: 12px;
        border: none;
        padding: 1.8rem;
        margin-bottom: 1.5rem;
        background: white;
        box-shadow: var(--shadow-md);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        position: relative;
        overflow: hidden;
        background: linear-gradient(to right, white 96%, var(--haier-blue) 4%);
    }
    
    .stContainer::before, .stExpander > div::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 4px;
        height: 100%;
        background: var(--haier-gradient);
        box-shadow: 2px 0 5px rgba(0,102,204,0.3);
    }
    
    .stContainer:hover, .stExpander > div:hover {
        transform: translateY(-2px);
        box-shadow: var(--shadow-lg);
    }
    
    /* 按钮样式 */
    .stButton>button {
        background: var(--haier-gradient) !important;
        color: white !important;
        border-radius: 8px;
        padding: 0.5rem 1.5rem;
        font-weight: 500;
        border: none !important;
        box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }
    
    /* 进度条样式 */
    .stProgress>div>div>div {
        background: var(--haier-gradient) !important;
    }
    
    /* 表格样式 */
    table {
        border-collapse: collapse;
        width: 100%;
        margin: 1rem 0;
        border-radius: 8px;
        overflow: hidden;
        box-shadow: var(--shadow-sm);
    }
    
    th, td {
        padding: 0.75rem;
        text-align: left;
        border-bottom: 1px solid #eee;
    }
    
    th {
        background-color: var(--haier-light-blue);
        color: var(--haier-blue);
        font-weight: 600;
        position: relative;
    }
    
    th::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 2px;
        background: var(--haier-gradient);
    }
    
    tr:hover {
        background-color: rgba(0,102,204,0.05);
    }
    
    /* 图片样式 */
    .stImage > img {
        border-radius: 8px;
        box-shadow: var(--shadow-md);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        border: 1px solid rgba(0,0,0,0.05);
    }
    
    .stImage > img:hover {
        transform: scale(1.02);
        box-shadow: var(--shadow-lg);
    }
    
    /* 链接样式 */
    a {
        color: var(--haier-blue);
        text-decoration: none;
        transition: all 0.3s ease;
        font-weight: 500;
        position: relative;
    }
    
    a:hover {
        color: var(--haier-dark-blue);
    }
    
    a::after {
        content: '';
        position: absolute;
        bottom: -2px;
        left: 0;
        width: 0;
        height: 2px;
        background: var(--haier-gradient);
        transition: width 0.3s ease;
    }
    
    a:hover::after {
        width: 100%;
    }
    
    /* 分隔线样式 */
    .divider {
        height: 2px;
        background: linear-gradient(to right, transparent, var(--haier-blue), transparent);
        margin: 2.5rem 0;
        position: relative;
    }
    
    .divider::after {
        content: '';
        position: absolute;
        bottom: -5px;
        left: 50%;
        transform: translateX(-50%);
        width: 30%;
        height: 1px;
        background: rgba(0,102,204,0.3);
    }
    
    /* 图标装饰 */
    .icon-decorator {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 40px;
        height: 40px;
        border-radius: 50%;
        background: var(--haier-gradient);
        color: white;
        margin-right: 10px;
        box-shadow: var(--shadow-sm);
        transition: all 0.3s ease;
    }
    
    .icon-decorator:hover {
        transform: scale(1.1);
        box-shadow: 0 4px 8px rgba(0,102,204,0.3);
    }
    
    /* 新增动画效果 */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .stContainer, .stExpander > div {
        animation: fadeIn 0.5s ease-out;
    }
</style>
""", unsafe_allow_html=True)

# 页面主标题
st.title("以海尔公司为例进行数据治理分析")

# 侧边栏菜单
st.sidebar.title("目录")
menu = st.sidebar.radio(
    "",
    [ "作业流程", "任务分工", "公司介绍","数据治理", "总结"]
)

# 主要内容区域

if menu == "作业流程":
    st.title("📝 作业流程")
    
    steps = [
        {"title": "1. 查找资料确定选题", "content": "小组通过网络搜索、查阅文献，收集数据治理及海尔COSMOPlat平台信息。经讨论后，确定'以海尔公司为例进行数据治理分析'为作业选题。"},
        {"title": "2. 讨论作业大致框架", "content": "列出作业涉及方面，如平台介绍、数据治理功能、海尔发展与指标变化等，确定作业框架包括主题介绍、平台概述、数据治理应用、案例分析、技术实现、总结等。"},
        {"title": "3. 选择集成工具", "content": "调研Python相关库和工具，了解创建交互式页面及整合资料数据的方法。最终选择使用Python的Streamlit搭建交互式页面，便于资料整合展示。"},
        {"title": "4. 成员分工", "content": "将任务细分并确定小组成员的分工。"},
        {"title": "5. 收集资料", "content": "深入收集海尔集团相关资料，涵盖海尔集团股权结构、组织架构、发展历程、海尔年报、海尔生态等重点内容。"},
        {"title": "6. 建设集成网页", "content": "依据作业框架和资料，使用Python搭建交互式页面，设计合理布局。将资料数据整合到页面，以图表、文字等形式展示海尔集团数据治理情况和应用效果。"},
        {"title": "7. 撰写报告", "content": "按作业框架撰写报告初稿，确保内容完整、逻辑清晰。之后审阅修改初稿，补充遗漏内容，完善表达和逻辑。最终多次修改后形成最终报告。"}
    ]
    
    for step in steps:
        with st.expander(step["title"]):
            st.write(step["content"])
    
    st.progress(100, text="作业完成进度")

elif menu == "任务分工":
    st.title("👥 任务分工")
    
    # 创建任务分工卡片数据
    tasks = [
        {"职能": "数据收集", "任务": "搜集海尔案例、DCMM数据治理方面的标准文件", "人员": "段雨彤", "icon": "📚"},
        {"职能": "可视化", "任务": "绘制组织框架图、制度流程图等", "人员": "朱婧涵", "icon": "📊"},
        {"职能": "网页开发", "任务": "Python集成网页开发", "人员": "杜锦江、朱欣悦", "icon": "💻"},
        {"职能": "报告撰写", "任务": "撰写小组作业报告", "人员": "藏仁博、邹园园、黄择橙", "icon": "📝"}
    ]
    
    cols = st.columns(2)
    for i, task in enumerate(tasks):
        with cols[i % 2]:
            with st.container(border=True):
                st.markdown(f"### {task['icon']} {task['职能']}")
                st.markdown(f"**任务**: {task['任务']}")
                st.markdown(f"**负责人**: {task['人员']}")
                st.progress(100 if i % 2 == 0 else 75, text="完成进度")

elif  menu == "公司介绍":
    st.header("公司介绍")
    st.image("海尔.png", caption="海尔集团总部", width=800)
    st.header("公司组织结构")
    st.image("2024组织架构.png", caption="组织架构", width=800)
    st.write("""ESG委员会说明https://www.ibm.com/cn-zh/topics/environmental-social-and-governance""")
    st.header("公司股权结构")
    st.image("2024股权结构.png", caption="股权结构", width=800)
    st.write("""
    ## 公司概况
    海尔集团成立于1984年，总部位于山东省青岛市，是中国领先的物联网生态企业。从一家濒临破产的集体小厂发展至今，
    已成为全球家电行业领军企业之一，业务涵盖智慧家庭、工业互联网、生物医疗等多个领域。
    
    ## 核心业务
    - 智慧住居：提供智能家电及全屋智能解决方案，旗下品牌包括海尔、卡萨帝（Casarte）、Leader等，并推出全球首个智慧家庭场景品牌"三翼鸟"。
    - 产业互联网：通过卡奥斯（COSMOPlat）工业互联网平台，赋能制造业数字化转型。
    - 大健康：涉及生物医疗、健康管理等领域，如盈康一生品牌。
    
    ## 全球化布局
    - 全球拥有29个制造基地、8个综合研发中心和19个海外贸易公司，员工超6万人。
    - 国际化战略包括收购通用电气家电业务（GE Appliances）、新西兰Fisher & Paykel、意大利Candy等国际品牌。
    
    ## 品牌价值与市场地位
    - 连续13年（截至2021年）位居欧睿国际（Euromonitor）全球家电品牌第一。
    - 2023年，海尔连续5年作为全球唯一物联网生态品牌入选BrandZ最具价值全球品牌100强。
    - 2024年，海尔智家（海尔集团旗下上市公司）营收达2859.81亿元，归母净利润同比增长12.92%。
    
    ## 创新与管理
    - "人单合一"模式：强调员工与用户直接连接，被哈佛商学院等收录为经典案例。
    - 全球拥有6家"灯塔工厂"（世界经济论坛认证），代表全球智能制造最高水平。
    
    ## 近期发展
    - 明确聚焦智慧住居、产业互联网和大健康三大赛道。
    - 通过收购汽车之家布局汽车后市场服务。
    - 海尔智家2024年资产负债率降至58.20%。
    
    本案例将深入分析海尔在数据治理方面的发展。
    """)


elif menu == "数据治理":
    st.title("数据治理")
    sub_menu = st.sidebar.radio(
        "数据治理子菜单",
        ["整体发展历程", "2012年以前", "2012-2014年", "2015-2018年", "2019-2021年", "2022年至今"]
    )
    
    if sub_menu == "整体发展历程":
        st.header("整体发展历程")
        st.write("""
        海尔在数据治理方面的整体发展历程:
        """)
        st.image("timeline.png", caption="海尔数据治理发展历程", width=800)

        



    elif sub_menu == "2012年以前":
        st.header("2012年以前")
        st.image("2012以前.png", caption="张瑞敏砸冰箱",width=800)
        with st.expander("数据治理组织"):
            st.markdown("""
            **组织架构分散**: 在2012年以前，海尔的数据治理工作主要由各个业务部门自行负责，缺乏专门的数据治理组织或团队。例如，生产数据由生产部门管理，销售数据由销售部门管理，各部门之间缺乏统一协调和整合机制。
            
            **缺乏跨部门协作**: 由于缺乏统一的组织架构，各部门之间的数据治理工作相对独立，跨部门协作较少。数据的共享和流通受到限制，导致数据孤岛现象严重，难以形成全局性的数据管理和利用体系。
            
            **专业人才不足**: 当时海尔在数据治理领域缺乏专业的数据治理人才，数据管理主要由业务人员兼职负责，缺乏专业的数据分析师、数据架构师等专业人员。这使得数据治理工作在技术层面和专业性方面存在不足，难以有效推进数据治理的深度和广度。
            """)
            
        with st.expander("数据制度建设"):
            st.markdown("""
            **缺乏统一的数据标准**: 2012年以前，海尔尚未建立统一的数据标准体系。不同部门根据自身业务需求自行定义数据格式、数据编码规则等，导致数据在跨部门共享和整合时出现数据不一致、数据冲突等问题。
            
            **数据质量管理制度不完善**: 数据质量管理是数据治理的重要环节，但在2012年以前，海尔在这方面的制度建设较为薄弱。缺乏明确的数据质量评估指标和监控机制，数据的准确性、完整性、及时性无法得到有效保障。
            
            **数据安全与合规制度缺失**: 随着数据重要性的提升，数据安全和合规性成为关键问题。然而，2012年以前海尔在数据安全和合规方面的制度建设相对滞后。缺乏明确的数据安全策略、数据访问控制制度以及数据备份和恢复机制。
            """)
            
        with st.expander("数据治理沟通"):
            st.markdown("""
            **沟通渠道不畅**: 由于缺乏统一的数据治理组织和平台，各部门之间的数据治理沟通主要依靠传统的会议、邮件等方式，沟通效率较低。
            
            **缺乏统一的沟通平台**: 没有专门的数据治理沟通平台或工具，各部门在数据治理过程中难以实时共享信息、协同工作。
            
            **跨部门沟通成本高**: 由于各部门数据治理工作相对独立，跨部门沟通需要协调多个部门的利益和需求，沟通成本较高。
            """)
        
        st.write("""https://www.haier.com/press-events/news/20211108_172896.shtml""")

    elif sub_menu == "2012-2014年":
        st.header("2012-2014年")
        st.image("倒三角.png",width=800)
        with st.expander("数据治理组织"):
            st.markdown("""
            **明确职责与管理层重视**: 2012年海尔提出网络化战略，开启了数字化转型工作，这使得数据治理在企业战略层面的重要性得到凸显。管理层开始重视数据治理工作，明确各部门在数据治理中的职责，为数据治理工作的开展提供了组织保障和资源支持。例如，企业可能会设立专门的数字化转型小组或数据治理委员会，由高层领导牵头，统筹协调各部门的数据治理工作。
            
            **管理模式与组织结构变革**: 从管理模式变革角度，海尔探索将传统管理模式变为一种适应互联网时代的人单合一双赢模式。这种模式的转变使得数据治理不再是单纯的后台支持工作，而是与员工创造用户价值紧密相连，激励员工积极参与数据治理工作，以更好地满足用户需求。从组织结构角度，海尔将传统的正三角组织结构创新为倒三角组织结构，让接触用户的员工在第一线，领导从原来的指挥者变成资源提供者。这种组织结构的变革有助于打破部门壁垒，促进数据在企业内部的流通和共享，提高数据治理的效率和效果。
            
            **互联工厂的推动作用**: 2012年，海尔建成了第一家互联工厂——沈阳海尔电冰箱有限公司，开启了从大规模生产向大规模定制转型的探索。互联工厂的建设需要对生产过程中的数据进行深度挖掘和分析，以实现生产的智能化和个性化定制。这促使海尔在数据治理组织方面进行相应的调整和优化，建立跨部门的数据协同机制，确保生产、销售、物流等环节的数据能够实时共享和交互，为互联工厂的高效运行提供支持。
            """)
            st.write("""互联工厂：https://baike.baidu.com/item/%E4%BA%92%E8%81%94%E5%B7%A5%E5%8E%82/50886715""")
        
        st.image("U+.png", width=800)
        with st.expander("数据制度建设"):
            st.markdown("""
            **搭建“网器平台”与U+智慧生活操作系统**: 海尔搭建了“网器平台”，并从U-home转为U+，发布了U+智慧生活操作系统。这一举措不仅拓展了海尔产品的智能化功能，也为数据治理提供了制度覆盖范围。U+智慧生活操作系统通过连接各种智能家电设备，收集和分析用户在使用过程中的数据，为用户提供更加个性化、智能化的服务。同时，海尔也建立了一套与之配套的数据管理制度，规范数据的采集、存储、处理和使用流程，确保数据的安全和合规性，为数据的深度挖掘和价值创造提供制度保障。
            
            **数据标准与规范的建立**: 在数据制度建设方面，海尔开始着手建立统一的数据标准和规范。这包括数据的格式、编码规则、数据质量要求等方面的标准，以便于不同部门、不同系统之间的数据能够进行有效的整合和共享。例如，对于客户数据，海尔可能会制定统一的客户信息编码规则，确保在企业内部各个业务环节中对同一客户的描述是一致的，从而提高数据的一致性和准确性，为数据分析和决策提供可靠的数据基础。
            
            **数据安全与合规制度完善**: 随着数据重要性的提升，海尔在数据安全与合规方面也加强了制度建设。制定了明确的数据安全策略，包括数据访问控制、数据加密、数据备份和恢复等措施，防止数据泄露、篡改等安全事件的发生。同时，海尔也注重数据合规管理，确保数据的收集、使用和共享符合相关法律法规的要求，避免因数据问题引发的法律风险。
            """)

        
        st.image("2014员工.png", width=800)
        with st.expander("数据治理沟通"):
            st.markdown("""
            **内部沟通机制的优化**: 在数据治理沟通方面，海尔通过优化内部沟通机制，加强了各部门之间的数据治理沟通与协作。建立了定期的数据治理沟通会议制度，让各部门能够及时分享数据治理的进展、经验和问题，共同探讨解决方案。同时，利用企业内部的信息化平台，如企业内部网站、即时通讯工具等，搭建了数据治理的在线沟通渠道，方便各部门之间随时交流数据治理相关的信息，提高沟通效率。
            
            **数据治理培训与宣贯**: 为了提高员工对数据治理的认识和理解，海尔开展了数据治理培训与宣贯活动。通过组织内部培训课程、研讨会等形式，向员工普及数据治理的基本概念、方法和工具，提高员工的数据治理意识和技能水平。同时，海尔也通过内部宣传渠道，如企业内部刊物、宣传栏等，加强对数据治理工作的宣传和推广，营造良好的数据治理文化氛围，让数据治理的理念深入人心。
            
            **与外部合作与交流**: 海尔还开展与外部机构的数据治理合作与交流。与高校、科研机构合作开展数据治理相关的研究项目，借助外部的专业力量提升自身数据治理水平。同时，海尔也积极参与行业内的数据治理交流活动，分享自身在数据治理方面的经验和实践成果，学习借鉴其他企业的先进经验，不断优化自身的数据治理沟通机制，提升数据治理的综合能力。
            """)

            
        with st.expander("具体数据指标"):
            st.markdown("""
            **生产效率提升**: 以海尔胶州空调互联工厂为例，通过采用大数据、数字孪生等技术，该工厂将设计周期缩短了49%，订单交付时间缩短了19%，海外市场故障率降低了28%。
            
            **质量性能提升**: 海尔青岛洗衣机互联工厂通过5.5G、先进算法等技术，实现了产品成本优化32%，效率提高36%，服务抱怨率降低85%。
            
            **数据平台的覆盖范围**: 海尔的数据平台覆盖了集团及各领域运营分析决策人员，形成了从数据战略到数据决策与增值、到数据中台、到数据治理的闭环。
            """)
        st.write("""2014年报：https://file.finance.sina.com.cn/211.154.219.97:9494/MRGG/CNSESH_STOCK/2015/2015-3/2015-03-31/1683566.PDF""")



    elif sub_menu == "2015-2018年":
        st.header("2015-2018年")
        
        with st.expander("数据治理组织"):
            st.markdown("""
            **DTS（数据服务部）的成立与职责**: 2015年左右，海尔成立了DTS（数据服务部），专门负责数据治理相关工作。DTS部门围绕小微企业策略和人单合一策略搭建数据平台，为海尔的数字化转型提供数据支持。DTS部门的成立标志着海尔数据治理组织的进一步完善，职责更加明确，能够更好地推动数据治理工作。
            
            **明确的考核机制**: DTS部门内部建立了明确的考核机制，通过设定关键绩效指标（KPI）来衡量数据治理工作的成效。例如，考核数据治理对业务的赋能效果、数据资产的增值情况、数据平台的稳定性和可用性等。这种考核机制不仅激励了数据治理团队积极工作，还确保了数据治理工作的目标与企业整体战略保持一致。
            """)

        st.write("""采访：https://www.shangyexinzhi.com/article/327480.html""")    
        with st.expander("数据制度建设"):
            st.markdown("""
            **数据平台的搭建与完善**: 海尔在这一时期不断完善数据平台，整合企业内外部数据资源，建立统一的数据标准和规范。数据平台的搭建使得数据的采集、存储、处理和分析更加高效和规范，为数据的深度挖掘和价值创造提供了基础。
            
            **数据安全与合规制度的加强**: 随着数据重要性的提升，海尔加强了数据安全与合规制度。制定了详细的数据安全策略，包括数据访问控制、数据加密、数据备份和恢复等措施，确保数据的安全性和完整性。同时，海尔也注重数据合规管理，确保数据的收集、使用和共享符合相关法律法规的要求。
            """)
        st.write("""卡奥斯平台：https://www.cosmoplat.com/platform""")

            
        with st.expander("数据治理沟通"):
            st.markdown("""
            **卡奥斯COSMOPlat平台的创建**: 2017年，海尔创建了卡奥斯COSMOPlat平台，这是一个以大规模定制为核心、实现整个价值链端到端连接的工业互联网平台。该平台的创建不仅提升了海尔内部的数据治理沟通效率，还促进了海尔与上下游合作伙伴之间的数据共享和协同，推动了整个产业链的数字化转型。
            
            **灯塔工厂的建设与推广**: 2018年，海尔中央空调互联工厂入选全球首批"灯塔工厂"。此后，海尔陆续建设了多个灯塔工厂，如2020年的沈阳海尔冰箱互联工厂、2021年的青岛啤酒互联工厂和天津海尔洗衣机互联工厂等。这些灯塔工厂通过部署先进的数字化技术和数据分析工具，实现了生产效率的提升、成本的降低和质量的提高。同时，海尔还将灯塔工厂的经验和能力向全球150多家工厂推广，推动了整个行业的数据治理和数字化转型。
            """)
        st.write("""灯塔工厂发展：https://www.cosmoplat.com/lighthouseFactory/lighthouse""")
        import plotly.graph_objects as go
    
    # 数据
        years = [2018,2020, 2021, 2022, 2023, 2024]
        values = [1,2, 4, 6, 10, 11]
        custom_texts = ['海尔中央空调互联工厂入选全球首批"灯塔工厂"', '沈阳海尔冰箱互联工厂', 
        '青岛啤酒互联工厂、天津海尔洗衣机互联工厂', '郑州海尔热水器互联工厂、青岛海尔冰箱互联工厂', 
        '天津海尔洗衣机互联工厂、卡奥斯合肥智控互联工厂、海尔青岛洗衣机互联工厂、海尔合肥空调互联工厂',
        '海尔胶州空调互联工厂']

    # 创建折线图
        fig = go.Figure(data=[
            go.Scatter(
                x=years,
                y=values,
                mode='lines+markers',
                hovertemplate='<b>年份</b>: %{x}<br><b>数值</b>: %{y}<br><b>说明</b>: %{text}<extra></extra>',
                text=custom_texts,
                line=dict(color='#1f77b4', width=3, shape='spline'),
                marker=dict(
                size=12,
                color='#1f77b4',
                line=dict(color='white', width=2),
                symbol='circle'
                )
        )
        ])

    # 设置布局
        fig.update_layout(
            title=dict(
                text='海尔互联工厂发展历程',
                font=dict(size=28, family='Arial', color='#2c3e50'),
                x=0.5,
                y=0.95
            ),
            xaxis=dict(
                title=dict(text='年份', font=dict(size=16, family='Arial', color='#2c3e50')),
                tickformat='d',
                tickmode='linear',
                dtick=1,
                showgrid=True,
                gridcolor='rgba(189, 195, 199, 0.2)',
                tickfont=dict(size=14, family='Arial')
            ),
            yaxis=dict(
                title=dict(text='互联工厂数量', font=dict(size=16, family='Arial', color='#2c3e50')),
                showgrid=True,
                gridcolor='rgba(189, 195, 199, 0.2)',
                tickfont=dict(size=14, family='Arial')
            ),
            showlegend=False,
            plot_bgcolor='white',
            paper_bgcolor='white',
            margin=dict(l=80, r=40, t=100, b=80),
            hoverlabel=dict(bgcolor='white', font_size=14, font_family='Arial')
        )

    # 在Streamlit中显示图表
        st.plotly_chart(fig, use_container_width=True)
            
        with st.expander("具体指标数据"):
            st.markdown("""
            **生产效率提升**: 海尔在2015-2018年期间持续推进智能制造升级，通过引入先进的自动化设备和信息化系统，生产效率得到了显著提升。例如，海尔的冰箱生产线在2016年引入了自动化装配机器人，使得生产效率提高了30%。此外，海尔还通过优化生产流程和供应链管理，进一步降低了生产成本
            
            **质量性能提升**: 海尔在质量管理方面一直走在行业前列。2015-2018年期间，海尔通过引入大数据分析和人工智能技术，进一步提升了产品质量。例如，海尔在2017年引入了人工智能自检系统，使得产品合格率提高了38%，售后成本降低了70%
            
            **数据平台的覆盖范围**: 海尔的数据平台已贯穿企业内部的多个关键环节，从源头的数据采集、整合，到中层的数据分析与处理，再到顶层的决策支持，构建起一个完整且高效的数据生态系统。这一平台不仅服务于集团总部的战略规划与决策，还深入到各业务板块、生产工厂以及销售终端等各个层面，为不同部门和岗位的人员提供精准、实时的数据支持，助力企业实现精细化管理和科学决策。
            """)

    elif sub_menu == "2019-2021年":
        st.header("2019-2021年")

        st.image("三大赛道.png",caption="布局三大赛道", width=800)
        st.write("""https://www.haier.com/haier-ecosystem/?spm=net.home_pc.hg2024_home_part01_20241122.2""")
        with st.expander("数据治理组织"):
            st.markdown("""
            **数据平台与数据管理委员会的成立**: 2019年，海尔主导籌建了数据平台，并牵头成立了数据管理委员会。数据管理委员会从集团数据治理、数据决策及增值、数据技术交付、数字化风险管控等角度落地推进数据治理工作，同时着眼于未来，进行各类数字化前瞻性技术研究，承接集团数据中台建设及数字化转型推进目标。
            
            **明确的考核机制**: 数据平台部门内部建立了明确的考核机制，通过设定关键绩效指标（KPI）来衡量数据治理工作的成效。例如，考核数据治理对业务的赋能效果、数据资产的增值情况、数据平台的稳定性和可用性等。
            
            **搭建盈康一生平台与海数汇-云探**: 2019年，海尔搭建了盈康一生平台，2020年搭建了企业级大数据资产管理平台——海数汇-云探。这些平台的搭建进一步完善了海尔的数据治理组织架构，提升了数据治理的专业性和效率。
            """)
        
            
        with st.expander("数据制度建设"):
            st.markdown("""
            **制度覆盖范围**: 海尔的数据治理制度覆盖了智慧住居生态、大健康产业生态和数字经济产业生态。在智慧住居生态中，海尔通过智能家电、智慧家庭和智慧生活等业务，为用户提供全场景覆盖的个性化智慧家庭解决方案。在大健康产业生态中，海尔提供生命科学、临床医学和生物科技等数字场景综合解决方案。在数字经济产业生态中，海尔通过卡奥斯COSMOPlat工业互联网平台、海纳云城市治理解决方案、卡泰池汽车场景和海尔新能源等业务，为全球企业和行业提供数字化转型解决方案。
            
            **数据标准与规范**: 海尔建立了统一的数据标准和规范，包括数据格式、编码规则、质量要求等，提高数据的一致性和准确性。同时，海尔还制定了详细的数据安全策略，加强数据访问控制、加密、备份和恢复等措施，确保数据的安全性和完整性。
            """)
            
        with st.expander("数据治理沟通"):
            st.markdown("""
            **数据平台的推广与应用**: 海尔通过数据平台，将数据治理的理念和方法推广到集团的各个业务领域和生态合作伙伴中。数据平台不仅为内部员工提供了数据查询、分析和决策支持服务，还为外部合作伙伴提供了数据共享和协同的平台，促进了数据的流通和价值创造。
            
            **数据治理培训与宣贯**: 海尔开展数据治理培训与宣贯活动，提高员工对数据治理的认识和理解。通过组织内部培训课程、研讨会等形式，向员工普及数据治理的基本概念、方法和工具，营造良好的数据治理文化氛围。
            
            **数字化转型案例研究与分享**: 海尔作为数字化转型的典型案例，积极参与行业内的交流活动，分享自身在数据治理和数字化转型方面的经验和成果。通过案例研究和分享，海尔不仅提升了自身的品牌影响力，还为其他企业提供了有益的借鉴和参考。
            """)
            
        with st.expander("具体指标数据"):
            st.markdown("""
            **数据平台的用户覆盖范围**: 海数汇-云探平台覆盖了海尔集团及各生态合作伙伴的大量用户，为用户提供数据查询、分析和决策支持服务。
            
            **数据治理对业务的赋能效果**: 通过数据治理，海尔在多个业务领域实现了显著的业务增长和效率提升。例如，在智慧住居生态中，海尔的智能家电产品销量持续增长，用户满意度不断提高；在大健康产业生态中，海尔的生命科学、临床医学和生物科技等业务取得了显著的市场突破。
            
            **数据安全与合规**: 海尔通过了ISO27001、ISO27701等数据安全认证，确保数据的安全性和合规性。
            """)
        st.image("IEC 27018权威认证.png", caption="海尔数据治理发展历程", width=800)   
        st.write("""第五章典型案例：海尔集团https://www.vzkoo.com/document/20241204b0b2b7311699bd5ee210f080.html """)

    elif sub_menu == "2022年至今":
        st.header("2022年至今")
        
        with st.expander("数据治理组织"):
            st.markdown("""
            **数字化平台的深化与拓展**: 海尔在2022年进一步深化了数字化平台的建设，通过全流程、全要素、全节点上平台，打造了以端到端流程为基础、数据为核心、价值创造为导向的数字化运营体系。这不仅提升了内部运营效率，还推动了生态圈的共同发展。例如，海尔智家通过数字化业务平台、数字化制造平台、数字化研发平台等，实现了全流程可控可视、挖掘降费提效空间。
            
            **组织架构的优化**: 海尔智家通过数字化转型，优化了组织架构，提升了组织效率。例如，通过数字化制造平台，实现了采购、供应链、制造、物流等环节的打通，使时序下线准确率达92%、支持订单准时交付率达95%。同时，数字化研发平台通过打通设计-研发-采购环节，提升了爆款率，上半年海尔智家产品效率提升23%。
            """)
        
        with st.expander("数据制度建设"):
            st.markdown("""
            **制度覆盖范围的拓展**: 海尔的数据治理制度覆盖了智慧住居生态、大健康产业生态和数字经济产业生态。在数字经济产业生态中，海尔通过卡奥斯COSMOPlat工业互联网平台、海纳云城市治理解决方案、卡泰池汽车场景和海尔新能源等业务，为全球企业和行业提供数字化转型解决方案。
            
            **数据标准与规范的完善**: 海尔建立了统一的数据标准和规范，包括数据格式、编码规则、质量要求等，提高数据的一致性和准确性。例如，海尔智家通过统一数据平台，实现了全球研发中心协作，研发设计成本降低20亿元，验证一次通过率超90%。
            """)
        st.image("品牌生态.png", caption="品牌生态", width=800)

        
        with st.expander("数据治理沟通"):
            st.markdown("""
            **数字化平台的推广与应用**: 海尔通过数据平台，将数据治理的理念和方法推广到集团的各个业务领域和生态合作伙伴中。例如，海尔智家通过用户体验云平台，实现了对用户全旅程体验的实时感知，并通过有效的反馈机制推动业务竞争力提升，用户抱怨量下降24%。
            
            **数据治理培训与宣贯**: 海尔开展数据治理培训与宣贯活动，提高员工对数据治理的认识和理解。例如，海尔智家通过数字化分销系统、用户经营辅助分析系统等工具，提升经销商在分销管理、进销存管理和门店运营的效率，数字化零售额同比增长了22%。
            
            **数字化转型案例研究与分享**: 海尔作为数字化转型的典型案例，积极参与行业内的交流活动，分享自身在数据治理和数字化转型方面的经验和成果。例如，海尔智家通过集成式研发平台，实现了企划、开发、采购全流程高效协同，国内市场单型号产出效率提升19%。
            """)
        
        
        with st.expander("具体数据指标"):
            st.markdown("""
            **财务表现**: 海尔智家在2022年实现了全球营业收入2,435.14亿元，增长7.2%，归母净利润达到147.11亿元，增长12.5%。2024年上半年，海尔智家实现营业收入1356.2亿元，同比增长3.0%；归母净利润104.2亿元，同比增长16.3%。
            
            **运营效率提升**: 通过数字化转型，海尔智家的运营效率显著提升。例如，数字化制造平台使时序下线准确率达92%、支持订单准时交付率达95%。数字化研发平台提升了爆款率，产品效率提升23%。
            
            **用户体验改善**: 海尔智家通过用户体验云平台，实现了对用户全旅程体验的实时感知，用户抱怨量下降24%。同时，通过数字化分销系统，数字化零售额同比增长了22%。
            """)
        st.image("5年营业收入.png", caption="五年营业收入", width=800)
        st.image("5年净利润.png", caption="五年净利润", width=800)
        st.write(""""三翼鸟：https://www.sanyiniao.com/about/ppzl/?spm=sanyiniao.about-home_pc.brand_home_part04_20240115.1""")
        st.write("""盈康一生：https://www.haier.com/yingkanglife/?spm=net.haier-ecosystem_pc.hg2020_ecology_plate_03_20231113.2""")
        st.write("""海尔新能源：https://haier-energy.com/about_int.html""")


elif menu == "总结":
    st.title("总结")
    
    st.markdown("""
    在对海尔集团数据治理发展历程的深入研究中，我们看到了一个企业如何通过持续的数字化转型，实现从传统制造企业向智能化、数字化企业的蜕变。这个转变过程既令人振奋，又充满启发。

    从2012年以前的传统管理模式，到如今成为引领全球智能制造的标杆企业，海尔用十余年时间完成了令人瞩目的转型。在这个过程中，我们看到了海尔在数据治理方面的不懈努力：从最初的部门分散管理到建立统一的数据治理体系，从单一的生产数据到全方位的数据资产管理，从简单的数据收集到深度的数据价值挖掘。

    特别令人印象深刻的是，海尔并没有将数据治理仅仅视为一个技术问题，而是将其融入到企业战略和文化中。通过"人单合一"模式的创新，将员工、用户和数据紧密连接；通过建设互联工厂，将数字化理念渗透到生产的每个环节；通过发展三大产业生态，构建起完整的数字化生态系统。

    在这个过程中，海尔取得了显著的成果：
    - 11家灯塔工厂的建设展现了其在智能制造领域的领先地位
    - 卡奥斯工业互联网平台实现了产业链的数字化协同
    - U+智慧生活平台打造了智能家居生态系统
    - 最新财报显示，数字化转型为企业带来了实实在在的效益提升

    然而，更重要的是海尔给我们的启示：数据治理不是一蹴而就的工程，而是需要持续演进的过程；不是简单的技术应用，而是深刻的管理变革；不是孤立的信息系统，而是连接企业内外的生态平台。

    正如海尔的发展历程所展示的，数字化转型是一场既艰巨又充满机遇的征程。它需要企业具有前瞻性的战略眼光、坚定的变革决心，以及持续的创新能力。在这个数字化时代，海尔的经验值得每一个致力于数字化转型的企业借鉴和思考。
    """)
