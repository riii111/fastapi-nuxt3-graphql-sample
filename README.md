# GraphQL memo

## GUI

<http://localhost:30020/graphql>

## GraphQLのフロー

GraphQL、REST併用することを想定しているので、usecaseやmodel、repositoryを経由する。
"Book"に対してQuery/Mutationを行う場合のフロー。

```mermaid
graph TD
    Client[Client] -->|GraphQL Query| Router[GraphQL Router]
    Router -->|Executes| Schema["Federation Schema (Query)"]
    Schema -->|Defines & Resolves| Query[Query]
    Query -->|Resolves| Resolvers[Resolvers]
    Resolvers -->|Uses| Context[GraphQL Context]
    Context -->|Depends on| BookUseCase[Book UseCase]
    BookUseCase -->|Uses| BookRepository[Book Repository]
    BookRepository -->|Accesses| Database[(Database)]
    
    Resolvers -->|Returns| BookViewType[BookViewType]
    BookViewType -->|Defined in| Types[Types]
    Types -->|Uses| PyObjectIdType[PyObjectIdType]
    
    subgraph "GraphQL Layer"
        Router
        Schema
        Query
        Resolvers
        Context
        BookViewType
        Types
        PyObjectIdType
    end
    
    subgraph "Business Logic Layer"
        BookUseCase
    end
    
    subgraph "Data Access Layer"
        BookRepository
    end
    
    subgraph "Models"
        BookView[BookView Model]
        PyObjectId[PyObjectId Model]
    end
    
    BookViewType -.->|Maps to| BookView
    PyObjectIdType -.->|Serializes| PyObjectId
    
    classDef graphql fill:#e6f3ff,stroke:#333,stroke-width:2px,color:#000;
    classDef business fill:#fff2cc,stroke:#333,stroke-width:2px,color:#000;
    classDef data fill:#e6ffee,stroke:#333,stroke-width:2px,color:#000;
    classDef model fill:#ffe6e6,stroke:#333,stroke-width:2px,color:#000;
    
    class Router,Schema,Query,Resolvers,Context,BookViewType,Types,PyObjectIdType graphql;
    class BookUseCase business;
    class BookRepository data;
    class BookView,PyObjectId model;

    linkStyle default fill:none,stroke:#333,stroke-width:2px;
```

## ざっくりメモ

- **クエリ (Query)**<br/>
  データを取得するためのリクエスト<br/>
  クライアントが必要なデータの構造を指定し、その構造に基づいてサーバーからデータが返される

- **ミューテーション (Mutation)**<br/>
  データを変更するためのリクエスト<br/>
  新しいデータの作成、既存データの更新、削除などが含まれる

- **サブスクリプション (Subscription)**<br/>
  特定のイベントが発生した際に、クライアントにリアルタイムで通知を送信する仕組み<br/>
  主にチャットアプリや通知機能で利用される

- **スキーマ (Schema)**<br/>
  GraphQL APIの仕様を定義するもの<br/>
  どのようなデータ型が存在し、それらがどのように関連しているかを示す<br/>
  スキーマは型システムに基づいており、APIの設計を明確にする

- **型 (Type)**<br/>
  GraphQLで使用されるデータ型<br/>
  基本的なスカラー型（String, Int, Float, Boolean, ID）やオブジェクト型などがある

- **リゾルバ (Resolver)**<br/>
  特定のフィールドに対してデータを取得するための関数<br/>
  リゾルバはスキーマで定義されたフィールドに基づいて実行される
