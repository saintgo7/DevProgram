// Game Mode
// Program 051

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program051.generated.h"

UCLASS()
class AProgram051 : public AActor
{
    GENERATED_BODY()

public:
    AProgram051();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
