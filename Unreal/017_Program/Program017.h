// UActorComponent
// Program 017

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program017.generated.h"

UCLASS()
class AProgram017 : public AActor
{
    GENERATED_BODY()

public:
    AProgram017();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
