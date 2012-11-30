
Create TABLE [dbo].[T_Class](
 [F_ID] [uniqueidentifier] NOT NULL CONSTRAINT [DF_T_Class_F_ID]  DEFAULT (newid()),
 [F_ClassName] [nvarchar](256) COLLATE Chinese_PRC_CI_AS NULL CONSTRAINT [DF_F_ClassTest_F_ClassName]  DEFAULT (''),
 [F_ShortName] [nvarchar](50) COLLATE Chinese_PRC_CI_AS NULL,
 [F_ParentID] [uniqueidentifier] NULL CONSTRAINT [DF_T_Class_F_ParentID]  DEFAULT (newid()),
 [F_Depth] [int] NULL CONSTRAINT [DF_F_ClassTest_F_Depth]  DEFAULT ((0)),
 [F_RootID] [int] NULL CONSTRAINT [DF_F_ClassTest_F_RootID]  DEFAULT ((0)),
 [F_Orders] [int] NULL CONSTRAINT [DF_F_ClassTest_F_Orders]  DEFAULT ((0)),
 [F_ParentIDStr] [nvarchar](300) COLLATE Chinese_PRC_CI_AS NULL CONSTRAINT [DF_F_ClassTest_F_ParentIDStr]  DEFAULT (''),
 [F_ParentNameStr] [nvarchar](300) COLLATE Chinese_PRC_CI_AS NULL CONSTRAINT [DF_F_ClassTest_F_ParentNameStr]  DEFAULT (''),
 [F_ReadMe] [nvarchar](250) COLLATE Chinese_PRC_CI_AS NULL CONSTRAINT [DF_F_ClassTest_F_ReadMe]  DEFAULT (''),
 [F_AddTime] [datetime] NULL CONSTRAINT [DF_F_Class_F_AddTime]  DEFAULT (getdate()),
 [F_Type] [nvarchar](50) COLLATE Chinese_PRC_CI_AS NULL,
 [F_MaxPage] [int] NULL CONSTRAINT [DF_T_Class_F_MaxPage]  DEFAULT ((0)),
 [F_No] [nvarchar](50) COLLATE Chinese_PRC_CI_AS NULL,
 [F_isShow] [tinyint] NULL CONSTRAINT [DF_T_Class_F_isShow]  DEFAULT ((0)),
 [F_AutoId] [int] IDENTITY(1,1) NOT NULL,
 CONSTRAINT [PK_T_Class] PRIMARY KEY CLUSTERED
(
 [F_ID] ASC
)WITH (IGNORE_DUP_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]