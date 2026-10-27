import torch
import matplotlib.pyplot as plt
import torch.nn.functional as F

words = open('names.txt', 'r').read().splitlines()

N = torch.zeros((27, 27), dtype=torch.int32)
chars = sorted(list(set(''.join(words))))


stoi = {s: i+1 for i, s in enumerate(chars)}
stoi['.'] = 0

itos = {i: s for s, i in stoi.items()}

for w in words:
    chs = ['.'] + list(w) + ['.']
    for ch1, ch2 in zip(chs, chs[1:]):
        ix1 = stoi[ch1]
        ix2 = stoi[ch2]
        N[ix1, ix2] += 1
plt.figure(figsize=(13, 13))
plt.imshow(N, cmap='Blues')
for i in range(27):
    for j in range(27):
        chstr = itos[i] + itos[j]
        plt.text(j, i, chstr, ha='center', va='bottom', color='grey')
        plt.text(j, i, N[i, j].item(), ha='center', va='top', color='grey')
plt.axis('off')
P = (N+1).float()
P /= P.sum(1, keepdim=True)
g = torch.Generator().manual_seed(2147483647)
for i in range(5):
    out = []
    ix = 0
    while True:
        p = P[ix]
        ix = torch.multinomial(p, num_samples=1, replacement=True, generator=g).item()
        out.append(itos[ix])
        if ix == 0:
            break
log_likelihood = 0.0
n = 0.0
for w in ['marcus']:
    chs = ['.'] + list(w) + ['.']
    for ch1, ch2 in zip(chs, chs[1:]):
        ix1 = stoi[ch1]
        ix2 = stoi[ch2]
        prob = P[ix1, ix2]
        logprob = torch.log(prob)
        log_likelihood += logprob
        n += 1
        (f'{ch1}{ch2}: {prob:.4f} {logprob:.4f}')

(f'{log_likelihood=}')
nll = -log_likelihood
(f'{nll=}')
(f'{nll/n=}')



xs, ys = [], []
for w in words[:1]:
    chs = ['.'] + list(w) + ['.']
    for ch1, ch2 in zip(chs, chs[1:]):
        ix1 = stoi[ch1]
        ix2 = stoi[ch2]
        xs.append(ix1)
        ys.append(ix2)
xs = torch.tensor(xs)
ys = torch.tensor(ys)
g = torch.Generator().manual_seed(2147483647)
W = torch.randn((27,27), generator=g, requires_grad=True)
xenc = F.one_hot(xs, num_classes=27).float()
logits = (xenc @ W)
counts = logits.exp()
probs = counts / counts.sum(1, keepdim=True)

nlls = torch.zeros(5)
for i in range(5):
    x = xs[i].item()
    y = ys[i].item()
    ('-------')
    (f'bigram example {i+1}: {itos[x]}{itos[y]} (indexes {x}, {y}')
    ('input to the neural net:', x)
    ('output of probabilities of the neural net:', probs[i])
    ('label (actual next character):', y)
    p = probs[i, y]
    ('probability assigned by the net to the correct character', p.item())
    logp = torch.log(p)
    ('log probability:', logp.item())
    nll = - logp
    ('negative log-likelihood:', nll.item())
    nlls[i] = nll
('=======')
('average negative log likelihood, ie loss=', nlls.mean().item())

xenc = F.one_hot(xs, num_classes=27).float()
logits = (xenc @ W)
counts = logits.exp()
probs = counts / counts.sum(1, keepdim=True)
loss = -probs[torch.arange(5), ys].log().mean()


W.grad = None
loss.backward()
W.data += -0.1 * W.grad
(loss.item())


xs, ys = [], []
for w in words:
    chs = ['.'] + list(w) + ['.']
    for ch1, ch2 in zip(chs, chs[1:]):
        ix1 = stoi[ch1]
        ix2 = stoi[ch2]
        xs.append(ix1)
        ys.append(ix2)
xs = torch.tensor(xs)
ys = torch.tensor(ys)
num = xs.nelement()
print('number of examples:', num)
g = torch.Generator().manual_seed(2147483647)
W = torch.randn((27,27), generator=g, requires_grad=True)
for k in range(100):
    xenc = F.one_hot(xs, num_classes=27).float()
    logits = xenc @ W
    counts = logits.exp()
    probs = counts / counts.sum(1, keepdim=True)
    loss = -probs[torch.arange(num), ys].log().mean()
    print(loss.item())
    W.grad = None
    loss.backward()
    W.data += -50 * W.grad





