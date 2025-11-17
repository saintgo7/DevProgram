// Hit Result
// Program 090

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program090.generated.h"

UCLASS()
class AProgram090 : public AActor
{
    GENERATED_BODY()

public:
    AProgram090();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
