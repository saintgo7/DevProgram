// Input Action
// Program 008

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program008.generated.h"

UCLASS()
class AProgram008 : public AActor
{
    GENERATED_BODY()

public:
    AProgram008();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
