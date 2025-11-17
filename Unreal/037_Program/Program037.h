// Behavior Tree
// Program 037

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program037.generated.h"

UCLASS()
class AProgram037 : public AActor
{
    GENERATED_BODY()

public:
    AProgram037();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
