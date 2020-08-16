# Lecture-02: Variables and Simple Data Types

এই লেকচার এ আমরা পাইথনে কীভাবে বিভিন্ন প্রকার ডেটা ব্যবহার করা যায় তা শিখব ।

## Variables ( চলক )

-   সব সময় বর্তমান মান নিয়ে কাজ করে ।
-   যেকোনো সময় মান পরিবর্তন করা যায় ।
-   চলকের টাইপ উল্লেখ করার দরকার হয়না ।

### Naming and Using Variables

কিছু কিছু নিয়ম আছে যেগুলো চলক ব্যবহারে মেনে চলতে হয়, না অনুসরণ করলে এররর (ভুল) হবে । আবার কিছু কিছু পরামর্শ আছে যা না মানলে এররর হবেনা কিন্তু মেনে চলা উত্তম ।

নিচের নিয়মগুলো মনে রাখবঃ

-   চলকের নাম শুধুমাত্র Letters, numbers, and underscores দিয়ে গঠন করা যাবে । তবে Numbers দিয়ে শুরু করা যাবে না । উদাহরনঃ `message_1` (সঠিক), কিন্তু `1_message` (ভুল) ।
-   চলকের নামের মাঝে Spaces (ফাকা স্থান) রাখা যাবে না । তবে শব্দগুলো আলাদা করার জন্য underscores ব্যবহার করা যাবে । যেমনঃ `greeting_message` সঠিক, কিন্তু `greeting message` ভুল ।
-   কিছু নির্দিস্ট word চলক হিসেবে ব্যবহার করা যাবে না । এগুলো পাইথন বিশেষ প্রয়োজনে সংরক্ষণ করে । তেমন কিছু `Keywords` ও `Built-in Functions` নিচের তালিকায় দেয়া হল। আমরা এইগুলো চলকের নামে ব্যবহার থেকে বিরত থাকব । যদিও `Built-in Functions` গুলো চলক এর নাম হিসেবে ব্যবহার করলে এররর আসবেনা, কিন্তু আমরা Function গুলোকে ওভাররাইট করা হয়ে যাবে যা আমরা চাইনা । 
    Python Keywords:
    | | | | | |
    | ------ | -------- | ------- | -------- | ------ |
    | False | await | else | import | pass |
    | None | break | except | in | raise |
    | True | class | finally | is | return |
    | and | continue | for | lambda | try |
    | as | def | from | nonlocal | while |
    | assert | del | global | not | with |
    | async | elif | if | or | yield |

    Python Built-in Functions:
    | | | | | |
    | ------------- | ----------- | ------------ | ------------ | -------------- |
    | abs() | delattr() | hash() | memoryview() | set() |
    | all() | dict() | help() | min() | setattr() |
    | any() | dir() | hex() | next() | slice() |
    | ascii() | divmod() | id() | object() | sorted() |
    | bin() | enumerate() | input() | oct() | staticmethod() |
    | bool() | eval() | int() | open() | str() |
    | breakpoint() | exec() | isinstance() | ord() | sum() |
    | bytearray() | filter() | issubclass() | pow() | super() |
    | bytes() | float() | iter() | print() | tuple() |
    | callable() | format() | len() | property() | type() |
    | chr() | frozenset() | list() | range() | vars() |
    | classmethod() | getattr() | locals() | repr() | zip() |
    | compile() | globals() | map() | reversed() | `__import__()` |
    | complex() | hasattr() | max() | round() | |

-
