// Player State
// Program 053

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program053.generated.h"

UCLASS()
class AProgram053 : public AActor
{
    GENERATED_BODY()

public:
    AProgram053();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
