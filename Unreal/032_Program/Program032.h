// Animation Instance
// Program 032

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program032.generated.h"

UCLASS()
class AProgram032 : public AActor
{
    GENERATED_BODY()

public:
    AProgram032();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
