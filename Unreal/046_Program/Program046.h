// Widget Blueprint
// Program 046

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program046.generated.h"

UCLASS()
class AProgram046 : public AActor
{
    GENERATED_BODY()

public:
    AProgram046();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
