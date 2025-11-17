// Add Force
// Program 063

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program063.generated.h"

UCLASS()
class AProgram063 : public AActor
{
    GENERATED_BODY()

public:
    AProgram063();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
