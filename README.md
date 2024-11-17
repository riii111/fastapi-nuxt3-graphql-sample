※RESTとGraphQLを併用できる形で実装。

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
    
    Resolvers -->|Returns| BookType[BookType]
    BookType -->|Defined in| Types[Types]
    Types -->|Uses| PyObjectIdType[PyObjectIdType]
    
    subgraph "GraphQL Layer"
        Router
        Schema
        Query
        Resolvers
        Context
        BookType
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
        Book[Book Model]
        PyObjectId[PyObjectId Model]
    end
    
    BookType -.->|Maps to| BookResponse
    PyObjectIdType -.->|Serializes| PyObjectId
    
    classDef graphql fill:#e6f3ff,stroke:#333,stroke-width:2px,color:#000;
    classDef business fill:#fff2cc,stroke:#333,stroke-width:2px,color:#000;
    classDef data fill:#e6ffee,stroke:#333,stroke-width:2px,color:#000;
    classDef model fill:#ffe6e6,stroke:#333,stroke-width:2px,color:#000;
    
    class Router,Schema,Query,Resolvers,Context,BookType,Types,PyObjectIdType graphql;
    class BookUseCase business;
    class BookRepository data;
    class BookResponse,PyObjectId model;

    linkStyle default fill:none,stroke:#333,stroke-width:2px;
```

## 動作確認例

### books一覧を取得する場合

<img width="1624" alt="image" src="https://github.com/user-attachments/assets/af6b548b-5149-4a97-9c49-8c2b69660ed3">

### 対象のIDのbookを取得する場合

<img width="1624" alt="image" src="https://github.com/user-attachments/assets/15f82b11-168d-44f5-a8d4-7b2a467c6a47">

### 新しいbookを作成する場合

<img width="1624" alt="image" src="https://github.com/user-attachments/assets/b2219d06-bfc6-414f-b9e0-58e6bb9a2825">

### bookを更新する場合

<img width="1624" alt="image" src="https://github.com/user-attachments/assets/042a7a61-4e26-45d1-8f71-88713a61bc5f">

### bookを削除する場合

<img width="1624" alt="image" src="https://github.com/user-attachments/assets/41597ad8-61bd-456e-98d4-8c9463c4b66b">

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
