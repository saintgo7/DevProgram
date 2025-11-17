// Timer
// Program 026

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program026.generated.h"

UCLASS()
class AProgram026 : public AActor
{
    GENERATED_BODY()

public:
    AProgram026();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
